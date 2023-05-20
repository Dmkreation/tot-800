import os
from transformers import GPT2LMHeadModel, GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained(
    f"{os.environ['GPT2_MODEL_PATH']}/model")
model = GPT2LMHeadModel.from_pretrained(
    f"{os.environ['GPT2_MODEL_PATH']}/model")


def query_gpt(input: str) -> None:
    input_text = input
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    sample_outputs = model.generate(
        input_ids, pad_token_id=50256, max_length=100, do_sample=True, top_k=40)
    for i, sample_output in enumerate(sample_outputs):
        print(tokenizer.decode(sample_output, skip_special_tokens=True))
