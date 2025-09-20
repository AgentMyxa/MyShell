from typing import Callable
import sys

def _command_cd(*args) -> str:
    return " ".join(args)


def _command_ls(*args) -> str:
    return " ".join(args)


def _command_exit(*args) -> None:
    sys.exit(0)


_command_dict: dict[str, Callable] = dict() 

_command_dict["cd"] = _command_cd
_command_dict["ls"] = _command_ls
_command_dict["exit"] = _command_exit


def get_command(name: str) -> Callable:
    return _command_dict.get(name)