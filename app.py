import sys
from models.gpt4all.app import query_gpt
while True:
    user_input = input("What can I do?\n\n")
    if user_input == 'exit':
        sys.exit()
    query_gpt(user_input)
