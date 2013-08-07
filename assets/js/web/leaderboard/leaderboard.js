function loadTableNext() {
	loadTable(parseInt($('#page_number').val()) + 1);
}

function loadTable(page_number) {
    var haggler_emails_string = $('#haggler_emails').val();
	var haggler_emails = haggler_emails_string.split(',');
    var vendor_doc_ids_string = $('#vendor_doc_ids').val();
    var vendor_doc_ids = vendor_doc_ids_string.split(',');
    var batch_size = 20
	var max_page = Math.ceil(haggler_emails.length / batch_size);
    if (page_number > max_page || page_number < 1) {
		return;
	}
    start_offset = (page_number - 1) * batch_size;
	if (parseInt($('#start_offset').val()) != start_offset) {
		return;
	}
    end_offset = batch_size * page_number;
	$('#page_number').val(page_number);
	batched_emails = haggler_emails.slice(start_offset, end_offset);
    var posting = $.post('/showcase/leaderboard', {'batched_emails' : batched_emails.join(),'vendor_doc_ids' : vendor_doc_ids.join(),'start_offset' : start_offset});
	$('#loading_message').css('visibility','visible');
	posting.always(function(){
		$('#loading_message').css('visibility','hidden');
	});
	posting.done(function(data){
		var content = data.content;
		var serial = data.serial;
		$('#leaderboard_serial').append( serial );
		$('#leaderboard_table').append( content );
		$('#start_offset').val(end_offset);
		loadData();
	});
	posting.fail(function(){
		$('#loading_error').css('visibility','visible');
		$('#load_more').remove();
	});
}

$(document).ready(function() {
	loadData();
});

$(document).ready(function() {
	$(window).scroll(function() {
		loadData();
	});
});

function loadData() {
	var bottom_of_window = $(window).scrollTop() + $(window).height();
	var load_more_top = $('#load_more').offset().top;
	var load_more_pos = bottom_of_window + ($(window).height() * 0.01);
	if(load_more_top < load_more_pos) {
		loadTableNext();
	}
}

$(document).ready(function() {
	$("#leaderboard th").on("click", function(event) {
		$("#leaderboard th").click(function() {
			return false;
		});
		$("#leaderboard th").disabled = true;
		var currTarget = $(event.currentTarget);
		window.location.assign('/showcase/leaderboard?vendor_doc_id='+currTarget.find('input').val()+'&current_ordering='+$('#current_ordering').val());
	});
});

$(document).ready(function() {
	$("#leaderboard th").dblclick(function() {
		return false;
	});
});