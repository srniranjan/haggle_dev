$('#params-submit').click(function(){
	$.ajax({
		type: "POST",
		url: "/fetch_from_api_server",
		data: {"endpoint": endpoint, "data": $("#params").serialize(), "token": $("#token").val()},
		beforeSend: function(){
		    $('#response').hide();
			$('#loading_indicator').show();
		},
		success: function(data){
			var pretty_data = JSON.stringify(JSON.parse(data), undefined, 4);
			$('#response').html(pretty_data);
			$('#loading_indicator').hide();
			$('#response').show();
		}
	});
	return false;
});