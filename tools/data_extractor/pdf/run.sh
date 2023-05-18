#!/bin/zsh

for file in $PDF_EXTRACTOR_PATH/exchange/*.pdf
do
    echo $file
    python app.py $file
done
