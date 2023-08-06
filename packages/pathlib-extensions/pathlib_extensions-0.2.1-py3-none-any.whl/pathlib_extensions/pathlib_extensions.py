import os
import pathlib

from mimetypes_extensions import image_file_extensions, audio_file_extensions, video_file_extensions

__all__ = [
    "PurePath", "PurePosixPath", "PureWindowsPath",
    "Path", "PosixPath", "WindowsPath",
]

#
# Internals
#

if hasattr(pathlib, "_IGNORED_ERROS"):
    _IGNORED_ERROS = pathlib._IGNORED_ERROS
else:
    from errno import ENOENT, ENOTDIR, EBADF, ELOOP

    # EBADF - guard against macOS `stat` throwing EBADF
    _IGNORED_ERROS = (ENOENT, ENOTDIR, EBADF, ELOOP)

if hasattr(pathlib, "_IGNORED_WINERRORS"):
    _IGNORED_WINERRORS = pathlib._IGNORED_WINERRORS
else:
    _IGNORED_WINERRORS = (
        21,  # ERROR_NOT_READY - drive exists but is not accessible
        123,  # ERROR_INVALID_NAME - fix for bpo-35306
        1921,  # ERROR_CANT_RESOLVE_FILENAME - fix for broken symlink pointing to itself
    )

if hasattr(pathlib, "_ignore_error"):
    _ignore_error = pathlib._ignore_error
else:
    def _ignore_error(exception):
        return (getattr(exception, 'errno', None) in _IGNORED_ERROS or
                getattr(exception, 'winerror', None) in _IGNORED_WINERRORS)


class _NormalAccessor(pathlib._NormalAccessor):
    if hasattr(os, "link"):
        link_to = os.link
    else:
        @staticmethod
        def link_to(self, target):
            raise NotImplementedError("os.link() not available on this system")


_normal_accessor = _NormalAccessor()


#
# Public API
#

class PurePath(pathlib.PurePath):
    """Base class for manipulating paths without I/O.

    PurePath represents a filesystem path and offers operations which
    don't imply any actual filesystem I/O.  Depending on your system,
    instantiating a PurePath will return either a PurePosixPath or a
    PureWindowsPath object.  You can also instantiate either of these classes
    directly, regardless of your system.
    """

    def __new__(cls, *args):
        """Construct a PurePath from one or several strings and or existing
        PurePath objects.  The strings and path objects are combined so as
        to yield a canonicalized path, which is incorporated into the
        new PurePath object.
        """
        if cls is PurePath:
            cls = PureWindowsPath if os.name == 'nt' else PurePosixPath
        return cls._from_parts(args)

    # 3.9+
    if hasattr(pathlib.PurePath, "with_stem"):
        with_stem = pathlib.PurePath.with_stem
    # 3.6-3.8
    else:
        def with_stem(self, stem):
            """Return a new path with the stem changed."""
            return self.with_name(stem + self.suffix)

    # 3.9+
    if hasattr(pathlib.PurePath, "is_relative_to"):
        is_relative_to = pathlib.PurePath.is_relative_to
    # 3.6-3.8
    else:
        def is_relative_to(self, *other):
            """Return True if the path is relative to another path or False.
            """
            try:
                self.relative_to(*other)
                return True
            except ValueError:
                return False


# Can't subclass os.PathLike from PurePath and keep the constructor
# optimizations in PurePath._parse_args().
os.PathLike.register(PurePath)


class PurePosixPath(PurePath):
    """PurePath subclass for non-Windows systems.

    On a POSIX system, instantiating a PurePath should return this object.
    However, you can also instantiate it directly on any system.
    """
    _flavour = pathlib._posix_flavour
    __slots__ = ()


class PureWindowsPath(PurePath):
    """PurePath subclass for Windows systems.

    On a Windows system, instantiating a PurePath should return this object.
    However, you can also instantiate it directly on any system.
    """
    _flavour = pathlib._windows_flavour
    __slots__ = ()


# Filesystem-accessing classes


