from main import app
from main.maintenance.company.forms import CompanyMaintenanceForm
from main.maintenance.borrower.forms import BorrowerMaintenanceForm
from main.maintenance.user.forms import  UserMaintenanceForm
from flask import render_template
from main.models.company import Company
from main.models.borrower import Borrower
from main.models.user import User
from main import csrf, db

class SijaxHandler(object):
    """A container class for all Sijax handlers.
    Grouping all Sijax handler functions in a class
    (or a Python module) allows them all to be registered with
    a single line of code.
    """
    
    @staticmethod
    def sijax_home(obj_response):
        # run the render template and place it in string variable
        html_string = str(render_template('/home/home_base_content.html'))

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
        # define form
        all_borrowers = Borrower.query.all()
        # form = CompanyMaintenanceForm(obj=get_company)

        # run the render template and place it in string variable
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