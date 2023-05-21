from datasets import load_dataset
from transformers import GPT2Tokenizer, AutoModelForCausalLM, TrainingArguments, Trainer


dataset = load_dataset(
    "wikitext", "wikitext-103-raw-v1")


tokenizer = GPT2Tokenizer.from_pretrained(
    "nomic-ai/gpt4all-j", revision="v1.2-jazzy")
model = AutoModelForCausalLM.from_pretrained(
    "nomic-ai/gpt4all-j", revision="v1.2-jazzy")


def encode(examples):
    return tokenizer(examples["text"], truncation=True, padding="max_length", max_length=128)


dataset = dataset.map(encode, batched=True)


dataset.set_format(type='torch', columns=['input_ids', 'attention_mask'])


args = TrainingArguments(
    output_dir=f"{os.environ['GPT4ALL_MODEL_PATH']}/model",
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=64,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir=f"{os.environ['GPT4ALL_MODEL_PATH']}/log",
)
trainer = Trainer(
    model=model,
    args=args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["validation"],
)


trainer.train()
