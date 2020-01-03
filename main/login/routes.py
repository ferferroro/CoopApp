from main import app
from flask import Blueprint, render_template, url_for, g, request, redirect
import flask_sijax
from main.login.forms import LoginForm
from main.models.user import User
from flask_login import LoginManager, login_user, login_required, logout_user

# instantiate and initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)

# user loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# instantiate blue print 
login_route = Blueprint('login', __name__)

# define login route
@flask_sijax.route(login_route, '/')
def login_route_function():

    # sijax function
    def login_response(obj_response, login_form):
        
        ''' Let WTForm perform the form validations '''
        # pass the dictionary to the form
        form = LoginForm(data=login_form)
        # validate the form
        form.validate()

        ''' Validate Username '''
        # get the error and the error class
        username_error, username_error_class = get_form_error(form.username.errors)
        # update the DOMs
        obj_response.attr('#username', 'class', username_error_class)
        obj_response.html('#username_error', username_error)

        ''' Validate Password '''
        # get the error and the error class
        password_error, password_error_class = get_form_error(form.password.errors)
        # update the DOMs
        obj_response.attr('#password', 'class', password_error_class)
        obj_response.html('#password_error', password_error)
        

        ''' Passed WTForm Validation? 
            Start validating if the the User exist on DB  '''
        if not form.errors.items():
                       
            login_user_error = ''
            if user := User.query.filter_by(username=form.username.data).first():
                
                if user.check_password(password=form.password.data):
                    login_user(user)
                    obj_response.redirect(url_for('home.home_route_function'))
                else:
                    login_user_error = 'Invalid password!'
            else:
                login_user_error = 'User not found!'

            if login_user_error != '':
                output = ''
                output += '<div class="sufee-alert alert with-close alert-danger alert-dismissible fade show">'
                output += login_user_error
                output += '<button type="button" class="close" data-dismiss="alert" aria-label="Close">'
                output += '<span aria-hidden="true">×</span>'
                output += '</button>'
                output += '</div>' 
                obj_response.html('#for-request-error', output)


    # check if its sijax request
    if g.sijax.is_sijax_request:
        g.sijax.register_callback('sijax_login', login_response)
        return g.sijax.process_request()
    
    # normal render
    login_form = LoginForm()
    return render_template('/login/login.html', form=login_form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login.login_route_function'))


# Function that return error and the error class
def get_form_error(input_list):
    error = ''
    error_class = 'form-control'
    if error := ','.join(input_list):
        error = ' * ' + error
        error_class = 'is-invalid ' + error_class
    
    return error, error_class
    

