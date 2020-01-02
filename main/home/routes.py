from flask import Blueprint, render_template, url_for, g, request
import flask_sijax
from main.models.company import Company
from flask_login import LoginManager, login_user, login_required, logout_user
from main import app, csrf
from main.spa_handler.sijax_handler import SijaxHandler

home_route = Blueprint('home', __name__)

@flask_sijax.route(home_route, '/')
@login_required
# @csrf.exempt
def home_route_function():
    # # sijax function
    # def home_responsex(obj_response):
    #     obj_response.alert('some')

    # check if its sijax request
    if g.sijax.is_sijax_request:
        # g.sijax.register_callback('sijax_homex', home_responsex)
        g.sijax.register_object(SijaxHandler)
        return g.sijax.process_request()
    else:
        return render_template('/home/home_base.html')
