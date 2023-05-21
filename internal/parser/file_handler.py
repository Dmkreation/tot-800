from typing import Union
import re
from logger import logger

handler_pattern = r'\b(file|fichier)\b|\b(handle|dl|download|telecharge)\b'
url_pattern = r'https?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
path_pattern = r'[\w/.\-]+(?:\.[\w]{1,5})'


def is_match(string):
    return bool(re.match(handler_pattern, string))


def find_urls(string) -> list:
    return re.findall(url_pattern, string)


def find_file_paths(string) -> list:
    return re.findall(path_pattern, string)


def handler(input: str) -> Union[None, True]:
    if not is_match(input):
        return None

    logger.info("File handler matching")
    urls = find_urls(input)
    paths = find_file_paths(input)
    if len(urls) >= 1:
        logger.info(f"Found urls {urls}")
    elif len(paths) >= 1:
        logger.info(f"Found paths {paths}")
