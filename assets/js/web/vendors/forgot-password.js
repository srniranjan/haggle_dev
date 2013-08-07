passwordResetHandler = function () {
    function init() {
        $("#password-forgot-form").submit(function (event) {
            event.preventDefault();
            var form = $(this);
            $.ajax({
                url:form.attr("action"),
                data:form.serialize(),
                type:"POST",
                success:handleForgotSuccess,
                error:handleForgotFailed
            });
        });
    }
    return init;
}();

function handleForgotSuccess(data) {
    var message = $("#valid-email-message");
    message.removeClass("hide-element");
    $("#controls").addClass("hide-element");
}

function handleForgotFailed(data) {
    var message = $("#invalid-email-message");
    message.removeClass("hide-element");
}

$(function () {
    new passwordResetHandler();
});