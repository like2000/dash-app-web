from flask import render_template

from . import blueprint


@blueprint.route("/")
@blueprint.route("/index")
def index():
    """Landing page."""
    return render_template(
        'index.html',
        template='home-template',
        title='Plotly Flask Tutorial.',
        body="This is an example homepage served with Flask."
    )
