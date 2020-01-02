from flask import Blueprint, render_template, g, request, flash
import flask_sijax
from main.models.borrower import Borrower
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from main.maintenance.borrower.forms import BorrowerMaintenanceForm
from main.spa_handler.sijax_handler import SijaxHandler
from main import csrf, db
import uuid

borrower_maintenance_route = Blueprint('borrower', __name__)

@flask_sijax.route(borrower_maintenance_route, '/borrower')
@login_required
def borrower_maintenance_function():
    # check if its sijax request
    if g.sijax.is_sijax_request:
        g.sijax.register_object(SijaxHandler)
        return g.sijax.process_request()
    else:
        all_borrowers = Borrower.query.all()
        return render_template('/maintenance/borrower/borrower_main_base.html', data=all_borrowers, content_to_load='List')

@flask_sijax.route(borrower_maintenance_route, '/borrower/add')
@login_required
def borrower_maintenance_add_function():

    # sijax function
    def add_borrower(obj_response, borrower_main_add_form):
        ''' Let WTForm perform the form validations '''
        # pass the dictionary to the form
        form = BorrowerMaintenanceForm(data=borrower_main_add_form)
        # validate the form
        form.validate()

        # run action to perform
        if not form.errors.items():
            # instantiate 
            new_borrower = Borrower()
            # Copies matching attributes from form onto user
            form.populate_obj(new_borrower)
            # genereate new uuid 
            new_borrower.uuid = str(uuid.uuid4())
            # save changes to db
            db.session.add(new_borrower)
            db.session.commit()
            form = BorrowerMaintenanceForm()
            flash(u'<a href="javascript:;" onclick="javascript:UpdateBorrower(' + "'" + new_borrower.uuid + "'" + ');"><strong>New Borrower</strong></a> has been saved! The form is now back to add mode.', 'success')
        else:
            flash(u'Changes has not been saved! Please check your inputs.', 'danger')

        # run the render template and place it in string variable then render-thru-sijax
        html_string = str(render_template('/maintenance/borrower/borrower_main_content.html', form=form, content_to_load='Add'))
        obj_response.html('#render-thru-sijax', html_string)

    # check if its sijax request
    if g.sijax.is_sijax_request:
        g.sijax.register_callback('sijax_maintenance_borrower_save', add_borrower)
        g.sijax.register_object(SijaxHandler)
        return g.sijax.process_request()
    else:
        form = BorrowerMaintenanceForm()
        return render_template('/maintenance/borrower/borrower_main_base.html', form=form, content_to_load='Add')

# sijax_maintenance_borrower_update
@flask_sijax.route(borrower_maintenance_route, '/borrower/update/<uuid>')
@login_required
def borrower_maintenance_update_function(uuid):
    # sijax function
    def borrower_update_save(obj_response, borrower_main_update_form):
        # pass the dictionary to the form
        form = BorrowerMaintenanceForm(data=borrower_main_update_form)

        if update_borrower := Borrower.query.filter_by(uuid=borrower_main_update_form['uuid']).first():
            ''' Let WTForm perform the form validations '''
            # validate the form
            form.validate()

            # run action to perform
            if not form.errors.items():
                form.populate_obj(update_borrower)
                db.session.add(update_borrower)
                db.session.commit()
                flash(u'Borrower has been updated!', 'success')
            else:
                flash(u'Changes has not been saved! Please check your inputs.', 'danger')

        else:
            flash(u'This record is not available!', 'danger')

        # run the render template and place it in string variable then render-thru-sijax
        html_string = str(render_template('/maintenance/borrower/borrower_main_content.html', form=form, content_to_load='Update'))
        obj_response.html('#render-thru-sijax', html_string)

    # sijax function
    def borrower_delete(obj_response, uuid):
        if delete_borrower := Borrower.query.filter_by(uuid=uuid).first():
            # delete the record
            db.session.delete(delete_borrower)
            db.session.commit()    
            flash(u'Borrower has been deleted!', 'success')        
        else:
            flash(u'Record is already deleted!', 'danger')

        # back to borrower list
        SijaxHandler.sijax_maintenance_borrower(obj_response)    

    # check if its sijax request
    if g.sijax.is_sijax_request:
        g.sijax.register_callback('sijax_maintenance_borrower_update_save', borrower_update_save)
        g.sijax.register_callback('sijax_maintenance_borrower_delete', borrower_delete)
        
        g.sijax.register_object(SijaxHandler)
        return g.sijax.process_request()
    else:
        get_borrower = Borrower.query.filter_by(uuid=uuid).first()
        form = BorrowerMaintenanceForm(obj=get_borrower)

        if get_borrower:
            content_to_load = 'Update'
        else:
            content_to_load = 'Error'

        return render_template('/maintenance/borrower/borrower_main_base.html', form=form, content_to_load=content_to_load)
