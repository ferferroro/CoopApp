from flask import Blueprint, render_template, g, request, flash
import flask_sijax
from main.models.member import Member
from main.models.contribution import Contribution
from flask_login import login_required
from main.enquiry.member.forms import MemberEnquiryForm
from main.spa_handler.sijax_handler import SijaxHandler
from main import csrf, db

member_enquiry_route = Blueprint('member_view', __name__)

@flask_sijax.route(member_enquiry_route, '/member_view')
@login_required
def member_enquiry_function():
    # check if its sijax request
    if g.sijax.is_sijax_request:
        g.sijax.register_object(SijaxHandler)
        return g.sijax.process_request()
    else:
        all_members = Member.query.all()
        return render_template('/enquiry/member/member_enquiry_base.html', data=all_members, content_to_load='List')


@flask_sijax.route(member_enquiry_route, '/member_view/<uuid>')
@login_required
def member_enquiry_view_function(uuid):
    
    # check if its sijax request
    if g.sijax.is_sijax_request:
        g.sijax.register_object(SijaxHandler)
        return g.sijax.process_request()
    else:
        get_member = Member.query.filter_by(uuid=uuid).first()
        form = MemberEnquiryForm(obj=get_member)

        if get_member:
            all_contributions = Contribution.query.filter_by(member_code=get_member.code).all()
            content_to_load = 'View'
        else:
            content_to_load = 'Error'
            all_contributions = []

        return render_template('/enquiry/member/member_enquiry_base.html', form=form, content_to_load=content_to_load, data=all_contributions)