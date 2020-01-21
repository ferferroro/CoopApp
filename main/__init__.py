from flask import Flask, render_template, request, g
from sqlalchemy.dialects.postgresql.base import UUID
from flask_sqlalchemy import SQLAlchemy
import flask_sijax
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

# instantiate objects
app =  Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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

# Transaction Contribution BluePrint
from main.transaction.contribution.routes import transaction_contribution_route
app.register_blueprint(transaction_contribution_route, url_prefix='/transaction')

# Transaction Loan BluePrint
from main.transaction.loan.routes import transaction_loan_route
app.register_blueprint(transaction_loan_route, url_prefix='/transaction')

# Setup Sequence BluePrint
from main.setup.sequence.routes import setup_sequence_route
app.register_blueprint(setup_sequence_route, url_prefix='/setup')


