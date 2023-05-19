import os
import sys
from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments, TextDataset, DataCollatorForLanguageModeling

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
dataset_path = f"{os.environ['GPT2_MODEL_PATH']}/dataset/{sys.argv[1]}"


def load_dataset():
    block_size = 128
    train_dataset = TextDataset(
        tokenizer=tokenizer,
        file_path=f"{dataset_path}/trains.txt",
        block_size=block_size,
        overwrite_cache=False
    )
    test_dataset = TextDataset(
        tokenizer=tokenizer,
        file_path=f"{dataset_path}/tests.txt",
        block_size=block_size,
        overwrite_cache=False
    )

    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer, mlm=False,
    )
    print('DATASET')
    print(f"train {len(train_dataset)}")
    print(f"test {len(test_dataset)}")
    return train_dataset, test_dataset, data_collator


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Specify dataset to train (rt2012)")
    else:
        pdf_path = sys.argv[1]
        train_dataset, test_dataset, data_collator = load_dataset()
        training_args = TrainingArguments(
            output_dir="./model",
            num_train_epochs=3,
            per_device_train_batch_size=1,
            per_device_eval_batch_size=1,
            warmup_steps=500,
            weight_decay=0.01,
            logging_dir='./logs',
        )

        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=test_dataset
        )

        trainer.train()
