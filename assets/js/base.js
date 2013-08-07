function negotiate_deal(slider_id, hidden_field_id, business_name)
{
	proposed_deal = $('#' + slider_id).val()
	initial_deal = $('#' + hidden_field_id).val();
	$.getJSON('/haggle', 
		  {'proposed_deal' : proposed_deal,
		   'initial_deal' : initial_deal,
		   'business_name' : business_name}
		   , function(data) {
		   is_accepted = false;
		   requested_discount = 0;
		   accepted_discount = 0;
		   $.each(data, function(key, val) {
			if(key == "accepted")
				is_accepted = val;			
			else if(key == "acceptedDiscount")
				accepted_discount = val;
			});
			$('#' + slider_id).val(accepted_discount);
			$('#' + slider_id).slider('refresh');
			$('#' + hidden_field_id).val(accepted_discount);			
	});
}

function negotiate_random_deal(slider_id, hidden_field_id, business_name, fieldset_id)
{
	proposed_deal = $('#' + slider_id).val()
	initial_deal = $('#' + hidden_field_id).val();
	$.getJSON('/haggle', 
		  {'proposed_deal' : proposed_deal,
		   'initial_deal' : initial_deal}
		   , function(data) {
		   is_accepted = false;
		   $.each(data, function(key, val) {
			if(key == "accepted")
				is_accepted = val;			
			});
			if(is_accepted) {
				$.mobile.changePage("/accepted_deal", null, true, true, {allowSamePageTransition : true});
				$('#' + slider_id).val(proposed_deal);
				$('#' + slider_id).slider('refresh');				
				$('#' + fieldset_id).removeClass("highlight_red")
				$('#' + fieldset_id).addClass("highlight_green")
			}
			else {
				$.mobile.changePage("/rejected_deal", null, true, true, {allowSamePageTransition : true});
				$('#' + slider_id).val(initial_deal);
				$('#' + slider_id).slider('refresh');
				$('#' + fieldset_id).removeClass("highlight_green")
				$('#' + fieldset_id).addClass("highlight_red")
			}
	});
}

function remove_all_highlights(element) {
	element.removeClass('highlight_green');
	element.removeClass('highlight_red');
	element.removeClass('highlight_yellow');
}

function find_display_text(name_span) {
	var inner_span = name_span.find('.ui-btn-text');
	var display_text = inner_span.children().remove().end().text(); 
	return display_text;
}

function update_text(name_span, initial_deal, proposed_deal) {		
	var display_text = find_display_text(name_span); 
	var tokens = display_text.split(':');
	var establishment_name = $.trim(tokens[0]);
	display_text = establishment_name + " : " + initial_deal + "% - " + proposed_deal + "%";
	name_span.find('.ui-btn-text').html(display_text);
}

function negotiate_dummy_deal(memcache_key) {
	$('div[data-role="collapsible"]').each(function(index){
		var curr_fieldset = $(this);		
		var slider_selector = 'input[data-type="range"]';
		var proposed_deal = curr_fieldset.find(slider_selector).val();
		var initial_deal = curr_fieldset.find('input[type="hidden"]').val();

		if(proposed_deal != initial_deal || name_span.hasClass('highlight_yellow')) {
			//User has changed the value
			remove_all_highlights(curr_fieldset);
			remove_all_highlights(name_span);
			curr_fieldset.find(slider_selector).slider('disable');
			curr_fieldset.unbind('expand');
			
			var id_attr = curr_fieldset.attr('id');
			var id_str = id_attr.substring(0, (id_attr.length - 9));
			name_span = curr_fieldset.find('h3>a>span');
			
			$.getJSON(
			'/negotiate', 
			{
				'initial_deal' : initial_deal,
				'requested_deal' : proposed_deal,
				'vendor_4s_id' : id_str,
				'memcache_key' : memcache_key
			}, 
			function(data) {				
				update_text(name_span, initial_deal, data.acceptedDiscount);
				if(data.accepted == 1){
					curr_fieldset.addClass('highlight_green');
					name_span.addClass('highlight_green')
				}
				else {
					curr_fieldset.addClass('highlight_red');
					name_span.addClass('highlight_red')
				}
			});			
		}
	});
}

function show_dialog(memcache_key) {
	var selected_deals = '';
	$('div[data-role="collapsible"]').each(function(index){		
		var curr_fieldset = $(this);		
		var name_span = curr_fieldset.find('h3>a>span');
		if(name_span.hasClass('highlight_orange')) {
			id_attr = curr_fieldset.attr('id');
			id_str = id_attr.substring(0, (id_attr.length - 9));
			selected_deals += id_str + "~" + find_display_text(name_span) + '|';
		}
	});
	var uri = "/accepted_deal?deals=" + encodeURIComponent(selected_deals) + "&memcache_key=" + encodeURIComponent(memcache_key);
	$.mobile.changePage(uri, null, true, true, {allowSamePageTransition : true});
}

function expand_grid(direction) {
	$.getJSON(
		'/expand_grid', 
		{
			'cell' : $('#input_cell > input').val(),
			'direction' : direction
		}, 
		function(data) {
			for(var i = 0; i < data.grid_to_append.length; i++) {
				var cell = data.grid_to_append[i];
				var bounding_box_coords = [
					new google.maps.LatLng(cell._ne.lat, cell._ne.lon),
					new google.maps.LatLng(cell._se.lat, cell._se.lon),
					new google.maps.LatLng(cell._sw.lat, cell._sw.lon),
					new google.maps.LatLng(cell._nw.lat, cell._nw.lon)
				];
				bounding_box = new google.maps.Polygon({
					paths: bounding_box_coords
				});
				bounding_box.setMap(map);
				var midPointLatLng = new google.maps.LatLng(cell.mid_point.lat, cell.mid_point.lon)
				var midPointMarker = new google.maps.Marker({
					position: midPointLatLng,
					title: cell.seed_cell
				});
				globallist.push(cell.seed_cell)
				midPointMarker.setMap(map);
			}	
		});
}
