/**
 * @return {boolean}
 */
function validateRegistrationData(){
	var timeRegex = "\s*,*\s*(([0-1]?[0-9]|[2][0-3]):([0,3]0))\s*-\s*(([0-1]?[0-9]|[2][0-3]):([0,3]0))";
    //var weekdayHoursString = $("#weekday_hours").val();
    //var weekendHoursString = $("#weekend_hours").val();
    //var validWeekdayHours = weekdayHoursString != undefined && (weekdayHoursString.match(timeRegex) || weekdayHoursString == '');
    //var validWeekendHours = weekendHoursString != undefined && (weekendHoursString.match(timeRegex) || weekendHoursString == '');
    var validUserRating = $("#user_rating").val() != undefined && $("#user_rating").val().match("[0-5]");

    var isValid = true;
    $("#user-rating-label").removeClass("form-data-error");
    $("#weekday-hours-label").removeClass("form-data-error");
    $("#weekend-hours-label").removeClass("form-data-error");
    $("#email-label").removeClass("form-data-error");
    $("#invalid-entry-message").addClass("hide-element");


    if (!validUserRating){
        $("#user-rating-label").addClass("form-data-error");
        isValid = false;
    }
	if ($("#admin-list li").length == 0 && ($.trim($("#email").val()) == '' || $.trim($("#name").val()) == '')) {
		alert('Vendor admin required');
		if ($.trim($("#email").val()) == '') {
			$("#email-label").addClass("form-data-error");
		} else if ($.trim($("#name").val()) == '') {
			$("#name-label").addClass("form-data-error");
		}
		isValid = false;
	}
    if ($("#email").val() != '' && !/^\S+@\S+\.\S+$/.test($("#email").val())) {
		alert('email invalid');
        $("#email-label").addClass("form-data-error");
        isValid = false;
    }
    /*if (!validWeekdayHours) {
        $("#weekday-hours-label").addClass("form-data-error");
        isValid = false;
    }
    if (!validWeekendHours) {
        $("#weekend-hours-label").addClass("form-data-error");
        isValid=false;
    }*/
    if (!isValid){
        $("#invalid-entry-message").removeClass("hide-element");
    }
	if(!validateRestaurantName($("#vendor_name")[0])) {
		isValid = false;
	}
	return isValid;
}
