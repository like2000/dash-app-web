from flask import render_template

from . import blueprint
from .dash_app import url_base


@blueprint.route("/app1")
def app():
    """Landing page."""
    print(f"Url base {url_base}")
    return render_template('app1.html', dash_url=url_base)
