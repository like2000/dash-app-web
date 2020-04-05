from flask import Blueprint

name = 'base'

blueprint = Blueprint(
    name + '_blueprint',
    import_name=__name__,
    static_folder='static',
    template_folder='templates',
)
