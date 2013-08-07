passwordChangeHandler = function () {
    function init() {
        $("#password-reset-form").submit(function (event) {
            event.preventDefault();
            if (($("#password1").val() == $("#password2").val()) && $("#password1").val() != '') {
                var form = $(this);
                $.ajax({
                    url:form.attr("action"),
                    data:form.serialize(),
                    type:"POST",
                    success:handleResetSuccess,
                    error:handleResetFailed
                });
            }
        });
    }
    return init;
}();

function handleResetSuccess(data) {
    window.location.href = "/vendors/select";
}

function handleResetFailed(data) {
    var message = $("#invalid-reset-message");
    message.removeClass("hide-element");
    message.value = $.parseJSON(data).errors;

}

function validatePassword(){
    var pass1 = $('#password1'),
        pass2 = $('#password2'),
        submit = $('#submit-button');

    // Use the complexify plugin on the first password field
    pass1.complexify({minimumChars:8, strengthScaleFactor:0.7}, function (valid, complexity) {

        if (valid) {
            pass2.removeAttr('disabled');

            pass1.parent()
                .removeClass('error')
                .addClass('success');
        }
        else {
            pass2.attr('disabled', 'true');

            pass1.parent()
                .removeClass('success')
                .addClass('error');
        }

        var desc = [];
        desc[0] = "Very Weak";
        desc[1] = "Weak";
        desc[2] = "Better";
        desc[3] = "Medium";
        desc[4] = "Strong";
        desc[5] = "Strongest";
        var score = 0;
        if(complexity > 10){
            score++;
        }
        if (complexity >30){
            score++;
        }
        if(complexity >50){
            score++;
        }
        if(complexity >70){
            score++;
        }
        if(complexity >85){
            score++;
        }

        document.getElementById("passwordDescription").innerHTML = desc[score];
        document.getElementById("passwordStrength").className = "strength" + score;

    });

    // Validate the second password field
    pass2.on('keydown input', function () {

        // Make sure its value equals the first's
        if (pass2.val() == pass1.val()) {

            pass2.parent()
                .removeClass('error')
                .addClass('success');
            submit.removeAttr("disabled");

        }
        else {
            pass2.parent()
                .removeClass('success')
                .addClass('error');
            submit.attr("disabled", "true");
        }
    });
}

$(function () {
    new passwordChangeHandler();
    validatePassword();
});