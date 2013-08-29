function renderEndpoint(endpoint){
	$.get('/endpoints/render', {'endpoint': endpoint});
};