"""Routes for core Flask app."""
from flask import Blueprint
from flask import render_template

server_bp = Blueprint('main', __name__,
                      static_folder='static',
                      template_folder='templates')


@server_bp.route("/")
@server_bp.route("/index")
def index():
    """Landing page."""
    return render_template('index.html',
                           template='home-template',
                           title='Plotly Flask Tutorial.',
                           body="This is an example homepage served with Flask.")


@server_bp.route("/dash_app")
def dash_app():
    """Landing page."""
    return render_template('index.html',
                           template='home-template',
                           title='Plotly Flask Tutorial.',
                           body="This is an example homepage served with Flask.")
