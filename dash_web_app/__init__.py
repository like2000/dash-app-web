from importlib import import_module

from flask import Blueprint
from flask import Flask

from dash_web_app.dash.dash_app import Add_Dash


def register_blueprints(server: Flask):
    for module_name in ('base', 'dash'):
        module = import_module(f'dash_web_app.{module_name}.routes')
        server.register_blueprint(module.blueprint)


def register_extensions(server: Flask, blueprint: Blueprint):
    ...


def create_app():
    server = Flask(__name__, static_folder='base/static')  # , instance_relative_config=False)
    # app.config.from_object('config.Config')

    # # Compile assets
    # from dash_web_app.assets import compile_assets
    # compile_assets(app)

    register_blueprints(server)

    server = Add_Dash(server)

    return server
