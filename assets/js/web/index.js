function signUpUser(){
    var email = $("#sign-up-email").val();
    var first_name = $("#sign-up-first-name").val();
	var last_name = $("#sign-up-last-name").val();
	if(validEmail(email)) {
		writeSignUpDataToDataStore(email, first_name, last_name, null, null, 'human');
	} else {
        $("#invalid-email").removeClass("hide-element");
        $("#invalid-email").addClass("help-inline");
	}
}

function signUpBusinessUser(){
    var email = $("#sign-up-email-b").val();
    var first_name = $("#sign-up-first-name-b").val();
	var last_name = $("#sign-up-last-name-b").val();
	var restaurant_name = $("#sign-up-restaurant").val();
	var comments = $("#sign-up-comments").val();
	if(validEmail(email)) {
		writeSignUpDataToDataStore(email, first_name, last_name, restaurant_name, comments, 'business');
	} else {
        $("#invalid-email-business").removeClass("hide-element");
        $("#invalid-email-business").addClass("help-inline");
	}
}

function validEmail(email) {
	var valid = false;
    if (/^\S+@\S+\.\S+$/.test(email)) {
    	valid = true;
    }
	return valid;
}

function showSuccessMessage(user_type){
	ga('send', 'event', user_type + '-signup-data', 'submit', 'Sign Up');
	clearHideAllSignUpModals();
	$('#signup-result-error').modal('hide');
	if (user_type == 'business') {
		$('#business-signup-result-success').modal('show');
	} else {
		$('#human-signup-result-success').modal('show');
	}
}

function showErrorMessage() {
	clearHideAllSignUpModals();
	$('#human-signup-result-success').modal('hide');
	$('#business-signup-result-success').modal('hide');
	$('#signup-result-error').modal('show');
}

function clearHideAllSignUpModals() {
	clearHideSignUpModal();
	clearHideBusinessSignUpModal();
}

function clearHideSignUpModal() {
	$('#signup input').val('');
    $("#invalid-email").removeClass("help-inline");
    $("#invalid-email").addClass("hide-element");
    $('#signup').modal('hide');
}

function clearHideBusinessSignUpModal() {
	$('#signup_business input').val('');
	$('#signup_business textarea').val('');
    $("#invalid-email-business").removeClass("help-inline");
    $("#invalid-email-business").addClass("hide-element");
    $('#signup_business').modal('hide');
}

function writeSignUpDataToDataStore(email, first_name, last_name, restaurant_name, comments, user_type) {
    $.ajax({
        url: '/api/users/signup',
        data: {email: email, first_name : first_name, last_name : last_name, restaurant_name : restaurant_name, comments : comments, user_type : user_type},
        type: "POST",
        success: showSuccessMessage(user_type),
        error: showErrorMessage
    });
}