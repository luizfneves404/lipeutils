from typing import Callable, Any


class Util:
    def __init__(
        self,
        command_name: str,
        action: Callable,
        args: dict[str, Callable[[str], Any]],
    ):
        self.command_name = command_name
        self.action = action
        self.args = args

    def add_to_subparsers(self, subparsers_bunch):
        self.util_parser = subparsers_bunch.add_parser(self.command_name)
        self.util_parser.set_defaults(func=self.action)
        if self.args is not None:
            for arg in self.args:
                self.util_parser.add_argument(arg, type=self.args[arg])
