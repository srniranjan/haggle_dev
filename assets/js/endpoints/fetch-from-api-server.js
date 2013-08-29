$('#params').submit(function(){
	$.ajax({
		type: "POST",
		url: "/fetch_from_api_server",
		data: $("#params").serialize(),
		success: function(data){
			var pretty_data = JSON.stringify(JSON.parse(data), undefined, 4);
			$('#response').html(pretty_data);
		}
	});
	return false;
});