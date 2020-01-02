from flask import Blueprint, render_template, g, request, flash
import flask_sijax
from main.models.user import User
from flask_login import LoginManager, login_required
from main.maintenance.user.forms import UserMaintenanceForm
from main.spa_handler.sijax_handler import SijaxHandler
from main import csrf, db
import uuid

# instantiate blue print 
user_maintenance_route = Blueprint('user', __name__)

@flask_sijax.route(user_maintenance_route, '/user')
@login_required
def user_maintenance_function():
    # check if its sijax request
    if g.sijax.is_sijax_request:
        g.sijax.register_object(SijaxHandler)
        return g.sijax.process_request()
    else:
        all_users = User.query.all()
        return render_template('/maintenance/user/user_main_base.html', data=all_users, content_to_load='List')

@flask_sijax.route(user_maintenance_route, '/user/add')
@login_required
def user_maintenance_add_function():

    # sijax function
    def add_user(obj_response, user_main_add_form):
        ''' Let WTForm perform the form validations '''
        # pass the dictionary to the form
        form = UserMaintenanceForm(data=user_main_add_form)
        # validate the form
        form.validate()

        # run action to perform
        if not form.errors.items():

            if check_user := User.query.filter_by(username=form.username.data).first():
                 flash(u'Username is aready taken!', 'danger')
            else:
                # instantiate
                new_user = User()
                # Copies matching attributes from form onto user
                form.populate_obj(new_user)
                # genereate new uuid 
                new_user.uuid = str(uuid.uuid4())
                new_user.hash_password(password=new_user.password)
                # save changes to db
                db.session.add(new_user)
                db.session.commit()
                form = UserMaintenanceForm()
                flash(u'<a href="javascript:;" onclick="javascript:UpdateUser(' + "'" + new_user.uuid + "'" + ');"><strong>New User</strong></a> has been saved! The form is now back to add mode.', 'success')
        else:
            flash(u'Changes has not been saved! Please check your inputs.', 'danger')

        # run the render template and place it in string variable then render-thru-sijax
        html_string = str(render_template('/maintenance/user/user_main_content.html', form=form, content_to_load='Add'))
        obj_response.html('#render-thru-sijax', html_string)

    # check if its sijax request
    if g.sijax.is_sijax_request:
        g.sijax.register_callback('sijax_maintenance_user_save', add_user)
        g.sijax.register_object(SijaxHandler)
        return g.sijax.process_request()
    else:
        form = UserMaintenanceForm()
        return render_template('/maintenance/user/user_main_base.html', form=form, content_to_load='Add')

# sijax_maintenance_user_update
@flask_sijax.route(user_maintenance_route, '/user/update/<uuid>')
@login_required
def user_maintenance_update_function(uuid):
    # sijax function
    def user_update_save(obj_response, user_main_update_form):
        # pass the dictionary to the form
        form = UserMaintenanceForm(data=user_main_update_form)

        if update_user := User.query.filter_by(uuid=user_main_update_form['uuid']).first():
            ''' Let WTForm perform the form validations '''
            # validate the form
            form.validate()

            # run action to perform
            if not form.errors.items():
                form.populate_obj(update_user)
                update_user.hash_password(password=update_user.password)
                db.session.add(update_user)
                db.session.commit()
                flash(u'User has been updated!', 'success')
            else:
                flash(u'Changes has not been saved! Please check your inputs.', 'danger')

        else:
            flash(u'This record is not available!', 'danger')

        # run the render template and place it in string variable then render-thru-sijax
        html_string = str(render_template('/maintenance/user/user_main_content.html', form=form, content_to_load='Update'))
        obj_response.html('#render-thru-sijax', html_string)

    # sijax function
    def user_delete(obj_response, uuid):
        if delete_user := User.query.filter_by(uuid=uuid).first():
            # delete the record
            db.session.delete(delete_user)
            db.session.commit()    
            flash(u'User has been deleted!', 'success')        
        else:
            flash(u'Record is already deleted!', 'danger')

        # back to user list
        SijaxHandler.sijax_maintenance_user(obj_response)    

    # check if its sijax request
    if g.sijax.is_sijax_request:
        g.sijax.register_callback('sijax_maintenance_user_update_save', user_update_save)
        g.sijax.register_callback('sijax_maintenance_user_delete', user_delete)
        g.sijax.register_object(SijaxHandler)
        return g.sijax.process_request()
    else:
        get_user = User.query.filter_by(uuid=uuid).first()
        form = UserMaintenanceForm(obj=get_user)

        if get_user:
            content_to_load = 'Update'
        else:
            content_to_load = 'Error'

        return render_template('/maintenance/user/user_main_base.html', form=form, content_to_load=content_to_load)