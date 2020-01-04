from flask import Flask, render_template, request, g
from sqlalchemy.dialects.postgresql.base import UUID
from flask_sqlalchemy import SQLAlchemy
import flask_sijax
from flask_migrate import Migrate
import os
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user


# instantiate the app
app =  Flask(__name__)

app.config['BASE_URL'] = os.path.dirname(__file__)

# configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/coop_app_db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' +  os.path.join(os.path.dirname(__file__), 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'usethisatyourownrisk'
# sijax setup and config 
path = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')
app.config['SIJAX_STATIC_PATH'] = path
app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'
# separete secret key for forms
app.config['WTF_CSRF_SECRET_KEY'] = 'anothersecret'

# instantiate
db = SQLAlchemy(app)
db.UUID = UUID
csrf = CSRFProtect(app)
flask_sijax.Sijax(app)

migrate = Migrate(app, db)

# Login Blueprint
from main.login.routes import login_route
app.register_blueprint(login_route)

# Home Blueprint
from main.home.routes import home_route
app.register_blueprint(home_route, url_prefix='/home')

# Company Maintenance Blueprint
from main.maintenance.company.routes import company_maintenance_route
app.register_blueprint(company_maintenance_route, url_prefix='/maintenance')

# Borrower Maintenance BluePrint
from main.maintenance.borrower.routes import borrower_maintenance_route
app.register_blueprint(borrower_maintenance_route, url_prefix='/maintenance')

# User Maintenance BluePrint
from main.maintenance.user.routes import user_maintenance_route
app.register_blueprint(user_maintenance_route, url_prefix='/maintenance')

# Member Maintenance BluePrint
from main.maintenance.member.routes import member_maintenance_route
app.register_blueprint(member_maintenance_route, url_prefix='/maintenance')


# Setup Sequence BluePrint
from main.transaction.contribution.routes import transaction_contribution_route
app.register_blueprint(transaction_contribution_route, url_prefix='/transaction')


# Setup Sequence BluePrint
from main.setup.sequence.routes import setup_sequence_route
app.register_blueprint(setup_sequence_route, url_prefix='/setup')
