
loginHandler = function() {
    function init() {
        $("#sign-in-form").submit(function (event) {
            event.preventDefault();
            var form = $(this);
            $.ajax({
                url:form.attr("action"),
                data:form.serialize(),
                type:"POST",
                success:handleLoginSuccess,
                error:handleLoginFailed
            });
        });
    }
    return init;
}();

function handleLoginSuccess(data){
    window.location.href = data.redirectURL;
}

function handleLoginFailed(data, textStatus){
    var message = $("#invalid-login-message");
    message.removeClass("hide-element");
    message.value = textStatus;
}

function validateEmail() {
    var email = $('#email');
    if(email.length >0){
        // Empty the fields on load
        email.val('');

        // Validate the email field
        email.on('blur', function () {

            // Very simple validation
            if (!/^\S+@\S+\.\S+$/.test(email.val())) {
                email.parent().addClass('error').removeClass('success');
            }
            else {
                email.parent().removeClass('error').addClass('success');
            }

        });
    }
}

$(function(){
    new loginHandler();
    validateEmail();
});