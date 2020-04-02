from flask import render_template

from . import blueprint


@blueprint.route("/index")
def index():
    """Landing page."""
    return render_template('index.html', variable=None)
