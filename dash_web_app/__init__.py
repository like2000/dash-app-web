from importlib import import_module

from dash import Dash
from flask import Blueprint
from flask import Flask

from dash_web_app.dash_app1.dash_example import get_covid_dataset
from dash_web_app.dash_app1.dash_layout import html_layout


def register_blueprints(server: Flask):
    module_name = ['base']
    module = import_module(f'dash_web_app.{module_name}.routes')
    server.register_blueprint(module.blueprint)


def register_dashapp(server: Flask, layout, name: str):
    external_stylesheets = ["https://www.w3schools.com/w3css/4/w3.css", ]

    dashapp = Dash(server=server,
                   url_base_pathname=f'/{name}/',
                   # external_scripts=external_scripts,
                   # routes_pathname_prefix='/dash_app/',
                   external_stylesheets=external_stylesheets,
                   )

    with server.app_context():
        dashapp.index_string = html_layout
        dashapp.layout = layout(get_covid_dataset)

        # @dashapp.callback(Output('dash-container', 'children'), [Input(None, None)])
        # def callback():
        #     return get_covid_dataset()

        return dashapp.server


def register_extensions(server: Flask, blueprint: Blueprint):
    ...


def create_app():
    server = Flask(__name__, instance_relative_config=False)
    # app.config.from_object('config.Config')

    # Import Dash application
    from dash_web_app.dash.dash_example import layout
    register_dashapp(server, layout, "dash_app")

    # # Compile assets
    # from dash_web_app.assets import compile_assets
    # compile_assets(app)

    register_blueprints(server)

    # server.dash.das

    return server