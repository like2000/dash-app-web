from flask import render_template

from . import blueprint


@blueprint.route("/dash_app1")
def dash_app():
    """Landing page."""
    return render_template('dash_app.html', dash_url=dash_app.url_base)
