$(document).ready(function(){
	$("#try-it").click(function(){
		$.get('/fetch_from_server', { endpoint: 'aggregate_campaigns', property: 'average_discounts', lat: 40.745619, lon: -73.985296, radius: 3000}, function(data){
			var pretty_data = JSON.stringify(JSON.parse(data), undefined, 4);
			$('#response').html(pretty_data);
		});
	});
});