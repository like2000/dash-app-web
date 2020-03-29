from flask import render_template

from . import blueprint


@blueprint.route("/dash_app")
def dash_app():
    """Landing page."""
    return render_template(
        'base/templates/index.html',
        template='home-template',
        title='Plotly Flask Tutorial.',
        body="This is an example homepage served with Flask."
    )
