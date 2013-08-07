function deal(id, user, photo, discount, partySize, reservationAt, status){
    var self = this;
    self.id = id;
    self.user = user;
    self.discount = discount + "%";
    self.photo = photo;
    self.partySize = partySize;
    self.reservationAt = reservationAt + ' Reservation';
    self.status = status;
    self.cssClass = ko.computed(function(){
        var cssClassToReturn = "btn";
        if (self.status == "AVAILED"){
             cssClassToReturn += " hide-element";
        }
        else{
            cssClassToReturn += " btn-primary";
        }
        return cssClassToReturn;
    });
    self.HandleDealCheckInClick = function(){
        var vendorId = document.getElementById("vendor-id").value;
        if (!$("#"+self.id).hasClass("availed")){
            $.ajax({
                url : '/api/vendors/' + vendorId + "/deals/" + self.id + "/checkin",
                type: 'POST',
                success: function(){ var button = $("#"+self.id);
                    button.removeClass("btn-primary");
                    button.addClass("hide-element");
                }

            });
        }
    };
}

var dealsViewModel = {
    deals : ko.observableArray()
};

function loadDealsData(){
    var vendorId = document.getElementById("vendor-id").value;
    var url = '../../api/vendors/' + vendorId + '/deals';

    $.ajax({
        url: url,
        data: {from_date: hg.dt.toTimestamp(hg.dt.today()), to_date: hg.dt.toTimestamp(hg.dt.tommorow())},
        success: populateDealData
    });
}

function populateDealData(data){
    dealsViewModel.deals.removeAll();
    for (index in data){
        var dealObject = data[index];
        dealsViewModel.deals.push(new deal(dealObject.id, dealObject.user_name,
                                 dealObject.photo, dealObject.offered_disc,
                                 dealObject.party_size,
								 hg.dt.fromTimestamp(dealObject.redemption_datetime).toTimeString(),
                                 dealObject.status));
    }
}

