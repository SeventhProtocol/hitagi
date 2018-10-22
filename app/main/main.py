import functools

from flask import (
    Blueprint, redirect, render_template, request, url_for
)


bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    return "hey"