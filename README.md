# Setup and Start
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
|name|inference|trainer|
|[GTP-2](models/gpt2)|✅|✅|
|[GTP4ALL](models/gpt4all)|✅|❌|

# Tools
|name|model|library|description|
|[DataExtractor::Pdf](tools/data_extractor/pdf)||[PyPDF2](https://pypi.org/project/PyPDF2/)|extract text from .pdf files|
|[Translator::Fr2En](tools/translator/fr2en)|[Helsinki-NLP/opus-mt-fr-en](https://huggingface.co/Helsinki-NLP/opus-mt-fr-en)||translate text from French to English|

# Internal
|name|description|
|[cli Initializer](internal/initializer)|Create `bin/app` file at first start to easily interact with app like log, shell...|
|[Logger](internal/logger.py)|Set in `$PYTHONPATH` to access everywhere|
|[Parser](internal/parser)|Query parsers to handle actions|
|[Parser::FileHandler](internal/parser/file_handler.py)|Detect file from path and/or url in query|