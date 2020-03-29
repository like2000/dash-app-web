from flask import Blueprint

blueprint = Blueprint(
    'dash_app1',
    __name__,
    static_folder='static',
    template_folder='templates',
)
