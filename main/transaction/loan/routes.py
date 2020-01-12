from flask import Blueprint, render_template, g, request, flash
import flask_sijax
from main.models.loan import Loan
from main.transaction.loan.forms import TransactionLoanForm
from main.models.loan_detail import LoanDetail
from main.transaction.loan.forms import TransactionLoanDetailForm
from main.models.borrower import Borrower
from main.models.company import Company
from flask_login import LoginManager, login_required
from main.spa_handler.sijax_handler import SijaxHandler
from main import csrf, db
import uuid
from datetime import datetime, timedelta
from main.utils.sequence_generator import generate_sequence

transaction_loan_route = Blueprint('loan', __name__)

@flask_sijax.route(transaction_loan_route, '/loan')
@login_required
def transaction_loan_function():
    # check if its sijax request
    if g.sijax.is_sijax_request:
        g.sijax.register_object(SijaxHandler)
        return g.sijax.process_request()
    else:
        all_loans = Loan.query.order_by(Loan.code.desc()).all()
        return render_template('/transaction/loan/transaction_loan_base.html', data=all_loans, content_to_load='List')

@flask_sijax.route(transaction_loan_route, '/loan/add')
@login_required
def transaction_loan_add_function():

    # sijax function
    def add_transaction_loan(obj_response, transaction_loan_add_form):
        ''' Let WTForm perform the form validations '''
        # obj_response.alert(transaction_loan_add_form['date_start'])
        # obj_response.alert(str(datetime.strptime(transaction_loan_add_form['date_start'], '%Y-%m-%d')))

        # pass the dictionary to the form
        if transaction_loan_add_form['date_start'] != '':
            transaction_loan_add_form['date_start'] =  datetime.strptime(transaction_loan_add_form['date_start'], '%Y-%m-%d')
            
        form = TransactionLoanForm(data=transaction_loan_add_form)
        # validate the form
        form.validate()

        # run action to perform
        if not form.errors.items():
            # check if borrower exist
            if check_borrower := Borrower.query.filter_by(code=form.borrower_code.data).first():
                # instantiate 
                new_loan = Loan()
                # Copies matching attributes from form onto user
                form.populate_obj(new_loan)

                # genereate new uuid 
                new_loan.uuid = str(uuid.uuid4())   
                # new_loan.interest_amount = float(new_loan.amount) * (float(new_loan.interest_rate) * float(.01))
                new_loan.code = generate_sequence('Loan')
                # save new loan to DB
                db.session.add(new_loan)
                db.session.commit()

                # recompute the details
                recompute_loan_details(new_loan)

                form = TransactionLoanForm()
                flash(u'<a href="javascript:;" onclick="javascript:UpdateTransactionLoan(' + "'" + str(new_loan.uuid) + "'" + ');"><strong>New Transaction Loan</strong></a> has been saved! The form is now back to add mode.', 'success')
            else:
                flash(u'Member not found!', 'danger')
        else:
            flash(u'Changes has not been saved! Please check your inputs.', 'danger')  

        # run the render template and place it in string variable then render-thru-sijax
        html_string = str(render_template('/transaction/loan/transaction_loan_content.html', form=form, content_to_load='Add'))
        obj_response.html('#render-thru-sijax', html_string)

    # check if its sijax request
    if g.sijax.is_sijax_request:
        g.sijax.register_callback('sijax_transaction_loan_save', add_transaction_loan)
        g.sijax.register_object(SijaxHandler)
        return g.sijax.process_request()
    else:
        form = TransactionLoanForm()
        return render_template('/transaction/loan/transaction_loan_base.html', form=form, content_to_load='Add')

