/**
 * @return {boolean}
 */
function validateSettingsData(){
    var timeRegex = "\s*,*\s*(([0-1]?[0-9]|[2][0-3]):([0-5][0-9]))\s*-\s*(([0-1]?[0-9]|[2][0-3]):([0-5][0-9]))";
    //var weekdayHoursString = $("#weekday_hours").val();
    //var weekendHoursString = $("#weekend_hours").val();
    //var validWeekdayHours = weekdayHoursString!=undefined && (weekdayHoursString.match(timeRegex) || weekdayHoursString == '');
    //var validWeekendHours = weekendHoursString!=undefined && (weekendHoursString.match(timeRegex) || weekendHoursString == '');

    var isValid = true;
    $("#weekday-hours-label").removeClass("form-data-error");
    $("#weekend-hours-label").removeClass("form-data-error");
    $("#invalid-entry-message").addClass("hide-element");

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
	if(!validateRestaurantName($("#name")[0])) {
		isValid = false;
	}
    return isValid;
}

$(document).ready(function () {
    $("#settings").addClass('active');
});