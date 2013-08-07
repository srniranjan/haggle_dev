function scoreData(scoreType, deals, dealsDelta){
    var self = this;
    self.scoreType = scoreType;
    self.deals = deals;
    self.dealsDelta = dealsDelta;
    self.dealsDeltaText = ko.computed(function(){
        if (self.dealsDelta >=0){return "+" + self.dealsDelta;}
        else{return self.dealsDelta}
    });
    self.deltaCss = ko.computed(function(){
        var cssClass = "badge deals-delta-text";
        if(self.dealsDelta >= 0){cssClass += " badge-success";}
        else if(self.dealsDelta < 0){cssClass += " badge-important";}
        return cssClass;
    });
}

var campaignReportViewModel = {
    dealsInterested : ko.observable(),
    dealsAvailed : ko.observable(),
    scores: ko.observableArray(),
    fromDate : ko.observable(),
    toDate : ko.observable(),
    maxDate : ko.observable()
};

function loadCampaignReportData(){
    var vendorId = document.getElementById("vendor-id").value;
    var campaignReportURL = "../../api/vendors/" + vendorId + "/report";
    var fromDate = $("#from_date").val();
    var toDate = $("#to_date").val();


    var to = hg.dt.endOfDay(toDate ? hg.dt.parse(toDate) : hg.dt.now());
    var from = hg.dt.startOfDay(
		fromDate ? hg.dt.parse(fromDate) : hg.dt.add_days(to, -7));

   $.ajax({
       url:campaignReportURL ,
       data:{from_date:hg.dt.toTimestamp(from), to_date:hg.dt.toTimestamp(to)},
       success:populateCampaignReportData
    });
}

function setupDatePickers() {
    var fromDate = new Date(campaignReportViewModel.fromDate());
    var toDate = new Date(campaignReportViewModel.toDate());
    var maxDate = new Date(campaignReportViewModel.maxDate());
    var fromDatePicker = $("#dp1").datepicker();
    var toDatePicker = $("#dp2").datepicker();
    fromDatePicker.unbind('changeDate');
    fromDatePicker.on('changeDate', function (ev) {
            if(ev.date.valueOf() > maxDate.valueOf()){
                $("#alert").find('span').text('The from date can not be in the future');
                $("#alert").removeClass("hide-element");
            }
            else if (ev.date.valueOf() > toDate.valueOf()) {
                $("#alert").find('span').text('The from date can not be greater than the to date');
                $("#alert").removeClass("hide-element");
            } else {
                $('#alert').addClass("hide-element");
                fromDate = new Date(ev.date);
                $('#startDate').text($('#dp4').data('date'));
                $('#dp1').datepicker('hide');
                loadCampaignReportData();
            }
        });
    toDatePicker.unbind('changeDate');
    toDatePicker.on('changeDate', function (ev) {
            if (ev.date.valueOf() > maxDate.valueOf()) {
                $("#alert").find('span').text('The to date can not be in the future');
                $("#alert").removeClass("hide-element");
            }
            else if (ev.date.valueOf() < fromDate.valueOf()) {
                $('#alert').find('strong').text('The to date can not be less than the from date');
                $("#alert").removeClass("hide-element");
            } else {
                $('#alert').addClass("hide-element");
                toDate = new Date(ev.date);
                $('#endDate').text($('#dp5').data('date'));
                $('#dp2').datepicker('hide');
                loadCampaignReportData();
            }
        });
}

function populateCampaignReportData(data){
    if(data != ""){
        var reportData = $.parseJSON(data);
        campaignReportViewModel.fromDate(reportData.from_date);
        campaignReportViewModel.toDate(reportData.to_date);
        campaignReportViewModel.maxDate(reportData.today);
        setupDatePickers();
        campaignReportViewModel.dealsAvailed(reportData.deals.availed);
        campaignReportViewModel.dealsInterested(reportData.deals.interested);
        campaignReportViewModel.scores.removeAll();
        campaignReportViewModel.scores.push(new scoreData(reportData.deals.one.scoreType,
                                                          reportData.deals.one.count,
                                                          reportData.deals.one.change));
        campaignReportViewModel.scores.push(new scoreData(reportData.deals.two.scoreType,
                                                   reportData.deals.two.count,
                                                   reportData.deals.two.change));
        campaignReportViewModel.scores.push(new scoreData(reportData.deals.three.scoreType,
                                                          reportData.deals.three.count,
                                                          reportData.deals.three.change));
        campaignReportViewModel.scores.push(new scoreData(reportData.deals.four.scoreType,
                                                          reportData.deals.four.count,
                                                          reportData.deals.four.change));
    }
}
