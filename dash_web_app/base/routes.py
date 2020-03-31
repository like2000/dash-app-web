from flask import render_template

from . import blueprint


@blueprint.route("/")
# def route_default():
#     return redirect(url_for('base.index'))
@blueprint.route("/index")
def index():
    """Landing page."""
    print(f"Primary route: {index}")
    return render_template('index.html', variable=None)
