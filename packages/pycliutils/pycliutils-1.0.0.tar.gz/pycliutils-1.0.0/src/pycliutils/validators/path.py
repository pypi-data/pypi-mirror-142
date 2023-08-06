import os
import sys

from pathlib import Path

from typing import Dict, Callable, Generic, List, Optional, Tuple, Type, TypeVar, cast

import magic

from argparse import ArgumentTypeError

from . import Converter, Validator

def get_mimetype_from_file(file: Path) -> str:
    assert file.is_file()
    return  magic.Magic(mime=True).from_file(file.resolve())


def path_is_readable(path: Path) -> bool:
    return os.access(path, mode=os.R_OK)

def path_is_writable(path: Path) -> bool:  # TODO: handle existing directories
    if path.is_dir():
        raise NotImplementedError
    pre_exist = path.exists()
    if not pre_exist and not path.parent.exists():
        return path_is_writable(path.parent)
    writable = True
    try:
        with path.open("ab") as fobj:
            fobj.flush()
    except IOError:
        writable = False
    if not pre_exist:
        path.unlink()
    return writable

class PathValidator(Validator[Path]):

    def __init__(
            self,
            exists: Optional[bool] = None,
            is_absolute: Optional[bool] = None,
            is_block_device: Optional[bool] = None,
            is_char_device: Optional[bool] = None,
            is_dir: Optional[bool] = None,
            is_fifo: Optional[bool] = None,
            is_file: Optional[bool] = None,
            is_mount: Optional[bool] = None,
            is_relative_to: Optional[Path] = None,
            is_not_relative_to: Optional[Path] = None,
            is_reserved: Optional[bool] = None,
            is_socket: Optional[bool] = None,
            is_symlink: Optional[bool] = None,
            match: Optional[str] = None,
            no_match: Optional[str] = None,
            is_readable: Optional[bool] = None,
            is_writable: Optional[bool] = None,
            mimetype: Optional[str] = None,
            mimetypes: Optional[List[str]] = None) -> None:
        self.exists = exists
        self.is_absolute = is_absolute
        self.is_block_device = is_block_device
        self.is_char_device = is_char_device
        self.is_dir = is_dir
        self.is_fifo = is_fifo
        self.is_file = is_file
        self.is_mount = is_mount
        self.is_relative_to = is_relative_to
        self.is_not_relative_to = is_not_relative_to
        self.is_reserved = is_reserved
        self.is_socket = is_socket
        self.is_symlink = is_symlink
        self.match = match
        self.no_match = no_match
        self.is_readable = is_readable
        self.is_writable = is_writable
        self.mimetypes = mimetypes or []
        if mimetype is not None:
            self.mimetypes.append(mimetype)
        if len(self.mimetypes) > 0:
            assert self.is_file is not False
            self.is_file = True

    def validate(self, value: Path) -> None:
        validators: Dict[Callable[[], bool], Tuple[Optional[bool], str, str]] = {
                value.exists: (self.exists, f"{value} does not exist", f"{value} exists"),
                value.is_absolute: (self.is_absolute, f"{value} is not an absolute path", f"{value} is an absolute path"),
                value.is_block_device: (self.is_block_device, f"{value} is not a block device", f"{value} is a block device"),
                value.is_char_device: (self.is_char_device, f"{value} is not a char device", f"{value} is a char device"),
                value.is_dir: (self.is_dir, f"{value} is not a directory", f"{value} is a directory"),
                value.is_fifo: (self.is_fifo, f"{value} is not a fifo stream", f"{value} is a fifo stream"),
                value.is_file: (self.is_file, f"{value} is not a file", f"{value} is a file"),
                value.is_mount: (self.is_mount, f"{value} is not a mount", f"{value} is a mount"),
                value.is_reserved: (self.is_reserved, f"{value} is not reserved", f"{value} is reserved"),
                value.is_socket: (self.is_socket, f"{value} is not a socket", f"{value} is a socket"),
                value.is_symlink: (self.is_symlink, f"{value} is not a symlink", f"{value} is a symlink"),
                lambda: path_is_readable(value): (self.is_readable, f"{value} is not readable", f"{value} is readable"),
                lambda: path_is_writable(value): (self.is_writable, f"{value} is not writable", f"{value} is writable"),
        }
        for validator, tvalue in validators.items():
            bvalue, vfalse, vtrue = tvalue
            if bvalue is not None:
                if validator() != bvalue:
                    raise ArgumentTypeError(vfalse if bvalue else vtrue)
        if self.is_relative_to is not None:
            if not value.is_relative_to(self.is_relative_to):
                raise ArgumentTypeError(f"{value} is not relative to {self.is_relative_to}")
        if self.is_not_relative_to is not None:
            if value.is_relative_to(self.is_not_relative_to):
                raise ArgumentTypeError(f"{value} is relative to {self.is_not_relative_to}")
        if self.match is not None:
            if not value.match(self.match):
                raise ArgumentTypeError(f"{value} does not match {repr(self.match)}")
        if self.no_match is not None:
            if value.match(self.no_match):
                raise ArgumentTypeError(f"{value} matches {repr(self.no_match)}")
        if len(self.mimetypes) > 0:
            mt = get_mimetype_from_file(value)
            if mt not in self.mimetypes:
                mtl = self.mimetypes.pop()
                if len(self.mimetypes) > 1:
                    mtl = ", ".join(self.mimetypes) + " or " + mtl
                raise ArgumentTypeError(f"{value} is of type {mt}, must be {mtl}")
        return None

class ExtendedPathConverter(Converter[str, Path]):

    def convert(self, value: str) -> Path:
        if value.startswith("~"):
            value = str(Path.home()) + value[1:]
        return Path(value)

