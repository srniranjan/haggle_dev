$('#params-submit').click(function(){
    var fetch_url = $('#url').val();
    var method = "POST";
    if( fetch_url == 'local') {
        fetch_url = endpoint;
        method = "GET";
    } else {
        fetch_url = "/fetch_from_api_server";
    }
	$.ajax({
		type: method,
		url: fetch_url,
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