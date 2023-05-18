import os
import sys
from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments, TextDataset, DataCollatorForLanguageModeling

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")


def merge_files(output_file, test_data):
    suffix = '.test.txt' if test_data else '.txt'
    dataset_path = f"{os.environ['GPT2_MODEL_PATH']}/dataset/{sys.argv[1]}"

    with open(output_file, 'w') as outfile:
        for filename in os.listdir(dataset_path):
            if filename.endswith(suffix):
                with open(os.path.join(dataset_path, filename), 'r') as readfile:
                    outfile.write(readfile.read())
                outfile.write('\n')


def load_folder(test_data):
    block_size = 128
    filename = 'tests.txt' if test_data else 'trains.txt'
    file_path = f"{os.environ['GPT2_MODEL_PATH']}/dataset/{sys.argv[1]}/{filename}"
    merge_files(file_path, test_data=test_data)

    print(f"load file at {file_path}")
    dataset = TextDataset(
        tokenizer=tokenizer,
        file_path=file_path,
        block_size=block_size,
        overwrite_cache=False
    )

    return dataset


def load_dataset():
    train_dataset = load_folder(False)
    test_dataset = load_folder(True)

    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer, mlm=False,
    )
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
