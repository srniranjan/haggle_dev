$(document).ready(function(){
    ko.applyBindings(dealsViewModel, document.getElementById("patron-activity"));
    loadDealsData();
    if(document.getElementById("campaign-report")){
        ko.applyBindings(campaignReportViewModel, document.getElementById("campaign-report"));
        loadCampaignReportData();
    }
    $("#home").addClass('active');
    setTabNavBasedOnSize();

    setTimeout(loadDealsData, 300000);

    if (window.location.hash == "") {
        gotoHashTab("#dashboard");
    }
    else {
        gotoHashTab(window.location.hash);
    }
});

$(window).resize(function(){
    setTabNavBasedOnSize();
});

function setTabNavBasedOnSize() {
    var isDesktop = $(".visible-desktop").is(':visible');
    var tabNavigation = $(".tabbable");
    var tabNavigationTabs = tabNavigation.find("ul");

    if(isDesktop){
        tabNavigation.removeClass("tabs-top");
        tabNavigationTabs.removeClass("vendor-tabs-tablet-phone");
        tabNavigation.addClass("tabs-left");
    }else{
        tabNavigation.addClass("tabs-top");
        tabNavigationTabs.addClass("vendor-tabs-tablet-phone");
        tabNavigation.removeClass("tabs-left");
    }
}

var gotoHashTab = function (customHash) {
    var hash = customHash || location.hash;
    var hashPieces = hash.split('?');
    $('.tab-pane').removeClass('active');
    $('.nav > li').removeClass('active');
    $(hashPieces[0]).addClass('active');
    $('[href=' + hashPieces[0] + ']').parent().addClass('active')
};

// when the nav item is selected update the page hash
$('.nav a').on('shown', function (e) {
    window.location.hash = e.target.hash;
});