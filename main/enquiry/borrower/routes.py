from flask import Blueprint, render_template, g, request, flash
import flask_sijax
from main.models.borrower import Borrower
from main.models.loan import Loan
from flask_login import login_required
from main.enquiry.borrower.forms import BorrowerEnquiryForm
from main.spa_handler.sijax_handler import SijaxHandler
from main import csrf, db

borrower_enquiry_route = Blueprint('borrower_view', __name__)

@flask_sijax.route(borrower_enquiry_route, '/borrower_view')
@login_required
def borrower_enquiry_function():
    # check if its sijax request
    if g.sijax.is_sijax_request:
        g.sijax.register_object(SijaxHandler)
        return g.sijax.process_request()
    else:
        all_borrowers = Borrower.query.all()
        return render_template('/enquiry/borrower/borrower_enquiry_base.html', data=all_borrowers, content_to_load='List')


@flask_sijax.route(borrower_enquiry_route, '/borrower_view/<uuid>')
@login_required
def borrower_enquiry_view_function(uuid):
    
    # check if its sijax request
    if g.sijax.is_sijax_request:
        g.sijax.register_object(SijaxHandler)
        return g.sijax.process_request()
    else:
        get_borrower = Borrower.query.filter_by(uuid=uuid).first()
        form = BorrowerEnquiryForm(obj=get_borrower)

        if get_borrower:
            all_loans = Loan.query.filter_by(borrower_code=get_borrower.code).all()
            content_to_load = 'View'
        else:
            content_to_load = 'Error'
            all_loans = []

        return render_template('/enquiry/borrower/borrower_enquiry_base.html', form=form, content_to_load=content_to_load, data=all_loans)