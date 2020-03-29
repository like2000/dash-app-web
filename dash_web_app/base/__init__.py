from flask import Blueprint

blueprint = Blueprint(
    'base',
    __name__,
    static_folder='static',
    template_folder='templates'
)
