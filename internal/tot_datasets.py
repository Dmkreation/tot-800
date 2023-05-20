import inquirer
from datasets import load_dataset

available = [
    {
        "name": "nomic-ai/gpt4all-j-prompt-generations",
        "versions": ["v1.2-jazzy", "v1.1-jazzy"],
        "revision": True
    },
    {
        "name": "wikitext",
        "versions": ["wikitext-103-raw-v1", "wikitext-2-raw-v1", "wikitext-2-v1"],
        "revision": False
    },
]

ds_questions = [
    inquirer.List('dataset',
                  message="Choose a dataset",
                  choices=[d["name"] for d in available],
                  ),
]
q_dataset = inquirer.prompt(ds_questions)
dataset_name = q_dataset["dataset"]
dataset = None

for obj in available:
    if obj["name"] == dataset_name:
        dataset = obj

dsv_questions = [
    inquirer.List('version',
                  message="Choose a version",
                  choices=[v for v in dataset["versions"]],
                  ),
]
q_version = inquirer.prompt(dsv_questions)
version = q_version["version"]

if dataset['revision']:
    dataset = load_dataset(dataset["name"], revision=version)
else:
    dataset = load_dataset(dataset["name"], version)


if isinstance(dataset, dict):
    print(dataset['train'][0].keys())
    print(dataset['train'][0])
else:
    print(dataset['train'][0])
