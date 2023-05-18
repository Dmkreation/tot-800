#!/bin/zsh

for file in /app/exchange/*.pdf
do
    echo $file
    python app.py $file
done