@flask_sijax.route(transaction_loan_route, '/loan/update/<uuid>')
@login_required
def transaction_loan_update_function(uuid):
    # sijax function
    def transaction_loan_update_save(obj_response, transaction_loan_update_form):

        # save updates
        # amount_update_to = float(transaction_loan_update_form['amount'])
        if transaction_loan_update_form['date_start'] != '':
            transaction_loan_update_form['date_start'] =  datetime.strptime(transaction_loan_update_form['date_start'], '%Y-%m-%d')

        # obj_response.alert(str((transaction_loan_update_form)))

        form = TransactionLoanForm(data=transaction_loan_update_form)

        if update_loan := Loan.query.filter_by(uuid=transaction_loan_update_form['uuid']).first():
            ''' Let WTForm perform the form validations '''
            # validate the form
            form.validate()

            # run action to perform
            if not form.errors.items():
                
                if check_borrower := Borrower.query.filter_by(code=form.borrower_code.data).first():
                    save_loan_code = update_loan.code
                    form.populate_obj(update_loan)
                    # update_loan.interest_amount = float(update_loan.amount) * (float(update_loan.interest_rate) * float(.01))

                    update_loan.code = save_loan_code
                    
                    # save the header values
                    db.session.commit()
                    
                    # recompute the detail lines
                    recompute_loan_details(update_loan)
                    
                    flash(u'Transaction Loan has been updated!', 'success')

                    SijaxHandler.sijax_transaction_loan_update(obj_response, transaction_loan_update_form['uuid'])
                    return
                else:
                    flash(u'Borrower not found!', 'danger')
            else:
                flash(u'Changes has not been saved! Please check your inputs.', 'danger')

        else:
            flash(u'This record is not available!', 'danger')

        # run the render template and place it in string variable then render-thru-sijax
        html_string = str(render_template('/transaction/loan/transaction_loan_content.html', form=form, content_to_load='Update'))
        obj_response.html('#render-thru-sijax', html_string)

    # sijax function
    def transaction_loan_delete(obj_response, uuid):
        if delete_loan := Loan.query.filter_by(uuid=uuid).first():
            # delete the detail record
            all_details = LoanDetail.query.filter_by(loan_code=delete_loan.code).all()
            for detail in all_details:
                db.session.delete(detail)
                db.session.commit()

            # delete the header record
            db.session.delete(delete_loan)
            db.session.commit()  
            flash(u'Transaction Loan has been deleted!', 'success')        
        else:
            flash(u'Record is already deleted!', 'danger')

        # back to list
        SijaxHandler.sijax_transaction_loan(obj_response)   

    # sijax function
    def transaction_loan_approve(obj_response, uuid):
        # obj_response.alert(uuid)
        if approve_loan := Loan.query.filter_by(uuid=uuid).first():

            if not approve_loan.is_approved:
                # mark the loan as approved
                approve_loan.type_loan = 'Loan'
                approve_loan.is_approved = True
                db.session.commit()

                # update the company fund
                if update_company := Company.query.first():
                    update_company.total_fund += approve_loan.amount_gross
                    update_company.available_fund -= approve_loan.amount
                    update_company.lended_fund += approve_loan.amount
                    update_company.total_profit += approve_loan.interest_amount
                    db.session.commit()
                flash(u'Transaction Loan has been Approved!', 'success')  
            else:
                flash(u'This Loan is already approved!', 'danger')   
        else:
            flash(u'Record is already deleted!', 'danger')

        # reload the page
        get_loan = Loan.query.filter_by(uuid=uuid).first()
        form = TransactionLoanForm(obj=get_loan)
        form_modal = TransactionLoanDetailForm()
        if get_loan:
            content_to_load = 'Update'
            form.is_approved.data = True
            get_loan_detail = LoanDetail.query.filter_by(loan_code=get_loan.code).all()
            if get_borrower := Borrower.query.filter_by(code=get_loan.borrower_code).first():
                form.borrower_name.data = str(get_borrower.first_name) + ' ' + str(get_borrower.last_name)
        else:
            content_to_load = 'Error'

        # run the render template and place it in string variable
        html_string = ''
        html_string += '<div class="animated fadeIn">'
        html_string += str(render_template('/transaction/loan/transaction_loan_content.html', form=form, form_modal=form_modal, content_to_load=content_to_load, data=get_loan_detail))
        html_string += '</div>'
        
        # render-thru-sijax
        obj_response.html('#render-thru-sijax', html_string)


    def transaction_loan_payment_modal(obj_response, uuid):
        if loan_detail := LoanDetail.query.filter_by(uuid=uuid).first():
            if loan_header := Loan.query.filter_by(code=loan_detail.loan_code).first():
                form = TransactionLoanForm(obj=loan_header)
                form_modal = TransactionLoanDetailForm(obj=loan_detail)

                html_string = ''
                html_string += str(render_template('/transaction/loan/transaction_loan_update_modal_payment.html', form=form, form_modal=form_modal))
                # click the hidden button that calls the modal
                html_string += "<script>$(document).ready(function() { $('#call-loan-detail-modal').trigger('click');}); </script>"

                
                # render-thru-sijax
                obj_response.html('#render-thru-sijax-loan-payment-modal', html_string)
            else:
                obj_response.alert('Orphan line!')
        else:
            obj_response.alert('This line does not exist')
    

    def transaction_loan_payment_modal_save(obj_response, transaction_loan_detail_update_form):

        if update_loan_detail := LoanDetail.query.filter_by(uuid=transaction_loan_detail_update_form['uuid']).first():
            # load the updated loan header
            if loan_header := Loan.query.filter_by(code=update_loan_detail.loan_code).first():
                form = TransactionLoanForm(obj=loan_header)
                # obj_response.alert(loan_header.code)

                # validate the form
                form_modal = TransactionLoanDetailForm(data=transaction_loan_detail_update_form)
                form_modal.validate()

                # run action to perform
                if not form_modal.errors.items():
                    update_loan_detail.amount_payed = float(form_modal.amount_payed.data)
                    update_loan_detail.date_payed = datetime.utcnow()
                    db.session.commit()
                    flash(u'Transaction Loan Payment has been updated!', 'success')
                    obj_response.script("$('#submit_transaction_loan_detail_cancel').trigger('click');")
                else:
                    obj_response.attr('#amount_payed', 'class', 'form-control animated fadeIn is-invalid')
                    obj_response.html('#amount_payed_error', 'Please enter a valid amount')
                    return
            else:
                flash(u'Orphan line!!!', 'danger')
        else:
            form = TransactionLoanForm()
            form_modal = TransactionLoanDetailForm()
            flash(u'This record is not available!', 'danger')
        
        SijaxHandler.sijax_transaction_loan_update(obj_response,loan_header.uuid)


    # check if its sijax request
    if g.sijax.is_sijax_request:
        g.sijax.register_callback('sijax_transaction_loan_update_save', transaction_loan_update_save)
        g.sijax.register_callback('sijax_transaction_loan_delete', transaction_loan_delete)
        g.sijax.register_callback('sijax_transaction_loan_approve', transaction_loan_approve)
        g.sijax.register_callback('sijax_transaction_loan_detail_modal', transaction_loan_payment_modal)

        g.sijax.register_callback('sijax_transaction_loan_detail_modal_save', transaction_loan_payment_modal_save)
        g.sijax.register_object(SijaxHandler)
        return g.sijax.process_request()
    else:
        get_loan = Loan.query.filter_by(uuid=uuid).first()
        form = TransactionLoanForm(obj=get_loan)
        form_modal = TransactionLoanDetailForm()

        if get_loan:
            content_to_load = 'Update'
            get_loan_detail = LoanDetail.query.filter_by(loan_code=get_loan.code).order_by(LoanDetail.term).all()
            if get_borrower := Borrower.query.filter_by(code=get_loan.borrower_code).first():
                form.borrower_name.data = str(get_borrower.first_name) + ' ' + str(get_borrower.last_name)
        else:
            content_to_load = 'Error'

        return render_template('/transaction/loan/transaction_loan_base.html', form=form, form_modal=form_modal, content_to_load=content_to_load, data=get_loan_detail)


