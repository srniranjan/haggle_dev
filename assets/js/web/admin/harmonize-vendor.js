var map = null;
var mapMarkers = [];

function loadVendors(){
    var vendorId = $("#vendor-id").val();
    var vendorName = $("#vendor-name").text();
    var vendorSearch = $("#vendor-search-field").val();
    var vendorLat = $("#vendor-lat").val();
    var vendorLon = $("#vendor-lon").val();
    var vendorCategory = $("#vendor-category").val();
    harmonizeVendorsViewModel.vendor(new vendorModel(vendorId, vendorLat, vendorLon, vendorName, vendorCategory));
    var url = '/api/vendors/admin_search?q=' + vendorSearch + '&lat=' + vendorLat + '&lon=' + vendorLon;
    $.ajax({
        url:url,
        success: populateVendorsModel
           });
}

function populateVendorsModel(data) {
    var similarVendors = data.data;
    //Drop All Markers from map
    for(var markerIndex in mapMarkers){
        mapMarkers[markerIndex].setMap(null);
    }
    mapMarkers = [];
    harmonizeVendorsViewModel.similarVendors.removeAll();
    harmonizeVendorsViewModel.harmonizedVendors.removeAll();
    for (var index in similarVendors) {
        var vendorObject = data.data[index].vendor;
        var tpVendors = data.data[index].tp_vendors;
        var tpVendorsArray;
        if (vendorObject.id != harmonizeVendorsViewModel.vendor().id) {
            var vendor = new vendorModel(vendorObject.id,
                vendorObject.lat,
                vendorObject.lon,
                vendorObject.name,
                vendorObject.category);
            tpVendorsArray = vendor.thirdPartyVendors;
            harmonizeVendorsViewModel.similarVendors.push(vendor);
            addMarker(vendor);
        }
        else {
            tpVendorsArray = harmonizeVendorsViewModel.thirdPartyVendors;
        }
        tpVendorsArray.removeAll();
        for (var index in tpVendors) {
            var tpVendor = tpVendors[index];
            tpVendorsArray.push(new tpVendorModel(tpVendor.id, tpVendor.name, tpVendor.network));
        }
    }
}

function harmonizeVendors(){
    var harmonizeIds = [];
    var vendors = harmonizeVendorsViewModel.harmonizedVendors()
    for (var index in vendors){
        harmonizeIds.push(vendors[index].id);
    }
    var url = '/api/vendors/' + harmonizeVendorsViewModel.vendor().id + '/harmonize';
    var harmonizeIdsString = harmonizeIds.toString();
    $.ajax({
        url:url,
        data: { harmonizeids: harmonizeIdsString, deharmonizeids: harmonizeVendorsViewModel.deharmonizeVendors.toString()},
        type: "POST",
        success: harmonizeSuccessful
    });
}

function harmonizeSuccessful(){
    $("#request-submitted").removeClass("hide-element");
    $("#submit-button").attr("disabled", "disabled");
}

var harmonizeVendorsViewModel = {
    vendor : ko.observable(),
    thirdPartyVendors : ko.observableArray(),
    harmonizedVendors : ko.observableArray(),
    similarVendors : ko.observableArray(),
    deharmonizeVendors : []

}

function vendorModel(id, lat, lon, name, category){
    var self = this;
    self.id = id;
    self.lat = lat;
    self.lon = lon;
    self.name = name;
    self.category = category;
    self.thirdPartyVendors = ko.observableArray();
}

function tpVendorModel(id, name, network){
    var self = this;
    self.id = id;
    self.name = name;
    self.network = network;
    self.key = ko.computed(function(){
       return self.network + "|" + self.id;
    });
    self.harmonized = true;
    self.displayName = ko.computed(function(){
       return self.network + " : " + self.name;
    });
    self.url = ko.computed(function(){
        if(self.network == "4S"){
            return "//foursquare.com/venue/" + self.id;
        }else if(self.network == "FB"){
            return "//facebook.com/" + self.id;
        }
        return "#";
    });
}

function unharmonizeThirdPartyVendor (target) {
    if (!target.checked) {
        harmonizeVendorsViewModel.deharmonizeVendors.push(target.id);
    } else {
        harmonizeVendorsViewModel.deharmonizeVendors.splice(
            harmonizeVendorsViewModel.deharmonizeVendors.indexOf(target.id), 1);
    }
}

function initializeMap(){
    var seedLatLng = new google.maps.LatLng( harmonizeVendorsViewModel.vendor().lat ,
                                             harmonizeVendorsViewModel.vendor().lon )
    var myOptions = {
        center: seedLatLng,
        zoom: 15,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
    var marker = new google.maps.Marker({position: seedLatLng,
                                            title:"Primary: " + harmonizeVendorsViewModel.vendor().name});
    marker.setMap(map);
}

function addMarker(vendor){
    var vendorLatLng = new google.maps.LatLng( vendor.lat , vendor.lon );

    var marker = new google.maps.Marker({position: vendorLatLng,
                                         title:vendor.name,
                                         id: vendor.id});
    addMarkerClickEvent(marker, vendor)
    marker.setMap(map);
    mapMarkers.push(marker);
}

function addMarkerClickEvent(marker, vendor){
    google.maps.event.addListener(marker, 'click', function() {
        if (findHarmonizedVendor(vendor.id) == null){
            harmonizeVendorsViewModel.harmonizedVendors.push(vendor);
        }
        removeSimilarVendor(vendor.id);
        marker.setMap(null);
    });
}

function findHarmonizedVendor(id){
    return ko.utils.arrayFirst(harmonizeVendorsViewModel.harmonizedVendors(), function(vendor) {
        return vendor.id == id;
    });
}

function removeHarmonizedVendor(id){
    vendor = ko.utils.arrayFirst(harmonizeVendorsViewModel.harmonizedVendors(), function (item) {
        return id === item.id;
    });
    for (var index in vendor.thirdPartyVendors()){
        harmonizeVendorsViewModel.deharmonizeVendors.splice(
            harmonizeVendorsViewModel.deharmonizeVendors.indexOf(vendor.thirdPartyVendors()[index].key), 1);
    }
    harmonizeVendorsViewModel.harmonizedVendors.remove(vendor);
}

function removeSimilarVendor(id){
    harmonizeVendorsViewModel.similarVendors.remove(function(item) { return item.id == id });
}

function unharmonizeVendor(event){
    var vendor = findHarmonizedVendor(event.id);
    addMarker(vendor);
    removeHarmonizedVendor(vendor.id);
    harmonizeVendorsViewModel.similarVendors.push(vendor);
}

$(document).ready(function(){
    ko.applyBindings(harmonizeVendorsViewModel, document.getElementById("harmonize-vendor"));
    loadVendors();
})

$(window).load(function(){
    initializeMap();
})
