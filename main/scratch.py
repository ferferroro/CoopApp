# username, password
        # obj_response.alert('Hi there!')
        # replace html content
           

        # x = LoginForm(login_form)
        form = LoginForm(data=login_form)

        form.validate()
        output = ''
        for field_name, error_messages in form.errors.items():
            for error in error_messages:
                output += '<div class="sufee-alert alert with-close alert-danger alert-dismissible fade show">'
                output += '<span class="badge badge-pill badge-danger">Success</span>'
                output += str(error)
                output += '<button type="button" class="close" data-dismiss="alert" aria-label="Close">'
                output += '<span aria-hidden="true">×</span>'
                output += '</button>'
                output += '</div>' 


        # for error in form.username.errors:
        #     output += '<div class="sufee-alert alert with-close alert-danger alert-dismissible fade show">'
        #     output += str(error)
        #     output += '<button type="button" class="close" data-dismiss="alert" aria-label="Close">'
        #     output += '<span aria-hidden="true">×</span>'
        #     output += '</button>'
        #     output += '</div>'   




@bp.route('/users/<int:id>/followed', methods=['GET'])
def get_followed(id):
    user = User.query.get_or_404(id)
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = User.to_collection_dict(user.followed, page, per_page,
                                   'api.get_followed', id=id)
    return jsonify(data)

<script type="text/javascript">

        /** Using JavaScript */
        function ChangeUrl(title, url) {
            if (typeof (history.pushState) != "undefined") {
                var obj = { Title: title, Url: url };
                history.pushState(obj, obj.Title, obj.Url);
            } else {
                alert("Browser does not support HTML5.");
            }
        }

        // Click home link
        $(function() {
            $('#home').bind('click', function() {
                
                Sijax.request('sijax_home', [],
                    { data: { csrf_token: "{{ csrf_token() }}" } });
                ChangeUrl('', '/home');
                //Prevent the form from being submitted
                return false;
            });
        });

        // Click Company maintenance
        $(function() {
            $('#maintenance_company').bind('click', function() {
                Sijax.request('sijax_maintenance_company', [],
                    { data: { csrf_token: "{{ csrf_token() }}" } });
                ChangeUrl('', '/maintenance/company');
                //Prevent the form from being submitted
                return false;
            });
        });
    </script>