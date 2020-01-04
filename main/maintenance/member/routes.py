from flask import Blueprint, render_template, g, request, flash
import flask_sijax
from main.models.member import Member
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from main.maintenance.member.forms import MemberMaintenanceForm
from main.spa_handler.sijax_handler import SijaxHandler
from main import csrf, db
import uuid
from datetime import datetime
from main.utils.sequence_generator import generate_sequence

member_maintenance_route = Blueprint('member', __name__)

@flask_sijax.route(member_maintenance_route, '/member')
@login_required
def member_maintenance_function():
    # check if its sijax request
    if g.sijax.is_sijax_request:
        g.sijax.register_object(SijaxHandler)
        return g.sijax.process_request()
    else:
        all_members = Member.query.all()
        return render_template('/maintenance/member/member_main_base.html', data=all_members, content_to_load='List')

@flask_sijax.route(member_maintenance_route, '/member/add')
@login_required
def member_maintenance_add_function():

    # sijax function
    def add_member(obj_response, member_main_add_form):
        ''' Let WTForm perform the form validations '''
        # pass the dictionary to the form
        form = MemberMaintenanceForm(data=member_main_add_form)
        # validate the form
        form.validate()

        # run action to perform
        if not form.errors.items():
            # instantiate 
            new_member = Member()
            # Copies matching attributes from form onto user
            form.populate_obj(new_member)
            new_member.code = generate_sequence('Member')
            if new_member.code != '':
                # genereate new uuid 
                new_member.uuid = str(uuid.uuid4())
                # save changes to db
                db.session.add(new_member)
                db.session.commit()
                form = MemberMaintenanceForm()
                flash(u'<a href="javascript:;" onclick="javascript:UpdateMember(' + "'" + str(new_member.uuid) + "'" + ');"><strong>New Member</strong></a> has been saved! The form is now back to add mode.', 'success')
            else:
                flash(u'Member Sequence not been setup!', 'danger')
        else:
            flash(u'Changes has not been saved! Please check your inputs.', 'danger')

        # run the render template and place it in string variable then render-thru-sijax
        html_string = str(render_template('/maintenance/member/member_main_content.html', form=form, content_to_load='Add'))
        obj_response.html('#render-thru-sijax', html_string)

    # check if its sijax request
    if g.sijax.is_sijax_request:
        g.sijax.register_callback('sijax_maintenance_member_save', add_member)
        g.sijax.register_object(SijaxHandler)
        return g.sijax.process_request()
    else:
        form = MemberMaintenanceForm()
        return render_template('/maintenance/member/member_main_base.html', form=form, content_to_load='Add')

# sijax_maintenance_member_update
@flask_sijax.route(member_maintenance_route, '/member/update/<uuid>')
@login_required
def member_maintenance_update_function(uuid):
    # sijax function
    def member_update_save(obj_response, member_main_update_form):
        # pass the dictionary to the form
        member_main_update_form['date_joined'] =  datetime.strptime(member_main_update_form['date_joined'], '%Y-%m-%d')
        form = MemberMaintenanceForm(data=member_main_update_form)

        if update_member := Member.query.filter_by(uuid=member_main_update_form['uuid']).first():
            ''' Let WTForm perform the form validations '''
            # validate the form
            form.validate()

            # run action to perform
            if not form.errors.items():
                form.populate_obj(update_member)
                db.session.add(update_member)
                db.session.commit()
                flash(u'Member has been updated!', 'success')
            else:
                flash(u'Changes has not been saved! Please check your inputs.', 'danger')

        else:
            flash(u'This record is not available!', 'danger')

        # run the render template and place it in string variable then render-thru-sijax
        html_string = str(render_template('/maintenance/member/member_main_content.html', form=form, content_to_load='Update'))
        obj_response.html('#render-thru-sijax', html_string)

    # sijax function
    def member_delete(obj_response, uuid):
        if delete_member := Member.query.filter_by(uuid=uuid).first():
            # delete the record
            db.session.delete(delete_member)
            db.session.commit()    
            flash(u'Member has been deleted!', 'success')        
        else:
            flash(u'Record is already deleted!', 'danger')

        # back to member list
        SijaxHandler.sijax_maintenance_member(obj_response)    

    # check if its sijax request
    if g.sijax.is_sijax_request:
        g.sijax.register_callback('sijax_maintenance_member_update_save', member_update_save)
        g.sijax.register_callback('sijax_maintenance_member_delete', member_delete)
        
        g.sijax.register_object(SijaxHandler)
        return g.sijax.process_request()
    else:
        get_member = Member.query.filter_by(uuid=uuid).first()
        form = MemberMaintenanceForm(obj=get_member)

        if get_member:
            content_to_load = 'Update'
        else:
            content_to_load = 'Error'

        return render_template('/maintenance/member/member_main_base.html', form=form, content_to_load=content_to_load)
