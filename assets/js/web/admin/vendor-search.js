function vendor(id, name, neighborhoods, category){
    var self = this;
    self.id = id;
    self.name = name;
    self.neighborhoods = neighborhoods;
    self.category = category;
    self.displayName = ko.computed(function(){
        var name = self.category + " : " + self.name;
        for (var index in self.neighborhoods){
            if (index == 0 && self.neighborhoods[index] != ''){
                name = name + " in ";
            }
            name = name + self.neighborhoods[index] + ",";
        }
        return name;
    }, self);
    self.registerVendorUrl = ko.computed(function() {
        return "/admin/vendors/" + self.id + "/register"
    }, self);
}

var vendorsViewModel = {
    errors: ko.observable(),
    vendors : ko.observableArray()
};

var neighborhoodsViewModel = {
    neighborhoods : ko.observableArray()
};

function loadVendorsData(){
    var vendorSearchString = document.getElementById("vendor-search-text").value;
    var url = '/api/vendors/admin_search?q=' + vendorSearchString;
    $.ajax({
        url: url,
        success: populateVendorData
    })
}

function loadNeighborhoodData(){
    var url = '/api/neighborhoods';
    $.ajax({
        url: url,
        success: populateNeighborhoodData
    })
}

function populateNeighborhoodData(data){
        neighborhoodsViewModel.neighborhoods.removeAll();
        for (var index in data){
            neighborhoodsViewModel.neighborhoods.push(data[index]);
        }
}

function populateVendorData(data){
    if (data.errors.length == 0){
        vendorsViewModel.errors("");
        vendorsViewModel.vendors.removeAll();
        for (index in data.data){
            var vendorObject = data.data[index].vendor;
            vendorsViewModel.vendors.push(new vendor(vendorObject.id, vendorObject.name,
                                                     vendorObject.neighborhoods, vendorObject.category));
        }
        $("#results").removeClass("hide-element");
    }else{
        vendorsViewModel.vendors.removeAll();
        vendorsViewModel.errors(data.errors);
    }
}

function showNeighborhood(){
    var neighborhood = document.getElementById("neighborhood-picker").value;
    window.location.href ="/show_neighborhood?neighborhood=" + neighborhood;
}

$(document).ready(function(){
    ko.applyBindings(vendorsViewModel, document.getElementById("results"));
    ko.applyBindings(neighborhoodsViewModel, document.getElementById("neighborhood-search"));
    loadNeighborhoodData();
})