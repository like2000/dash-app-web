from flask import Blueprint

name = 'dash'

blueprint = Blueprint(
    import_name=__name__,
    url_prefix=f'/{name}',
    static_folder='static',
    name=name + '_blueprint',
    template_folder='templates',
)
