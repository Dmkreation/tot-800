from datasets import load_dataset
from transformers import GPT2Tokenizer

dataset = load_dataset(
    "nomic-ai/gpt4all-j-prompt-generations", revision="v1.2-jazzy")

tokenizer = GPT2Tokenizer.from_pretrained(
    "nomic-ai/gpt4all-j", revision="v1.2-jazzy")


def encode(examples):
    return tokenizer(examples["text"], truncation=True, padding="max_length", max_length=128)


dataset = dataset.map(encode, batched=True)
