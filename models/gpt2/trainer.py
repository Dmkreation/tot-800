import json

from logger import logger
from transformers import (DataCollatorForLanguageModeling, GPT2LMHeadModel,
                          GPT2Tokenizer, LineByLineTextDataset,
                          Trainer, TrainingArguments)


def load_data():
    with open('dataset/sample.json', 'r') as f:
        data = json.load(f)

    texts = [f"{item['date']} {item['text']} {item['reference']}" for item in data]
    with open('dataset/data.txt', 'w') as f:
        for item in texts:
            f.write("%s\n" % item)

    logger.info('Data loaded')
    return texts


def load_dataset():
    text = load_data()
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    tokenizer.pad_token = tokenizer.eos_token
    inputs = tokenizer(text, return_tensors='pt',
                       truncation=True, padding=True)
    dataset = LineByLineTextDataset(
        tokenizer=tokenizer,
        file_path='dataset/data.txt',
        block_size=128,
    )
    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer, mlm=False)

    logger.info('Dataset loaded')
    return inputs, dataset, data_collator


def load_model():
    logger.info('Model loaded')
    return GPT2LMHeadModel.from_pretrained('gpt2')


def load_trainer():
    inputs, dataset, data_collator = load_dataset()
    model = load_model()
    training_args = TrainingArguments(
        output_dir='model',
        num_train_epochs=1,
        learning_rate=0.1,
        per_device_train_batch_size=1,
    )
    logger.info('Trainer loaded')
    return Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=dataset,
    )


def run():
    trainer = load_trainer()
    logger.info('Train model')
    trainer.train()
    trainer.save_model()


run()
logger.info('Model trained')
