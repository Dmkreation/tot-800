FROM python:3.11.3

LABEL maintainer="Eth3rnit3 <eth3rnit3@gmail.com>" version="1.0.0"

ARG APP_NAME=tot800
ARG USER_UID=1000
ARG USER_GID=1000

RUN groupadd --gid $USER_GID $APP_NAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $APP_NAME \
    && apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y sudo wget \
    && echo $APP_NAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$APP_NAME \
    && chmod 0440 /etc/sudoers.d/$APP_NAME \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

USER $APP_NAME

RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.5/zsh-in-docker.sh)" -- \
    -t alanpeabody \
    -p https://github.com/zsh-users/zsh-autosuggestions \
    -p https://github.com/zsh-users/zsh-completions \
    -p https://github.com/zsh-users/zsh-syntax-highlighting

WORKDIR /home/$APP_NAME/app

ENV PATH="${PATH}:/home/${APP_NAME}/.local/bin"
ENV PYTHONPATH="/home/${APP_NAME}/app/internal"