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


    // ##### SETUP-SEQUENCE functions START #####
    $('#setup_sequence').bind('click', function() {               
        // change the url
        ChangeUrl('', '/setup/sequence');
        // get token and call sijax to load the DOMs
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/setup/sequence');
        Sijax.request('sijax_setup_sequence', [],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });

    // call the add page 
    $(document).on('click', '#setup-sequence-call-create', function(){
        // change the url
        ChangeUrl('', '/setup/sequence/add');
        // get token and call sijax to load the DOMs
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/setup/sequence');
        Sijax.request('sijax_setup_sequence_add', [],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });

    // call save function of create new
    $(document).on('click', '#submit_setup_sequence_add', function(){
        // get token and call sijax to load the DOMs
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/setup/sequence/add');
        Sijax.request('sijax_setup_sequence_save', [Sijax.getFormValues('#setup-sequence-add-form')],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });

    $(document).on('click', '#submit_setup_sequence_update', function(){
        // get token and call sijax to load the DOMs
        var csrf_token = $('#csrf_token').val();
        var submit_type = '';
        Sijax.setRequestUri('/setup/sequence/update/' + $('#uuid').val());
        Sijax.request('sijax_setup_sequence_update_save', [Sijax.getFormValues('#setup-sequence-update-form')],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });

    $(document).on('click', '#submit_setup_sequence_delete', function(){
        ChangeUrl('', '/setup/sequence');
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/setup/sequence/update/' + $('#uuid').val());
        Sijax.request('sijax_setup_sequence_delete', [$('#uuid').val()],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });
    // ##### SETUP-SEQUENCE functions END #####



    // ##### TRANSACTION CONTRIBUTION  functions START #####
    $('#transaction_contribution').bind('click', function() {               
        // change the url
        ChangeUrl('', '/transaction/contribution');
        // get token and call sijax to load the DOMs
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/transaction/contribution');
        Sijax.request('sijax_transaction_contribution', [],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });

    // call the add page 
    $(document).on('click', '#transaction-contribution-call-create', function(){
        // change the url
        ChangeUrl('', '/transaction/contribution/add');
        // get token and call sijax to load the DOMs
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/transaction/contribution');
        Sijax.request('sijax_transaction_contribution_add', [],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });

    // call save function of create new
    $(document).on('click', '#submit_transaction_contribution_add', function(){
        // get token and call sijax to load the DOMs
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/transaction/contribution/add');
        Sijax.request('sijax_transaction_contribution_save', [Sijax.getFormValues('#transaction-contribution-add-form')],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });

    $(document).on('click', '#submit_transaction_contribution_update', function(){
        // get token and call sijax to load the DOMs
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/transaction/contribution/update/' + $('#uuid').val());
        Sijax.request('sijax_transaction_contribution_update_save', [Sijax.getFormValues('#transaction-contribution-update-form')],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });

    $(document).on('click', '#submit_transaction_contribution_delete', function(){
        ChangeUrl('', '/transaction/contribution');
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/transaction/contribution/update/' + $('#uuid').val());
        Sijax.request('sijax_transaction_contribution_delete', [$('#uuid').val()],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });
    // ##### TRANSACTION CONTRIBUTION functions END #####


    // ##### TRANSACTION CONTRIBUTION  functions START #####
    $('#transaction_loan').bind('click', function() {               
        // change the url
        ChangeUrl('', '/transaction/loan');
        // get token and call sijax to load the DOMs
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/transaction/loan');
        Sijax.request('sijax_transaction_loan', [],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });

    // call the add page 
    $(document).on('click', '#transaction-loan-call-create', function(){
        // change the url
        ChangeUrl('', '/transaction/loan/add');
        // get token and call sijax to load the DOMs
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/transaction/loan');
        Sijax.request('sijax_transaction_loan_add', [],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });

    // call save function of create new
    $(document).on('click', '#submit_transaction_loan_add', function(){
        // get token and call sijax to load the DOMs
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/transaction/loan/add');
        Sijax.request('sijax_transaction_loan_save', [Sijax.getFormValues('#transaction-loan-add-form')],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });

    $(document).on('click', '#submit_transaction_loan_update', function(){
        // get token and call sijax to load the DOMs
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/transaction/loan/update/' + $('#uuid').val());
        Sijax.request('sijax_transaction_loan_update_save', [Sijax.getFormValues('#transaction-loan-update-form')],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });

    $(document).on('click', '#submit_transaction_loan_delete', function(){
        ChangeUrl('', '/transaction/loan');
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/transaction/loan/update/' + $('#uuid').val());
        Sijax.request('sijax_transaction_loan_delete', [$('#uuid').val()],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });


    $(document).on('click', '#submit_transaction_loan_approve', function(){
        // get token and call sijax to load the DOMs
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/transaction/loan/update/' + $('#uuid').val());
        Sijax.request('sijax_transaction_loan_approve', [$('#uuid').val()],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });

    $(document).on('click', '#loan-detail-modal-link', function(){
        // get token and call sijax to load the DOMs
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/transaction/loan/update/' + $('#uuid').val());
        Sijax.request('sijax_transaction_loan_detail_modal', [$(this).attr('value')],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });

    $(document).on('click', '#submit_transaction_loan_detail_pay', function(){
        // get token and call sijax to load the DOMs
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/transaction/loan/update/' + $('#uuid').val());
        Sijax.request('sijax_transaction_loan_detail_modal_save', [Sijax.getFormValues('#transaction-loan-detail-update-form')],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });

    $(document).on('click', '#submit_transaction_loan_penalty_add', function(){
        // get token and call sijax to load the DOMs
        var csrf_token = $('#csrf_token').val();
        Sijax.setRequestUri('/transaction/loan/update/' + $('#uuid').val());
        Sijax.request('sijax_transaction_loan_detail_modal_penalty_add', [$('#uuid').val()],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });

    $(document).on('click', '#submit_transaction_loan_detail_penalty_submit', function(){
        // get token and call sijax to load the DOMs
        var csrf_token = $('#csrf_token_modal').val();
        Sijax.setRequestUri('/transaction/loan/update/' + $('#uuid').val());
        Sijax.request('sijax_transaction_loan_detail_modal_penalty_save', [Sijax.getFormValues('#transaction-loan-detail-penalty-update-form')],
            { data: { csrf_token: csrf_token } });
        //Prevent the form from being submitted
        return false;
    });

    // ##### TRANSACTION Loan functions END #####

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


// Setup has a list and this is the handler to every link!
function UpdateSetupSequence(uuid) {
    // alert(uuid);
    var csrf_token = $('#csrf_token').val();
    ChangeUrl('', '/setup/sequence/update/' + uuid);
    Sijax.setRequestUri('/setup/sequence');
    Sijax.request('sijax_setup_sequence_update', [uuid],
        { data: { csrf_token: csrf_token } });
    // Prevent the form from being submitted
    return false;
};


// Transaction Contribution has a list and this is the handler to every link!
function UpdateTransactionContribution(uuid) {
    // alert(uuid);
    var csrf_token = $('#csrf_token').val();
    ChangeUrl('', '/transaction/contribution/update/' + uuid);
    Sijax.setRequestUri('/transaction/contribution');
    Sijax.request('sijax_transaction_contribution_update', [uuid],
        { data: { csrf_token: csrf_token } });
    // Prevent the form from being submitted
    return false;
};

// Transaction Loan has a list and this is the handler to every link!
function UpdateTransactionLoan(uuid) {
    // alert(uuid);

    var csrf_token = $('#csrf_token').val();
    ChangeUrl('', '/transaction/loan/update/' + uuid);
    Sijax.setRequestUri('/transaction/loan');
    Sijax.request('sijax_transaction_loan_update', [uuid],
        { data: { csrf_token: csrf_token } });
    // Prevent the form from being submitted
    return false;
};


// Transaction Loan has a Detail list and this is the handler to every link!
function UpdateTransactionLoanDetail(uuid) {
    alert('Sorry, Loan details are auto generated!');

    // var csrf_token = $('#csrf_token').val();
    // ChangeUrl('', '/transaction/loan/update/' + uuid);
    // Sijax.setRequestUri('/transaction/loan');
    // Sijax.request('sijax_transaction_loan_update', [uuid],
    //     { data: { csrf_token: csrf_token } });
    // Prevent the form from being submitted
    return false;
};

