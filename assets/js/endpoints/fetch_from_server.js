$(document).ready(function(){
	$("#try-it").click(function(){
		$('#response').load('/fetch_from_server', {'endpoint': 'aggregate_campaigns', 'property': 'average_discounts', 'lat': 40.745619, 'lon': -73.985296, 'radius': 3000});
	});
});