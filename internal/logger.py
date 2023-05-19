from enum import Enum
import os
from datetime import datetime


class LogLevel(Enum):
    INFO = 4
    WARNING = 3
    ERROR = 2
    DEBUG = 1


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
        return f"{self.__base_message(level)}{message}"

    def __base_message(self, level: str) -> str:
        app_name = os.environ.get('APP_NAME', 'TOT-800')
        now = datetime.now()
        fmt_now = now.strftime("%H:%M:%S:%d/%m/%Y")

        return f"[{app_name}-{level}-({fmt_now})] - "


logger = Logger(LogLevel[os.environ.get('LOG_LEVEL', 'DEBUG').upper()])
