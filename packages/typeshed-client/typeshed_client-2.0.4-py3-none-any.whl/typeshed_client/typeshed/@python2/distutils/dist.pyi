from distutils.cmd import Command
from typing import Any, Iterable, Mapping, Text

class Distribution:
    cmdclass: dict[str, type[Command]]
    def __init__(self, attrs: Mapping[str, Any] | None = ...) -> None: ...
    def get_option_dict(self, command: str) -> dict[str, tuple[str, Text]]: ...
    def parse_config_files(self, filenames: Iterable[Text] | None = ...) -> None: ...
    def get_command_obj(self, command: str, create: bool = ...) -> Command | None: ...
