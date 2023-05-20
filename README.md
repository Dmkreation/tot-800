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