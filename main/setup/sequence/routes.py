from flask import Blueprint, render_template, g, request, flash
import flask_sijax
from main.models.sequence import Sequence
from flask_login import LoginManager, login_required
from main.setup.sequence.forms import SetupSequenceForm
from main.spa_handler.sijax_handler import SijaxHandler
from main import csrf, db
import uuid

# instantiate blue print 
setup_sequence_route = Blueprint('setup', __name__)

@flask_sijax.route(setup_sequence_route, '/sequence')
@login_required
def setup_sequence_function():
    # check if its sijax request
    if g.sijax.is_sijax_request:
        g.sijax.register_object(SijaxHandler)
        return g.sijax.process_request()
    else:
        all_sequences = Sequence.query.all()
        return render_template('/setup/sequence/setup_sequence_base.html', data=all_sequences, content_to_load='List')

@flask_sijax.route(setup_sequence_route, '/sequence/add')
@login_required
def setup_sequence_add_function():

    # sijax function
    def add_setup_sequence(obj_response, setup_sequence_add_form):
        ''' Let WTForm perform the form validations '''
        # pass the dictionary to the form
        form = SetupSequenceForm(data=setup_sequence_add_form)
        # validate the form
        form.validate()

        # run action to perform
        if not form.errors.items():

            if check_sequence := Sequence.query.filter((Sequence.name==form.name.data) | (Sequence.prefix==form.prefix.data)).first():
                 flash(u'Sequence name or prefix must be unique!', 'danger')
            else:
                # instantiate new model
                new_sequence = Sequence()
                # Copies matching attributes from form onto new model 
                form.populate_obj(new_sequence)
                # genereate new uuid 
                new_sequence.uuid = str(uuid.uuid4())
                # save changes to db
                db.session.add(new_sequence)
                db.session.commit()
                form = SetupSequenceForm()
                flash(u'<a href="javascript:;" onclick="javascript:UpdateSetupSequence(' + "'" + str(new_sequence.uuid)+ "'" + ');"><strong>New Sequence</strong></a> has been saved! The form is now back to add mode.', 'success')
        else:
            flash(u'Changes has not been saved! Please check your inputs.', 'danger')

        # run the render template and place it in string variable then render-thru-sijax
        html_string = str(render_template('/setup/sequence/setup_sequence_content.html', form=form, content_to_load='Add'))
        obj_response.html('#render-thru-sijax', html_string)

    # check if its sijax request
    if g.sijax.is_sijax_request:
        g.sijax.register_callback('sijax_setup_sequence_save', add_setup_sequence)
        g.sijax.register_object(SijaxHandler)
        return g.sijax.process_request()
    else:
        form = SetupSequenceForm()
        return render_template('/setup/sequence/setup_sequence_base.html', form=form, content_to_load='Add')

@flask_sijax.route(setup_sequence_route, '/sequence/update/<uuid>')
@login_required
def setup_sequence_update(uuid):
    # sijax function
    def setup_sequence_update_save(obj_response, setup_sequence_update_form):
        # pass the dictionary to the form
        form = SetupSequenceForm(data=setup_sequence_update_form)

        if update_sequence := Sequence.query.filter_by(uuid=setup_sequence_update_form['uuid']).first():
            ''' Let WTForm perform the form validations '''
            # validate the form
            form.validate()

            # run action to perform
            if not form.errors.items():
                if unique_sequence := Sequence.query.filter((Sequence.name==form.name.data) | (Sequence.prefix==form.prefix.data)).filter(Sequence.uuid!=update_sequence.uuid).count():
                    flash(u'Sequence name or prefix already taken!', 'danger')
                else:
                    form.populate_obj(update_sequence)
                    db.session.add(update_sequence)
                    db.session.commit()
                    flash(u'Sequence has been updated!', 'success')
            else:
                flash(u'Changes has not been saved! Please check your inputs.', 'danger')

        else:
            flash(u'This record is not available!', 'danger')

        # run the render template and place it in string variable then render-thru-sijax
        html_string = str(render_template('/setup/sequence/setup_sequence_content.html', form=form, content_to_load='Update'))
        obj_response.html('#render-thru-sijax', html_string)

    # sijax function
    def setup_sequence_delete(obj_response, uuid):
        if delete_sequence := Sequence.query.filter_by(uuid=uuid).first():
            db.session.delete(delete_sequence)
            db.session.commit()    
            flash(u'Sequence has been deleted!', 'success') 
        else:
            flash(u'Record is already deleted!', 'danger')

        SijaxHandler.sijax_setup_sequence(obj_response)    

    # check if its sijax request
    if g.sijax.is_sijax_request:
        g.sijax.register_callback('sijax_setup_sequence_update_save', setup_sequence_update_save)
        g.sijax.register_callback('sijax_setup_sequence_delete', setup_sequence_delete)
        g.sijax.register_object(SijaxHandler)
        return g.sijax.process_request()
    else:
        get_sequence = Sequence.query.filter_by(uuid=uuid).first()
        form = SetupSequenceForm(obj=get_sequence)

        if get_sequence:
            content_to_load = 'Update'
        else:
            content_to_load = 'Error'

        return render_template('/setup/sequence/setup_sequence_base.html', form=form, content_to_load=content_to_load)