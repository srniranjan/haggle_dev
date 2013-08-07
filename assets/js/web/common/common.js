function validateRestaurantName(e) {
	if(($.trim(e.value)).length >16) {
		if(!confirm('Optimal Restaurant Name length is 16 characters. Continue without changing?')) {
			e.focus();
			return false;
		}
	}
	return true;
}