from flask import render_template

from . import blueprint
from .app1 import url_base


@blueprint.route("/app1")
def app1():
    """Landing page."""
    return render_template('app1.html', dash_url=url_base)
