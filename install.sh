#!/bin/zsh

export TOOLS_PATH=/home/tot800/tools
export INTERNAL_PATH=/home/tot800/internal

# Extractors
cd $PDF_EXTRACTOR_PATH && pip install -r requirements.txt

# Translators
cd $FR2EN_TRANSLATOR_PATH && pip install -r requirements.txt

# Internal tools
cd $INTERNAL_PATH && pip install -r requirements.txt