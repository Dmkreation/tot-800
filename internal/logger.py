from enum import Enum
import os
from datetime import datetime
from termcolor import colored


class LogLevel(Enum):
    INFO = 4
    WARNING = 3
    ERROR = 2
    DEBUG = 1


level_colors = {
    'INFO': 'white',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'DEBUG': 'white',
}


class Logger:
    def __init__(self, level: LogLevel) -> None:
        self.level = level

    def debug(self, message: str) -> None:
        if self.level.value > LogLevel.DEBUG.value:
            return None

        print(self.__message("DEBUG", message))

    def error(self, message: str) -> None:
        if self.level.value > LogLevel.ERROR.value:
            return None

        print(self.__message("ERROR", message))

    def warning(self, message: str) -> None:
        if self.level.value > LogLevel.WARNING.value:
            return None

        print(self.__message("WARNING", message))

    def info(self, message: str) -> None:
        if self.level.value > LogLevel.INFO.value:
            return None

        print(self.__message("INFO", message))

    def __message(self, level: str, message: str) -> str:
        return f"{self.__base_message(level)}{colored(message, level_colors[level])}"

    def __base_message(self, level: str) -> str:
        app_name = colored(os.environ.get('APP_NAME', 'TOT-800'), 'blue')
        now = datetime.now()
        fmt_now = colored(now.strftime("%H:%M:%S:%d/%m/%Y"), 'green')

        return f"[{fmt_now}]-[{app_name}] - {colored(level, level_colors[level])} - "


logger = Logger(LogLevel[os.environ.get('LOG_LEVEL', 'DEBUG').upper()])
