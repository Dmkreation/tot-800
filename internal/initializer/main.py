import os
import stat
from jinja2 import Environment, FileSystemLoader

APP_NAME = os.environ['APP_NAME']


def load_init_template():
    env = Environment(loader=FileSystemLoader(
        f"{os.environ['ROOT_PATH']}/internal/initializer"))
    return env.get_template('shortcuts.template.txt')


def init():
    template = load_init_template()
    text = template.render(app_name=APP_NAME)
    out_file = f"{os.environ['ROOT_PATH']}/bin/app"
    if not os.path.exists(f"{os.environ['ROOT_PATH']}/bin"):
        os.makedirs(f"{os.environ['ROOT_PATH']}/bin")
    with open(out_file, 'w') as f:
        f.write(text)
    os.chmod(out_file, 0o775)


init()
