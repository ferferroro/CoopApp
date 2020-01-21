from main import app, csrf, db
from flask import render_template, jsonify

from main.models.company import Company
from main.maintenance.company.forms import CompanyMaintenanceForm

from main.models.borrower import Borrower
from main.maintenance.borrower.forms import BorrowerMaintenanceForm
from main.enquiry.borrower.forms import BorrowerEnquiryForm

from main.models.member import Member
from main.maintenance.member.forms import  MemberMaintenanceForm
from main.enquiry.member.forms import  MemberEnquiryForm

from main.models.user import User
from main.maintenance.user.forms import  UserMaintenanceForm

from main.models.sequence import Sequence
from main.setup.sequence.forms import  SetupSequenceForm

from main.models.contribution import Contribution
from main.transaction.contribution.forms import  TransactionContributionForm

from main.models.loan import Loan
from main.transaction.loan.forms import TransactionLoanForm

from main.models.loan_detail import LoanDetail
from main.transaction.loan.forms import TransactionLoanDetailForm

from datetime import datetime

class SijaxHandler(object):
    """A container class for all Sijax handlers.
    Grouping all Sijax handler functions in a class
    (or a Python module) allows them all to be registered with
    a single line of code.
    """
    
    @staticmethod
    def sijax_home(obj_response):        
        company = Company.query.first()
        # run the render template and place it in string variable
        html_string = str(render_template('/home/home_base_content.html', company=company))

        # render-thru-sijax
        obj_response.html('#render-thru-sijax', html_string)

    @staticmethod
    def sijax_maintenance_company(obj_response):
        # define form
        get_company = Company.query.first()
        form = CompanyMaintenanceForm(obj=get_company)

        # run the render template and place it in string variable
        html_string = ''
        html_string += '<div class="animated fadeIn">'
        html_string += str(render_template('/maintenance/company/company_main_content.html', form=form))
        html_string += '</div>'
        
        # render-thru-sijax
        obj_response.html('#render-thru-sijax', html_string)

    @staticmethod
    def sijax_maintenance_borrower(obj_response):        
        all_borrowers = Borrower.query.all()
        html_string = str(render_template('/maintenance/borrower/borrower_main_content.html', data=all_borrowers, content_to_load='List'))
        # render-thru-sijax
        obj_response.html('#render-thru-sijax', html_string)

    @staticmethod
    def sijax_maintenance_borrower_add(obj_response):
        form = BorrowerMaintenanceForm()

        # run the render template and place it in string variable
        html_string = ''
        html_string += '<div class="animated fadeIn">'
        html_string += str(render_template('/maintenance/borrower/borrower_main_content.html', form=form, content_to_load='Add'))
        html_string += '</div>'
        
        # render-thru-sijax
        obj_response.html('#render-thru-sijax', html_string)

    @staticmethod
    def sijax_maintenance_borrower_update(obj_response, uuid):
        # define form
        html_string = ''
        if get_borrower := Borrower.query.filter_by(uuid=uuid).first():
            form = BorrowerMaintenanceForm(obj=get_borrower)
            content_to_load = 'Update'
        else:
            form = BorrowerMaintenanceForm()
            content_to_load = 'Error'

        # run the render template and place it in string variable
        html_string = ''
        html_string += '<div class="animated fadeIn">'
        html_string += str(render_template('/maintenance/borrower/borrower_main_content.html', form=form, content_to_load=content_to_load))
        html_string += '</div>'
        # render-thru-sijax
        obj_response.html('#render-thru-sijax', html_string)

    # User START
    @staticmethod
    def sijax_maintenance_user(obj_response):
        # define form
        all_users = User.query.all()

        # run the render template and place it in string variable
        html_string = str(render_template('/maintenance/user/user_main_content.html', data=all_users, content_to_load='List'))
        
        # render-thru-sijax
        obj_response.html('#render-thru-sijax', html_string)

    @staticmethod
    def sijax_maintenance_user_add(obj_response):
        form = UserMaintenanceForm()

        # run the render template and place it in string variable
        html_string = ''
        html_string += '<div class="animated fadeIn">'
        html_string += str(render_template('/maintenance/user/user_main_content.html', form=form, content_to_load='Add'))
        html_string += '</div>'
        
        # render-thru-sijax
        obj_response.html('#render-thru-sijax', html_string)

    @staticmethod
    def sijax_maintenance_user_update(obj_response, uuid):
        # define form
        html_string = ''
        if get_user := User.query.filter_by(uuid=uuid).first():
            form = UserMaintenanceForm(obj=get_user)
            content_to_load = 'Update'
        else:
            form = UserMaintenanceForm()
            content_to_load = 'Error'

        # run the render template and place it in string variable
        html_string = ''
        html_string += '<div class="animated fadeIn">'
        html_string += str(render_template('/maintenance/user/user_main_content.html', form=form, content_to_load=content_to_load))
        html_string += '</div>'
        # render-thru-sijax
        obj_response.html('#render-thru-sijax', html_string)
    # User END


    # Member START
    @staticmethod
    def sijax_maintenance_member(obj_response):
        # define form
        all_members = Member.query.all()

        # run the render template and place it in string variable
        html_string = ''
        html_string += '<div class="animated fadeIn">'
        html_string += str(render_template('/maintenance/member/member_main_content.html', data=all_members, content_to_load='List'))
        html_string += '</div>'
        
        # render-thru-sijax
        obj_response.html('#render-thru-sijax', html_string)

    @staticmethod
    def sijax_maintenance_member_add(obj_response):
        form = MemberMaintenanceForm()

        # run the render template and place it in string variable
        html_string = ''
        html_string += '<div class="animated fadeIn">'
        html_string += str(render_template('/maintenance/member/member_main_content.html', form=form, content_to_load='Add'))
        html_string += '</div>'
        
        # render-thru-sijax
        obj_response.html('#render-thru-sijax', html_string)

    @staticmethod
    def sijax_maintenance_member_update(obj_response, uuid):
        # define form
        html_string = ''
        if get_member := Member.query.filter_by(uuid=uuid).first():
            form = MemberMaintenanceForm(obj=get_member)
            content_to_load = 'Update'
        else:
            form = MemberMaintenanceForm()
            content_to_load = 'Error'

        # run the render template and place it in string variable
        html_string = ''
        html_string += '<div class="animated fadeIn">'
        html_string += str(render_template('/maintenance/member/member_main_content.html', form=form, content_to_load=content_to_load))
        html_string += '</div>'
        # render-thru-sijax
        obj_response.html('#render-thru-sijax', html_string)

    # MEMBER END

    # Setup Sequence START
    @staticmethod
    def sijax_setup_sequence(obj_response):
        # define form
        all_sequences = Sequence.query.all()

        # run the render template and place it in string variable
        html_string = str(render_template('/setup/sequence/setup_sequence_content.html', data=all_sequences, content_to_load='List'))
        
        # render-thru-sijax
        obj_response.html('#render-thru-sijax', html_string)

    @staticmethod
    def sijax_setup_sequence_add(obj_response):
        form = SetupSequenceForm()

        # run the render template and place it in string variable
        html_string = ''
        html_string += '<div class="animated fadeIn">'
        html_string += str(render_template('/setup/sequence/setup_sequence_content.html', form=form, content_to_load='Add'))
        html_string += '</div>'
        
        # render-thru-sijax
        obj_response.html('#render-thru-sijax', html_string)

    @staticmethod
    def sijax_setup_sequence_update(obj_response, uuid):
        # define form
        html_string = ''
        if get_sequence := Sequence.query.filter_by(uuid=uuid).first():
            form = SetupSequenceForm(obj=get_sequence)
            content_to_load = 'Update'
        else:
            form = SetupSequenceForm()
            content_to_load = 'Error'

        # run the render template and place it in string variable
        html_string = ''
        html_string += '<div class="animated fadeIn">'
        html_string += str(render_template('/setup/sequence/setup_sequence_content.html', form=form, content_to_load=content_to_load))
        html_string += '</div>'
        # render-thru-sijax
        obj_response.html('#render-thru-sijax', html_string)
    # Setup Sequence END


    # Transaction Contribution START
    @staticmethod
    def sijax_transaction_contribution(obj_response):
        # define form
        all_contributions = Contribution.query.all()

        # run the render template and place it in string variable
        html_string = ''
        html_string += '<div class="animated fadeIn">'
        html_string += str(render_template('/transaction/contribution/transaction_contribution_content.html', data=all_contributions, content_to_load='List'))
        html_string += '</div>'
        
        # render-thru-sijax
        obj_response.html('#render-thru-sijax', html_string)

    @staticmethod
    def sijax_transaction_contribution_add(obj_response):
        form = TransactionContributionForm()

        # run the render template and place it in string variable
        html_string = ''
        html_string += '<div class="animated fadeIn">'
        html_string += str(render_template('/transaction/contribution/transaction_contribution_content.html', form=form, content_to_load='Add'))
        html_string += '</div>'
        
        # render-thru-sijax
        obj_response.html('#render-thru-sijax', html_string)

    @staticmethod
    def sijax_transaction_contribution_update(obj_response, uuid):
        # define form
        html_string = ''
        if get_contribution := Contribution.query.filter_by(uuid=uuid).first():
            form = TransactionContributionForm(obj=get_contribution)
            form.is_approved.data = get_contribution.is_approved
            content_to_load = 'Update'
        else:
            form = TransactionContributionForm()
            content_to_load = 'Error'

        # run the render template and place it in string variable
        html_string = ''
        html_string += '<div class="animated fadeIn">'
        html_string += str(render_template('/transaction/contribution/transaction_contribution_content.html', form=form, content_to_load=content_to_load))
        html_string += '</div>'
        # render-thru-sijax
        obj_response.html('#render-thru-sijax', html_string)
    # Transaction Contribution END


    # Transaction Loan START
    @staticmethod
    def sijax_transaction_loan(obj_response):
        # define form
        all_loans = Loan.query.order_by(Loan.code.desc()).all()

        # run the render template and place it in string variable
        html_string = ''
        html_string += '<div class="animated fadeIn">'
        html_string += str(render_template('/transaction/loan/transaction_loan_content.html', data=all_loans, content_to_load='List'))
        html_string += '</div>'
        
        # render-thru-sijax
        obj_response.html('#render-thru-sijax', html_string)

    @staticmethod
    def sijax_transaction_loan_add(obj_response):
        form = TransactionLoanForm()

        # run the render template and place it in string variable
        html_string = ''
        html_string += '<div class="animated fadeIn">'
        html_string += str(render_template('/transaction/loan/transaction_loan_content.html', form=form, content_to_load='Add'))
        html_string += '</div>'
        
        # render-thru-sijax
        obj_response.html('#render-thru-sijax', html_string)

    @staticmethod
    def sijax_transaction_loan_update(obj_response, uuid):
        # define form
        html_string = ''
        if get_loan := Loan.query.filter_by(uuid=uuid).first():
            content_to_load = 'Update'
            form = TransactionLoanForm(obj=get_loan)
            form_modal = TransactionLoanDetailForm()
            form.is_approved.data = get_loan.is_approved
            form.is_settled.data = get_loan.is_settled
            get_loan_detail = LoanDetail.query.filter_by(loan_code=get_loan.code).order_by(LoanDetail.term).all()
            if get_borrower := Borrower.query.filter_by(code=get_loan.borrower_code).first():
                form.borrower_name.data = str(get_borrower.first_name) + ' ' + str(get_borrower.last_name)
        else:
            form = TransactionLoanForm()
            form_modal = TransactionLoanDetailForm()
            get_loan_detail = []
            content_to_load = 'Error'

        

        # run the render template and place it in string variable
        html_string = ''
        html_string += '<div class="animated fadeIn">'
        html_string += str(render_template('/transaction/loan/transaction_loan_content.html', form=form, form_modal=form_modal, content_to_load=content_to_load, data=get_loan_detail))
        html_string += '</div>'
        # render-thru-sijax
        obj_response.html('#render-thru-sijax', html_string)
    # Transaction Loan END

    # Member search modal
    @staticmethod
    def sijax_launch_member_search_modal(obj_response, return_field):
        all_members = Member.query.all()
        html_string = str(render_template('/maintenance/member/modal/member_search_modal.html', return_field=return_field, data=all_members))
        obj_response.html('#render-thru-sijax-global-modal', html_string)
        obj_response.script("$('#call-render-thru-sijax-global-modal').trigger('click');")

    # Borrower search modal
    @staticmethod
    def sijax_launch_borrower_search_modal(obj_response, return_field):
        all_borrowers = Borrower.query.all()
        html_string = str(render_template('/maintenance/borrower/modal/borrower_search_modal.html', return_field=return_field, data=all_borrowers))
        obj_response.html('#render-thru-sijax-global-modal', html_string)
        obj_response.script("$('#call-render-thru-sijax-global-modal').trigger('click');")


    # Member Enquiry START
    @staticmethod
    def sijax_enquiry_member_view_all(obj_response):
        # define form
        all_members = Member.query.all()

        # run the render template and place it in string variable
        html_string = ''
        html_string += '<div class="animated fadeIn">'
        html_string += str(render_template('/enquiry/member/member_enquiry_content.html', data=all_members, content_to_load='List'))
        html_string += '</div>'
        
        # render-thru-sijax
        obj_response.html('#render-thru-sijax', html_string)

    @staticmethod
    def sijax_enquiry_member_view_one(obj_response, uuid):
        
        # define form
        html_string = ''
        if get_member := Member.query.filter_by(uuid=uuid).first():
            all_contributions = Contribution.query.filter_by(member_code=get_member.code).all()
            form = MemberEnquiryForm(obj=get_member)
            content_to_load = 'View'
        else:
            form = MemberEnquiryForm()
            content_to_load = 'Error'
            all_contributions = []

        # run the render template and place it in string variable
        html_string = ''
        html_string += '<div class="animated fadeIn">'
        html_string += str(render_template('/enquiry/member/member_enquiry_view.html', form=form, content_to_load=content_to_load, data=all_contributions))
        html_string += '</div>'
        # render-thru-sijax
        obj_response.html('#render-thru-sijax', html_string)

    @staticmethod
    def sijax_launch_member_contribution_modal(obj_response, uuid):
        get_contribution = Contribution.query.filter_by(uuid=uuid).first()
        html_string = str(render_template('/enquiry/member/modal/member_contribution_modal.html', data=get_contribution))
        obj_response.html('#render-thru-sijax-global-modal', html_string)
        obj_response.script("$('#call-render-thru-sijax-global-modal').trigger('click');")
    # Member Enquiry END



    # Borrower Enquiry START
    @staticmethod
    def sijax_enquiry_borrower_view_all(obj_response):
        # define form
        all_borrowers = Borrower.query.all()

        # run the render template and place it in string variable
        html_string = ''
        html_string += '<div class="animated fadeIn">'
        html_string += str(render_template('/enquiry/borrower/borrower_enquiry_content.html', data=all_borrowers, content_to_load='List'))
        html_string += '</div>'
        
        # render-thru-sijax
        obj_response.html('#render-thru-sijax', html_string)

    @staticmethod
    def sijax_enquiry_borrower_view_one(obj_response, uuid):
        # start
        html_string = ''
        if get_borrower := Borrower.query.filter_by(uuid=uuid).first():
            all_loans = Loan.query.filter_by(borrower_code=get_borrower.code).all()
            form = BorrowerEnquiryForm(obj=get_borrower)
            content_to_load = 'View'
        else:
            form = BorrowerEnquiryForm()
            content_to_load = 'Error'
            all_loans = []

        # run the render template and place it in string variable
        html_string = ''
        html_string += '<div class="animated fadeIn">'
        html_string += str(render_template('/enquiry/borrower/borrower_enquiry_view.html', form=form, content_to_load=content_to_load, data=all_loans))
        html_string += '</div>'
        # render-thru-sijax
        obj_response.html('#render-thru-sijax', html_string)

    @staticmethod
    def sijax_launch_borrower_loan_modal(obj_response, uuid):
        get_loan = Loan.query.filter_by(uuid=uuid).first()
        if get_loan:
            get_loan_detail = []
            get_loan_detail = LoanDetail.query.filter_by(loan_code=get_loan.code).order_by(LoanDetail.term).all()
        html_string = str(render_template('/enquiry/borrower/modal/borrower_loan_modal.html', data=get_loan, detail=get_loan_detail))
        obj_response.html('#render-thru-sijax-global-modal', html_string)
        obj_response.script("$('#call-render-thru-sijax-global-modal').trigger('click');")
    # Borrower Enquiry END