class Path(pathlib.Path):
    """PurePath subclass that can make system calls.

    Path represents a filesystem path but unlike PurePath, also offers
    methods to do system calls on path objects. Depending on your system,
    instantiating a Path will return either a PosixPath or a WindowsPath
    object. You can also instantiate a PosixPath or WindowsPath directly,
    but cannot instantiate a WindowsPath on a POSIX system or vice versa.
    """

    def __new__(cls, *args, **kwargs):
        if cls is Path:
            cls = WindowsPath if os.name == 'nt' else PosixPath
        self = cls._from_parts(args, init=False)
        if not self._flavour.is_supported:
            raise NotImplementedError("cannot instantiate %r on your system"
                                      % (cls.__name__,))
        self._init()
        return self

    def _init(self,
              # Private non-constructor arguments
              template=None,
              ):
        self._closed = False
        if template is not None:
            self._accessor = template._accessor
        else:
            self._accessor = _normal_accessor

    # Public API

    # 3.9+
    if hasattr(pathlib.Path, "readlink"):
        readlink = pathlib.Path.readlink
    # 3.6-3.8
    else:
        def readlink(self):
            """
            Return the path to which the symbolic link points.
            """
            path = self._accessor.readlink(self)
            obj = self._from_parts((path,), init=False)
            obj._init(template=self)
            return obj

    # 3.8+
    if hasattr(pathlib.Path, "link_to"):
        link_to = pathlib.Path.link_to
    # 3.6-3.7
    else:
        def link_to(self, target):
            """
            Make the target path a hard link pointing to this path.

            Note this function does not make this path a hard link to *target*,
            despite the implication of the function and argument names. The order
            of arguments (target, link) is the reverse of Path.symlink_to, but
            matches that of os.link.
            """
            if self._closed:
                self._raise_closed()
            self._accessor.link_to(self, target)

    # Convenience functions for querying the stat results

    # 3.7+
    if hasattr(pathlib.Path, "is_mount"):
        is_mount = pathlib.Path.is_mount
    # 3.6
    else:
        def is_mount(self):
            """
            Check if this path is a POSIX mount point
            """
            # Need to exist and be a dir
            if not self.exists() or not self.is_dir():
                return False

            parent = Path(self.parent)
            try:
                parent_dev = parent.stat().st_dev
            except OSError:
                return False

            dev = self.stat().st_dev
            if dev != parent_dev:
                return True
            ino = self.stat().st_ino
            parent_ino = parent.stat().st_ino
            return ino == parent_ino

    # Experimental functions

    def is_image_file(self):
        """
        Whether this path is an image file.
        """
        try:
            return self.is_file() and (self.suffix.lower() in image_file_extensions)
        except OSError as e:
            if not _ignore_error(e):
                raise
            # Path doesn't exist or is a broken symlink
            return False
        except ValueError:
            # Non-encodable path
            return False

    def is_audio_file(self):
        """
        Whether this path is an audio file.
        """
        try:
            return self.is_file() and (self.suffix.lower() in audio_file_extensions)
        except OSError as e:
            if not _ignore_error(e):
                raise
            # Path doesn't exist or is a broken symlink
            return False
        except ValueError:
            # Non-encodable path
            return False

    def is_video_file(self):
        """
        Whether this path is a video file.
        """
        try:
            return self.is_file() and (self.suffix.lower() in video_file_extensions)
        except OSError as e:
            if not _ignore_error(e):
                raise
            # Path doesn't exist or is a broken symlink
            return False
        except ValueError:
            # Non-encodable path
            return False


class PosixPath(Path, PurePosixPath):
    """Path subclass for non-Windows systems.

    On a POSIX system, instantiating a Path should return this object.
    """
    __slots__ = ()


class WindowsPath(Path, PureWindowsPath):
    """Path subclass for Windows systems.

    On a Windows system, instantiating a Path should return this object.
    """
    __slots__ = ()

    def owner(self):
        raise NotImplementedError("Path.owner() is unsupported on this system")

    def group(self):
        raise NotImplementedError("Path.group() is unsupported on this system")

    # 3.7+
    if hasattr(pathlib.WindowsPath, "is_mount"):
        is_mount = pathlib.WindowsPath.is_mount
    # 3.6
    else:
        def is_mount(self):
            raise NotImplementedError("Path.is_mount() is unsupported on this system")
