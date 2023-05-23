# What for?
This is the first draft of an AI-based personal assistant, the goal is to build an application able to understand the user's request and to interact with the system and/or the web to answer the requested need. 
In a second step, the model will have to learn from its interaction with the user, in order to correct its mistakes and to calibrate itself to the system and its user.
Finally, the application and the model will have to be able to run on systems with standard performances

# Setup and Start
## Requirements
Application is full Dockerized with `python:3.11.3` image, only [Docker](https://docs.docker.com/engine/install/) and Compose are required

```shell
export app_name=tot800 # Choose a name
docker build --build-arg APP_NAME=$app_name . -t "${app_name}-app" # Build image
APP_NAME="${app_name}" docker compose up -d # Start app
APP_NAME="${app_name}" docker compose logs -f # Log until you show [APP_NAME] is started
```

After the first setup, it generate helper file in `/bin` folder
```shell
./bin/app [option] # available options: [build|start|stop|restart|log|shell]

# example
./bin/app shell
```

# Usage
```shell
./bin/app shell

python app.py # Start interaction with assistant
```

# Models
Name|Inference|Trainer
----|---------|-------
[GTP-2](models/gpt2) | ✅ | ✅
[GTP4ALL](models/gpt4all) | ✅ | ❌

# Tools
Name|Model|Library|Description
----|-----|-------|-----------
[DataExtractor::Pdf](tools/data_extractor/pdf) | | [PyPDF2](https://pypi.org/project/PyPDF2/) | extract text from .pdf files
[Translator::Fr2En](tools/translator/fr2en) | [Helsinki-NLP/opus-mt-fr-en](https://huggingface.co/Helsinki-NLP/opus-mt-fr-en) | | translate text from French to English

# Internal
Name|description
----|-----------
[cli Initializer](internal/initializer) | Create `bin/app` file at first start to easily interact with app like log, shell...
[Logger](internal/logger.py) | Set in `$PYTHONPATH` to access everywhere
[Parser](internal/parser) | Query parsers to handle actions
[Parser::FileHandler](internal/parser/file_handler.py) | Detect file from path and/or url in query