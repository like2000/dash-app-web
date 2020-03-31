from flask import render_template

from . import blueprint


@blueprint.route("/app")
def app():
    """Landing page."""
    print(f"Url base {app.url_base}")
    return render_template('app.html', dash_url=app.url_base)
