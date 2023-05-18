#!/bin/zsh

export TOOLS_PATH=/home/tot800/tools

# Extractors
cd $PDF_EXTRACTOR_PATH && pip install -r requirements.txt

# Translators
cd $FR2EN_TRANSLATOR_PATH && pip install -r requirements.txt