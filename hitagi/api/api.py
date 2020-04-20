import functools

from flask import (
    Blueprint, redirect, render_template, request, url_for
)
from flask.json import jsonify

bp = Blueprint('api', __name__, url_prefix='/api')

info = {"version": "alpha", "name": "hitagi"}

@bp.route('/')
def index():
    return jsonify(info)