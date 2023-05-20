#!/bin/zsh

# Install root dependencies
pip install -r requirements.txt --upgrade pip

# Install tools and models dependencies
./install.sh

while true
do
    echo "${APP_NAME} is started"
    sleep 10
done