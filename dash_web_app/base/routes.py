from flask import redirect
from flask import render_template
from flask import url_for

from . import blueprint


@blueprint.route("/")
def home():
    return redirect(url_for('base_blueprint.index'))


@blueprint.route("/index")
def index():
    """Landing page."""
    return render_template('index.html', variable=None)
