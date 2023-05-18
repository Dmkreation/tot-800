FROM python:3.11.3

RUN apt update

RUN apt upgrade -y

WORKDIR /app

COPY . .

ENTRYPOINT [ "/app/entrypoint.sh" ]