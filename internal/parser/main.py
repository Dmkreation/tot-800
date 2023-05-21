from typing import Union
from parser.file_handler import handler as f_handler


def handlers(input: str) -> Union[None, True]:
    results = []
    results.append(f_handler(input))

    results = [x for x in results if x is not None]
    if len(results) >= 1:
        return True
