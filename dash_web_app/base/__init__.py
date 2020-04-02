from flask import Blueprint

name = 'base'

blueprint = Blueprint(
    import_name=__name__,
    static_folder='static',
    name=name + '_blueprint',
    template_folder='templates',
)
