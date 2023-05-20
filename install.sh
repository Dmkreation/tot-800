#!/bin/zsh

export TOOLS_PATH=$ROOT_PATH/tools
export INTERNAL_PATH=$ROOT_PATH/internal

# Extractors
cd $PDF_EXTRACTOR_PATH && pip install -r requirements.txt

# Translators
cd $FR2EN_TRANSLATOR_PATH && pip install -r requirements.txt

# Models
cd $GPT2_MODEL_PATH && pip install -r requirements.txt
cd $GPT4ALL_MODEL_PATH && pip install -r requirements.txt

# Internal tools
cd $INTERNAL_PATH && pip install -r requirements.txt
cd $INTERNAL_PATH/initializer && python main.py