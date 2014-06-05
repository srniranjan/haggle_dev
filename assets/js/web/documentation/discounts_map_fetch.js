function injectMap(data){
  	var heatmap = new HeatmapOverlay(map, {
		"radius":20,
		"visible":true,
		"opacity":60
	}); 
	var testData={
		max: 46,
		data: data,
	};
	heatmap.setDataSet(testData);
	/*
	google.maps.event.addListenerOnce(map, "idle", function(){
		heatmap.setDataSet(testData);
	});
*/
};

$('#params').submit(function(){
	$.ajax({
		type: "POST",
		url: "/fetch_from_api_server",
		data: {"endpoint": endpoint, "data": $("#params").serialize(), "token": $("#token").val()},
		beforeSend: function(){
			$('#loading_indicator').show();
		},
		success: function(data){
			console.log(JSON.parse(data));

			$('#loading_indicator').hide();
			//injectMap(JSON.parse(data));
		}
	});
	return false;
});