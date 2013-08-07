function Vendor(id, name){
    var self = this;
    self.id = id;
    self.name = name;
    self.vendorUrl = ko.computed(function() {
        return "/vendors/" + self.id;
    }, self);
}

var vendorsViewModel = {
    vendors : ko.observableArray()
};

function loadVendorsData(){
    var userId = document.getElementById("user-id").value;
    var url = '/api/users/' + userId + "/vendors";
    $.ajax({
        url: url,
        success: populateVendorData
    })
}

function populateVendorData(data){
    if (data.length == 0){
       $("#no-vendors-text").removeClass('hide-element');
    }
    else{
        $("#no-vendors-text").addClass('hide-element');
        if(data.length ==1){
            var vendorObject = new Vendor(data[0].id,data[0].name);
            window.location.href = "/vendors/" + vendorObject.id ;
        }else{
            vendorsViewModel.vendors.removeAll();
            for (var index in data){
                vendorsViewModel.vendors.push(new Vendor(data[index].id,data[index].name));
            }
        }
    }
}

$(document).ready(function(){
    ko.applyBindings(vendorsViewModel, document.getElementById("results"));
    loadVendorsData();
})