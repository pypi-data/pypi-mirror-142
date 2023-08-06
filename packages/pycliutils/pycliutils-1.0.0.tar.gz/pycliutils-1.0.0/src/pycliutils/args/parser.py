import argparse
import logging
import os
import signal
import sys
from typing import Any, Callable, Dict, Generic, List, Literal, Optional, TextIO, Type, TypeVar, Sequence, Union, cast, overload

from . import config
from .formatter import ColorFormatter

try:
    from argcomplete import autocomplete  # type: ignore[import]
except ImportError:
    def autocomplete(parser: argparse.ArgumentParser) -> None:
        ...


# pre-exec section
DEFAULT_LOG_LEVEL = logging.root.level
if ("--debug" in sys.argv) or ("-d" in sys.argv):
    DEFAULT_LOG_LEVEL = logging.DEBUG
elif ("--verbose" in sys.argv) or ("-v" in sys.argv):
    DEFAULT_LOG_LEVEL = logging.INFO


class Namespace(argparse.Namespace):
    prog: str
    version: str
    debug: bool
    _verbose: bool
    output: Optional[TextIO]

    @property
    def verbose(self) -> bool:
        return self.debug or self._verbose


N = TypeVar("N", bound=Namespace)
_N = TypeVar("_N")


class ArgumentParser(argparse.ArgumentParser, Generic[N]):
    NAME: Optional[str] = None
    DESCRIPTION: Optional[str] = None
    VERSION: Optional[str] = None
    NAMESPACE_TYPE: Type[N]
    LOGGING_FORMATTER: logging.Formatter = ColorFormatter()

    def __init__(
            self,
            prog: Optional[str] = None,
            version: Optional[str] = None,
            description: Optional[str] = None,
            epilog: Optional[str] = None,
            usage: Optional[str]=None,
            parents: List[argparse.ArgumentParser] = [],
            prefix_chars: str = "-",
            fromfile_prefix_chars: Optional[str] = None,
            argument_default: Any = None,
            conflict_handler: Literal["error", "resolve"] = "error",
            add_help: bool = True,
            allow_abbrev: bool = True,
            logger: Optional[logging.Logger] = None,
            formatter: Optional[logging.Formatter] = None) -> None:
        assert hasattr(self, "NAMESPACE_TYPE"), f"namespace type NAMESPACE_TYPE of '{self.__class__.__name__}' must be set"
        self.version = version or self.VERSION
        assert self.version is not None
        self.logger = logger or logging.getLogger()
        self.logging_formatter = formatter or self.LOGGING_FORMATTER
        super().__init__(
            prog=self.NAME or prog,
            usage=usage,
            description=description or self.DESCRIPTION,
            epilog=epilog,
            parents=parents,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            prefix_chars=prefix_chars,
            fromfile_prefix_chars=fromfile_prefix_chars,
            argument_default=argument_default,
            conflict_handler=conflict_handler,
            add_help=add_help,
            allow_abbrev=allow_abbrev)

    def error(self, message: str) -> Any:
        self.print_usage(sys.stderr)
        raise argparse.ArgumentTypeError(message)

    def __init_args__(self) -> None:
        self.add_argument("--version", action="version", version=f"%(prog)s {self.version}")
        verbosity = self.add_mutually_exclusive_group()
        verbosity.add_argument(
                "-v",
                "--verbose",
                action="store_true",
                dest="_verbose",
                help="enable verbose output")
        verbosity.add_argument(
                "-d",
                "--debug",
                action="store_true",
                help="enable debug output")
        self.add_argument(
                "-o",
                "--log-output",
                type=argparse.FileType("w"),
                default=None,
                dest="output",
                help="logging destination, default is stderr")

    @overload
    def parse_args(self, args: Optional[Sequence[str]] = ...) -> N:
        ...
    @overload
    def parse_args(self, args: Optional[Sequence[str]], namespace: None) -> N:
        ...
    @overload
    def parse_args(self, args: Optional[Sequence[str]], namespace: _N) -> _N:
        ...
    @overload
    def parse_args(self, *, namespace: None) -> N:
        ...
    @overload
    def parse_args(self, *, namespace: _N) -> _N:
        ...

    def parse_args(self, args: Optional[Sequence[str]] = None, namespace: Optional[_N] = None) -> _N:
        # set guessed logging level and add preliminary logger
        logger = self.logger
        log_level = logger.level
        logger.setLevel(DEFAULT_LOG_LEVEL)
        sh = logging.StreamHandler()
        sh.setFormatter(self.logging_formatter)
        logger.addHandler(sh)

        # initialize additional arguments
        self.__init_args__()
        # execute autocomplete
        autocomplete(self)

        if namespace is None:
            namespace = cast(_N, self.NAMESPACE_TYPE())
        setattr(namespace, "prog", self.prog)
        setattr(namespace, "version", self.version)
        argns = super().parse_args(args, namespace)

        # update logging level
        if getattr(argns, "debug", False):
            log_level = logging.DEBUG
        elif getattr(argns, "_verbose", False):
            log_level = logging.INFO
        logger.setLevel(log_level)

        # update logging handler
        logfile: Optional[TextIO] = getattr(argns, "output", None)
        if logfile is not None:
            logger.removeHandler(sh)
            sh = logging.StreamHandler(logfile)
            sh.setFormatter(self.logging_formatter)
            logger.addHandler(sh)
        return argns

    def exec(self,
            main: Callable[[N], Optional[int]],
            args: Optional[Sequence[str]] = None,
            namespace: Optional[N] = None) -> None:
        logger = self.logger
        try:
            argns: N = self.parse_args(args, namespace)
            logger.debug("running %s %s", self.prog, self.version)
            exit(main(argns) or 0)
        except Exception as exc:
            if logger.level <= logging.DEBUG:
                logger.exception(exc)
            else:
                if len(exc.args) == 0:
                    fallback = True
                    for texc, msg in config.EXCEPTION_INFORMATION.items():
                        if isinstance(exc, texc):
                            logger.error("%s: %s", self.prog, msg)
                            fallback = False
                    if fallback:
                        name = type(exc).__name__
                        name = name[name.rfind(".")+1:]
                        logger.error("%s: %s", self.prog, name)
                else:
                    logger.error("%s: %s", self.prog, ", ".join(exc.args))
            if isinstance(exc, argparse.ArgumentTypeError):
                exit(2)
            exit(1)
        except KeyboardInterrupt as kint:
            print(flush=True)
            logger.debug("%s: keyboard interrupt", argns.prog)
            signal.signal(signal.SIGINT, signal.SIG_DFL)
            os.kill(os.getpid(), signal.SIGINT)

