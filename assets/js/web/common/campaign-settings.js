haggle = (typeof haggle === "undefined")? {} : (haggle || {});

haggle.Campaign = function(){
    function init(options){
            options = options || {};
            $("#campaign-form").submit(function(event){
                event.preventDefault();
                if(validateDiscount() && validateBusyHours()){
                    $("#preference").val(savePreferences());
                    var form = $(this);
                    $.ajax({url: form.attr("action"), data: form.serialize(), type: "POST"}).
                success(function(){
                    if(options.success){
                        options.success();
                    }
                }).
            error(function(){$("#error").removeClass('hide-element')});
                };
            });
    };
    return init;
}();

function loadCampaignSettings(){
    var campaignId =  $("#campaign-id").val();
    if (campaignId != ''){
        var url = '/api/campaigns/' + campaignId;
        $.ajax({
            url: url,
            success: populateCampaignData
        });
    }
    else{
        $('#campaignSettingsModal').modal('hide');
    }
}

function populateCampaignData(data){
    $("#min_discount").val(data.min_discount);
    $("#max_discount").val(data.max_discount);
    validateDiscount();

    $("#busy_occupancy").val(data.busy_occupancy);
    $("#free_occupancy").val(data.free_occupancy);

    $("#weekday_busy_hours").val(data.weekday_busy_hours);
    $("#weekend_busy_hours").val(data.weekend_busy_hours);
    populateBusyHours();

    setPreferences(data.preference);

    $('#campaignSettingsModal').modal('hide');
}

function setPreferences(preferencesOrder){
    $("#preferences").val(preferencesOrder);
    resetPreferences();
}

/**
 * @return {boolean}
 */
function validateDiscount(){
    var minDiscount = $("#min_discount"),
        maxDiscount = $("#max_discount"),
        discountArea = $("#discount-area");

    discountArea.removeClass("alert alert-block alert-error");

	if(!validateDiscountNumber(minDiscount[0]) || !validateDiscountNumber(maxDiscount[0]) || parseInt(minDiscount.val()) > parseInt(maxDiscount.val())) {
        discountArea.addClass("alert alert-block alert-error");
        return false;
	}
    return true;
}

function validateDiscountNumber(e){
	var invalidDiscountRegEx = /[^0-9]/;

	if(invalidDiscountRegEx.test(e.value)) {
        alert('No fractional values allowed for Min and Max Discounts');
		e.focus();
		return false;
	} else {
		var discountSlide = $('#'+e.name+'_slide');
		discountSlide.val(e.value);
	}
	return true;
}

function updateMinDiscount(e){
	var minDiscount = $('#min_discount');
	minDiscount.val(e.value);
}

function updateMaxDiscount(e){
	var maxDiscount = $('#max_discount');
	maxDiscount.val(e.value);
}

function validateBusyHours(){
    /*
       var timeRegex = "\s*,*\s*(([0-1]?[0-9]|[2][0-3]):(00|59))\s*-\s*(([0-1]?[0-9]|[2][0-3]):(00|59))";
       var weekdayHoursString = $("#weekday_busy_hours").val();
       var weekendHoursString = $("#weekend_busy_hours").val();
       var validWeekdayHours = weekdayHoursString.match(timeRegex) || weekdayHoursString == '';
       var validWeekendHours = weekendHoursString.match(timeRegex) || weekendHoursString == '';
       var busyPeriodArea = $("#busy-hours-area");
       var isValid = true;
       busyPeriodArea.removeClass("alert alert-block alert-error");

       if (!validWeekdayHours) {
       busyPeriodArea.addClass("alert alert-block alert-error");
       isValid = false;
       }
       if (!validWeekendHours) {
       busyPeriodArea.addClass("alert alert-block alert-error");
       isValid = false;
       }

       return isValid;
       */
    return true
}

function handleWeekdayBusyHoursCheckboxClick(target){
    var weekday_busy_hours = [];
    if ($("#weekday_busy_hours").val() != ""){
        weekday_busy_hours = $("#weekday_busy_hours").val().split(",");
    }

    if (target.checked){
        weekday_busy_hours.push(target.value);
    }else{
        weekday_busy_hours.splice(weekday_busy_hours.indexOf(target.value),1);
    }

    $("#weekday_busy_hours").val(weekday_busy_hours.join(","));
}

function handleWeekendBusyHoursCheckboxClick(target) {
    var weekend_busy_hours = [];
    if ($("#weekend_busy_hours").val() != ""){
        weekend_busy_hours = $("#weekend_busy_hours").val().split(",");
    }

    if (target.checked) {
        weekend_busy_hours.push(target.value);
    } else {
        weekend_busy_hours.splice(weekend_busy_hours.indexOf(target.value), 1);
    }
    $("#weekend_busy_hours").val(weekend_busy_hours.join(","));
}

function savePreferences(){
    var data = $("#score-priority-list").find("li").map(function () {
        return $(this).val();
    }).get();
    $("#preferences").val(data.join(""));
    return $("#preferences").val();
}

function swapScore(position1, position2){
    var position1Element = $("#"+position1);
    var position1ScoreValue = position1Element.find("span").text();
    var position1ScoreKey = position1Element.val();

    var position2Element = $("#"+position2);
    var position2ScoreValue = position2Element.find("span").text();
    var position2ScoreKey = position2Element.val();

    position1Element.find("span").text(position2ScoreValue);
    position1Element.val(position2ScoreKey);

    position2Element.find("span").text(position1ScoreValue);
    position2Element.val(position1ScoreKey);
}

function resetPreferences(){
    var order = $("#preferences").val().split("");
    var scorePriorityList = $("#score-priority-list");
    for(var i=0; i<=3; i++){
        var scorePosition = scorePriorityList.find("li[value=" + order[i] + "]")[0].id;
        if(scorePosition != i+1){
            swapScore(i+1, scorePosition);
        }
    }
}

