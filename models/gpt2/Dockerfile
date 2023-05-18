FROM python:3.11.3

LABEL maintainer="Eth3rnit3 <eth3rnit3@gmail.com>" version="1.0.0"

RUN apt update

RUN apt upgrade -y

RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.5/zsh-in-docker.sh)" -- \
    -t alanpeabody \
    -p https://github.com/zsh-users/zsh-autosuggestions \
    -p https://github.com/zsh-users/zsh-completions

WORKDIR /home/gpt2

COPY requirements.txt requirements.txt 

RUN pip install -r requirements.txt --upgrade pip

ENTRYPOINT [ "/home/gpt2/entrypoint.sh" ]