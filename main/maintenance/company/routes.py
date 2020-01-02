from flask import Blueprint, render_template, url_for, g, request, flash
import flask_sijax
from main.models.company import Company
from flask_login import LoginManager, login_user, login_required, logout_user
from main.maintenance.company.forms import CompanyMaintenanceForm
from main.spa_handler.sijax_handler import SijaxHandler
from main import csrf, db

company_maintenance_route = Blueprint('company', __name__)

@flask_sijax.route(company_maintenance_route, '/company')
@login_required
def company_maintenance_function():
    
    # sijax functions
    def update_company(obj_response, company_main_form):
        ''' Let WTForm perform the form validations '''
        # pass the dictionary to the form and validate
        form = CompanyMaintenanceForm(data=company_main_form)
        form.validate()

        # run action to perform
        if not form.errors.items():
            get_company = Company.query.first()

            # Copies matching attributes from form onto user
            form.populate_obj(get_company) 
            db.session.commit()
            flash(u'Changes has been saved!', 'success')
        else:
            flash(u'Changes has not been saved! Please check your inputs.', 'danger')

        # run the render template and place it in string variable then render-thru-sijax
        html_string = str(render_template('/maintenance/company/company_main_content.html', form=form))
        obj_response.html('#render-thru-sijax', html_string)

    # check if its sijax request
    if g.sijax.is_sijax_request:
        g.sijax.register_callback('sijax_update_company', update_company)
        g.sijax.register_object(SijaxHandler)
        return g.sijax.process_request()
    else:
        get_company = Company.query.first()
        form = CompanyMaintenanceForm(obj=get_company)
        return render_template('/maintenance/company/company_main_base.html', form=form)