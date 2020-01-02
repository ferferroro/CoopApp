# from flask import Blueprint, jsonify, request
# from main import csrf
# # from main.models.user import User


# login_api_route = Blueprint('login_api', __name__)

# @login_api_route.route('/login_api', methods=['POST', 'GET'])
# @csrf.exempt
# def login_api_function():
#     return jsonify({'error': 'No data passed!'})

#     # if login_data := request.get_json():
#     #      # get the values from the html form
#     #     username = request.form['username']
#     #     password = request.form['password']

#     #     # query if the user is existing on db
#     #     user = User.query.filter_by(username=username).first()

#     #     if user and user.check_password(password=password):
#     #         # login_user(user)
#     #         return redirect(url_for('home'))
#     #     else:
#     #         return render_template('index.html', message='Invalid Login!')
#     # else:
#     #     return jsonify({'error': 'No data passed!'})



            # '''# api_response = requests.post(request.base_url + 'login_api', headers={"csrf_token":request.form['csrf_token']})
            # api_response = requests.post(request.base_url + 'login_api')
            # read_response = json.loads(api_response.text)
            

            # # obj_response.alert(request.form['csrf_token'])

            # # obj_response.alert(api_response.text)
            # output = ''
            # if api_error := read_response['error']:
            #     output += '<div class="sufee-alert alert with-close alert-danger alert-dismissible fade show">'
            #     # output += '<span class="badge badge-pill badge-danger">Success</span>'
            #     output += api_error
            #     output += '<button type="button" class="close" data-dismiss="alert" aria-label="Close">'
            #     output += '<span aria-hidden="true">×</span>'
            #     output += '</button>'
            #     output += '</div>' 
            #     obj_response.html('#for-request-error', output)'''