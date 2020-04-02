from importlib import import_module

from flask import Flask
from flask import redirect
from flask import url_for

from dash_web_app.dash.app1 import Add_Dash


def register_blueprints(server: Flask):
    for module_name in ('base', 'dash'):
        module = import_module(f'dash_web_app.{module_name}.routes')
        server.register_blueprint(module.blueprint, url_prefix=f'/{module_name}')


def register_extensions(server: Flask):
    pass


def create_app():
    server = Flask(
        __name__,
        static_folder='base/static'
    )
    # server.config.from_object('config.Config')

    register_blueprints(server)
    register_extensions(server)

    server = Add_Dash(server)
    print(server.url_map)

    @server.route("/")
    def home():
        return redirect(url_for('base_blueprint.index'))

    return server
