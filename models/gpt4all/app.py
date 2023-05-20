import gpt4all
model = gpt4all.GPT4All("ggml-gpt4all-j-v1.3-groovy")


def query_gpt(input: str) -> str:
    messages = [
        {
            "role": "user",
            "content": input
        }
    ]
    return model.chat_completion(messages)
