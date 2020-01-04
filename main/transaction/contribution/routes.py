from flask import Blueprint, render_template, g, request, flash
import flask_sijax
from main.models.contribution import Contribution
from main.models.member import Member
from flask_login import LoginManager, login_required
from main.transaction.contribution.forms import TransactionContributionForm
from main.spa_handler.sijax_handler import SijaxHandler
from main import csrf, db
import uuid

transaction_contribution_route = Blueprint('contribution', __name__)

@flask_sijax.route(transaction_contribution_route, '/contribution')
@login_required
def transaction_contribution_function():
    # check if its sijax request
    if g.sijax.is_sijax_request:
        g.sijax.register_object(SijaxHandler)
        return g.sijax.process_request()
    else:
        all_contributions = Contribution.query.all()
        return render_template('/transaction/contribution/transaction_contribution_base.html', data=all_contributions, content_to_load='List')

@flask_sijax.route(transaction_contribution_route, '/contribution/add')
@login_required
def transaction_contribution_add_function():

    # sijax function
    def add_transaction_contribution(obj_response, transaction_contribution_add_form):
        ''' Let WTForm perform the form validations '''
        # pass the dictionary to the form
        form = TransactionContributionForm(data=transaction_contribution_add_form)
        # validate the form
        form.validate()

        # run action to perform
        if not form.errors.items():
            if check_member := Member.query.filter_by(code=form.member_code.data).first():
                # instantiate 
                new_contribution = Contribution()
                # Copies matching attributes from form onto user
                form.populate_obj(new_contribution)
                # genereate new uuid 
                new_contribution.uuid = str(uuid.uuid4())
                # save changes to db
                db.session.add(new_contribution)
                db.session.commit()
                form = TransactionContributionForm()
                flash(u'<a href="javascript:;" onclick="javascript:UpdateTransactionContribution(' + "'" + str(new_contribution.uuid) + "'" + ');"><strong>New Transaction Contribution</strong></a> has been saved! The form is now back to add mode.', 'success')
            else:
                flash(u'Member not found!', 'danger')
        else:
            flash(u'Changes has not been saved! Please check your inputs.', 'danger')

        # run the render template and place it in string variable then render-thru-sijax
        html_string = str(render_template('/transaction/contribution/transaction_contribution_content.html', form=form, content_to_load='Add'))
        obj_response.html('#render-thru-sijax', html_string)

    # check if its sijax request
    if g.sijax.is_sijax_request:
        g.sijax.register_callback('sijax_transaction_contribution_save', add_transaction_contribution)
        g.sijax.register_object(SijaxHandler)
        return g.sijax.process_request()
    else:
        form = TransactionContributionForm()
        return render_template('/transaction/contribution/transaction_contribution_base.html', form=form, content_to_load='Add')

# sijax_maintenance_member_update
@flask_sijax.route(transaction_contribution_route, '/contribution/update/<uuid>')
@login_required
def transaction_contribution_update_function(uuid):
    # sijax function
    def transaction_contribution_update_save(obj_response, transaction_contribution_update_form):
        
        form = TransactionContributionForm(data=transaction_contribution_update_form)

        if update_contribution := Contribution.query.filter_by(uuid=transaction_contribution_update_form['uuid']).first():
            ''' Let WTForm perform the form validations '''
            # validate the form
            form.validate()

            # run action to perform
            if not form.errors.items():
                if check_member := Member.query.filter_by(code=form.member_code.data).first():
                    form.populate_obj(update_contribution)
                    db.session.commit()
                    flash(u'Transaction Contribution has been updated!', 'success')
                else:
                    flash(u'Member not found!', 'danger')
            else:
                flash(u'Changes has not been saved! Please check your inputs.', 'danger')

        else:
            flash(u'This record is not available!', 'danger')

        # run the render template and place it in string variable then render-thru-sijax
        html_string = str(render_template('/transaction/contribution/transaction_contribution_content.html', form=form, content_to_load='Update'))
        obj_response.html('#render-thru-sijax', html_string)

    # sijax function
    def transaction_contribution_delete(obj_response, uuid):
        if delete_contribution := Contribution.query.filter_by(uuid=uuid).first():
            # delete the record
            db.session.delete(delete_contribution)
            db.session.commit()    
            flash(u'Transaction Contribution has been deleted!', 'success')        
        else:
            flash(u'Record is already deleted!', 'danger')

        # back to member list
        SijaxHandler.sijax_transaction_contribution(obj_response)    

    # check if its sijax request
    if g.sijax.is_sijax_request:
        g.sijax.register_callback('sijax_transaction_contribution_update_save', transaction_contribution_update_save)
        g.sijax.register_callback('sijax_transaction_contribution_delete', transaction_contribution_delete)
        
        g.sijax.register_object(SijaxHandler)
        return g.sijax.process_request()
    else:
        get_contribution = Contribution.query.filter_by(uuid=uuid).first()
        form = TransactionContributionForm(obj=get_contribution)

        if get_contribution:
            content_to_load = 'Update'
        else:
            content_to_load = 'Error'

        return render_template('/transaction/contribution/transaction_contribution_base.html', form=form, content_to_load=content_to_load)
