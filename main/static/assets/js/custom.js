/** Using JavaScript */
function ChangeUrl(title, url) {
    if (typeof (history.pushState) != "undefined") {
        var obj = { Title: title, Url: url };
        history.pushState(obj, obj.Title, obj.Url);
    } else {
        alert("Browser does not support HTML5.");
    }
};

$(document).ready(function() {

    // If back button is pressed for the browser to reload from the last URL
    $(window).on('popstate', function() {
        location.reload(true);
    });

    // ##### Home functions Start #####
    $('#home').bind('click', function() {
        // get token and call sijax to load the DOMs
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/home/');
        Sijax.request('sijax_home', [],
            { data: { csrf_token: csrf_token } });
        ChangeUrl('', '/home');
        //Prevent the form from being submitted
        return false;
    });
    // ##### Home functions End #####

    // ##### Company Functions Start #####
    $('#maintenance_company').bind('click', function() {
        // get token and call sijax to load the DOMs
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/maintenance/company');
        Sijax.request('sijax_maintenance_company', [],
            { data: { csrf_token: csrf_token } });
        ChangeUrl('', '/maintenance/company');
        //Prevent the form from being submitted
        return false;
    });

    $(document).on('click', '#submit_company_update', function(){
        // get token and call sijax to load the DOMs
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/maintenance/company');
        Sijax.request('sijax_update_company', [Sijax.getFormValues('#company-main-form')],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });
    // ##### Company Functions End #####


    // ##### Borrower functions start #####
    $('#maintenance_borrower').bind('click', function() {               
        // change the url
        ChangeUrl('', '/maintenance/borrower');
        // get token and call sijax to load the DOMs
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/maintenance/borrower');
        Sijax.request('sijax_maintenance_borrower', [],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });

    // call the borrower add page 
    $(document).on('click', '#borrower-main-call-create', function(){
        // change the url
        ChangeUrl('', '/maintenance/borrower/add');
        // get token and call sijax to load the DOMs
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/maintenance/borrower');
        Sijax.request('sijax_maintenance_borrower_add', [],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });

    // call save function of create new borrower
    $(document).on('click', '#submit_borrower_add', function(){
        // get token and call sijax to load the DOMs
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/maintenance/borrower/add');
        Sijax.request('sijax_maintenance_borrower_save', [Sijax.getFormValues('#borrower-main-add-form')],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });

    $(document).on('click', '#submit_borrower_update', function(){
        // get token and call sijax to load the DOMs
        var csrf_token = $('#csrf_token').val();
        var submit_type = '';
        Sijax.setRequestUri('/maintenance/borrower/update/' + $('#uuid').val());
        Sijax.request('sijax_maintenance_borrower_update_save', [Sijax.getFormValues('#borrower-main-update-form')],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });

    $(document).on('click', '#submit_borrower_delete', function(){
        ChangeUrl('', '/maintenance/borrower');
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/maintenance/borrower/update/' + $('#uuid').val());
        Sijax.request('sijax_maintenance_borrower_delete', [$('#uuid').val()],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });
    // ##### Borrower functions end #####


    // ##### USER functions START ###### //
    $('#maintenance_user').bind('click', function() {               
        // change the url
        ChangeUrl('', '/maintenance/user');
        // get token and call sijax to load the DOMs
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/maintenance/user');
        Sijax.request('sijax_maintenance_user', [],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });

    // call the borrower add page 
    $(document).on('click', '#user-main-call-create', function(){
        // change the url
        ChangeUrl('', '/maintenance/user/add');
        // get token and call sijax to load the DOMs
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/maintenance/user');
        Sijax.request('sijax_maintenance_user_add', [],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });

    // call save function of create new User
    $(document).on('click', '#submit_user_add', function(){
        // get token and call sijax to load the DOMs
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/maintenance/user/add');
        Sijax.request('sijax_maintenance_user_save', [Sijax.getFormValues('#user-main-add-form')],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });

    $(document).on('click', '#submit_user_update', function(){
        // get token and call sijax to load the DOMs
        var csrf_token = $('#csrf_token').val();
        var submit_type = '';
        Sijax.setRequestUri('/maintenance/user/update/' + $('#uuid').val());
        Sijax.request('sijax_maintenance_user_update_save', [Sijax.getFormValues('#user-main-update-form')],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });

    $(document).on('click', '#submit_user_delete', function(){
        ChangeUrl('', '/maintenance/user');
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/maintenance/user/update/' + $('#uuid').val());
        Sijax.request('sijax_maintenance_user_delete', [$('#uuid').val()],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });
    // ##### USER functions END #####

    // ##### MEMBER functions START #####
    $('#maintenance_member').bind('click', function() {               
        // change the url
        ChangeUrl('', '/maintenance/member');
        // get token and call sijax to load the DOMs
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/maintenance/member');
        Sijax.request('sijax_maintenance_member', [],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });

    // call the add page 
    $(document).on('click', '#member-main-call-create', function(){
        // change the url
        ChangeUrl('', '/maintenance/member/add');
        // get token and call sijax to load the DOMs
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/maintenance/member');
        Sijax.request('sijax_maintenance_member_add', [],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });

    // call save function of create new
    $(document).on('click', '#submit_member_add', function(){
        // get token and call sijax to load the DOMs
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/maintenance/member/add');
        Sijax.request('sijax_maintenance_member_save', [Sijax.getFormValues('#member-main-add-form')],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });

    $(document).on('click', '#submit_member_update', function(){
        // get token and call sijax to load the DOMs
        var csrf_token = $('#csrf_token').val();
        var submit_type = '';
        Sijax.setRequestUri('/maintenance/member/update/' + $('#uuid').val());
        Sijax.request('sijax_maintenance_member_update_save', [Sijax.getFormValues('#member-main-update-form')],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });

    $(document).on('click', '#submit_member_delete', function(){
        ChangeUrl('', '/maintenance/member');
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/maintenance/member/update/' + $('#uuid').val());
        Sijax.request('sijax_maintenance_member_delete', [$('#uuid').val()],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });
    // ##### MEMBER functions END #####

});


// Borrower has a list and this is the handler to every link!
function UpdateBorrower(uuid) {
    // alert(uuid);
    var csrf_token = $('#csrf_token').val();
    ChangeUrl('', '/maintenance/borrower/update/' + uuid);
    Sijax.setRequestUri('/maintenance/borrower');
    Sijax.request('sijax_maintenance_borrower_update', [uuid],
        { data: { csrf_token: csrf_token } });
    // Prevent the form from being submitted
    return false;
};

// User has a list and this is the handler to every link!
function UpdateUser(uuid) {
    // alert(uuid);
    var csrf_token = $('#csrf_token').val();
    ChangeUrl('', '/maintenance/user/update/' + uuid);
    Sijax.setRequestUri('/maintenance/user');
    Sijax.request('sijax_maintenance_user_update', [uuid],
        { data: { csrf_token: csrf_token } });
    // Prevent the form from being submitted
    return false;
};

// Member has a list and this is the handler to every link!
function UpdateMember(uuid) {
    // alert(uuid);
    var csrf_token = $('#csrf_token').val();
    ChangeUrl('', '/maintenance/member/update/' + uuid);
    Sijax.setRequestUri('/maintenance/member');
    Sijax.request('sijax_maintenance_member_update', [uuid],
        { data: { csrf_token: csrf_token } });
    // Prevent the form from being submitted
    return false;
};
