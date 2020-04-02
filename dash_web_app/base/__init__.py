from flask import Blueprint

name = 'base'
url_prefix = f'/{name}'

blueprint = Blueprint(
    name + '_blueprint',
    __name__,
    url_prefix=url_prefix,
    static_folder='static',
    template_folder='templates',
)
