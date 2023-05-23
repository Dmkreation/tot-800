import sys
from models.gpt4all.app import query_gpt
from internal.logger import logger
from internal.parser.main import handlers

while True:
    user_input = input("What can I do?\n\n")
    if user_input == 'exit':
        sys.exit()
    elif handlers(user_input):
        logger.info("Handlers matching")
    query_gpt(user_input)