def recompute_loan_details(loan_header_input):

    if loan_header := Loan.query.filter_by(uuid=loan_header_input.uuid).first():
        # delete the detail record
        all_details = LoanDetail.query.filter_by(loan_code=loan_header.code).all()
        for detail in all_details:
            db.session.delete(detail)
            db.session.commit()

        new_loan_detail = [] 
        running_date = loan_header.date_start
        loan_header.amount_gross = float(0)
        # if not loan_header.amount:
        #     loan_header.amount = float(0)
        # if not loan_header.interest_amount:
        #     loan_header.interest_amount = float(0)
        # if not loan_header.interest_rate:
        #     loan_header.interest_rate = float(0)

        # refresh the interest amount per line
        if loan_header.type_schedule == 'Monthly' or loan_header.terms == 1:
            loan_header.interest_amount = float(loan_header.amount) * (float(loan_header.interest_rate) * float(.01))
            date_interval = 30
        elif loan_header.type_schedule == 'Semi-Monthly':
            loan_header.interest_amount = float(loan_header.amount) * ((float(loan_header.interest_rate) * float(.01)) / 2)
            date_interval = 15

        # save the interest amount
        db.session.commit()

        # loop thru the term - each term will be one loan_detail
        for i in range(1, int(loan_header.terms) + 1):
            each_loan = LoanDetail()
            each_loan.uuid = uuid.uuid4()
            each_loan.loan_code = loan_header.code
            each_loan.term = i
            each_loan.type_line = 'Amortization'
            # each_loan.amount_to_pay = float(loan_header.amount / loan_header.terms)
            each_loan.amount_base = float(loan_header.amount / loan_header.terms)
            each_loan.amount_interest = float(loan_header.interest_amount)
            each_loan.date_to_pay = running_date 
            each_loan.amount_to_pay = each_loan.amount_base + each_loan.amount_interest
            running_date = running_date + timedelta(days=date_interval)

            '''if loan_header.type_schedule == 'Monthly' or loan_header.terms == 1:
                each_loan.amount_to_pay = float(float(each_loan.amount_to_pay) + float(loan_header.interest_amount))
                running_date = running_date + timedelta(days=30)
            elif loan_header.type_schedule == 'Semi-Monthly':
                each_loan.amount_to_pay = float(float(each_loan.amount_to_pay) + (float(loan_header.interest_amount) / float(2.0)))
                running_date = running_date + timedelta(days=14)'''

            # obj_response.alert(float(float(loan_header.amount_gross) + float(each_loan.amount_to_pay)))
            loan_header.amount_gross = float(float(loan_header.amount_gross) + float(each_loan.amount_to_pay))
            new_loan_detail.append(each_loan)

        # save new loan details to DB
        db.session.add_all(new_loan_detail)
        db.session.commit()