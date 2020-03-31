from flask import Blueprint

name = 'dash'

blueprint = Blueprint(
    name + '_blueprint',
    __name__,
    url_prefix='/' + name,
    static_folder='static',
    template_folder='templates',
)
