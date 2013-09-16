$('#fetch_token').click(function(){
	console.log('login');
		$.ajax({
			type: "GET",
			url: "/fetch_token",
			success: function(data){
				console.log(data);
			}
		});
		return false;
});
