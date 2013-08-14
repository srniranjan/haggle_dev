/*
$(document).ready(function() {
	$(window).scroll( function(){
		var top_of_window = $(window).scrollTop();
		var bottom_of_window = top_of_window + $(window).height();
		var near_top_of_window = top_of_window + ($(window).height() * 0.075);
		var max_permissible = $('#page1_haggle_logo').offset().top; //+ $('#page1_haggle_logo').height() - $('#navbar-fluid').height();
		if(top_of_window > max_permissible)
			$('#navbar-fluid').show();
		else
			$('#navbar-fluid').hide();

		var business_top = $('#business').offset().top;
		if(business_top > top_of_window && business_top < bottom_of_window) {
			if(near_top_of_window > business_top) {
				highlightNavbarLink($("#business-link"));
				if(window.scroll_past_sent!='true') {
					ga('send', 'event', 'scrolled-past-human-to-business', 'scroll', 'Human Business Transition');
					window.scroll_past_sent = 'true';
				}
			} else {
				highlightNavbarLink($("#human-link"));
			}
		}
	});
});
*/
$(document).ready(function() {
	var url = document.URL;
	var accessed_page = url.substring(url.lastIndexOf('/'));
	$("#c820 a").each(function() {
		var current_link = this.href.substring(this.href.lastIndexOf('/'));
		if(accessed_page===current_link) {
			this.style.color="#e58170";
			return false;
		}
	});
});

$(document).ready(function() {
	$("#c820 a").on("click", function(event) {
		highlightNavbarLink($(event.currentTarget));
	});
});



function highlightNavbarLink(selectedLink) {
	$("#c820 a").each(function() {
		this.style.color="#ffffff";
	});
	selectedLink.css("color","#e58170");
}

$('navbar').on('touchstart', function(e) {
  e.stopPropagation();
});



function show(selectedLink) {
	$('.q').hide();
	$('.'+selectedLink).show();
	if(parseInt($('.'+selectedLink).css('height'))>798)
	{
		$('#documentation-sidebar')[0].style.height=$('.'+selectedLink).css('height');
	}
	else
	{
		$('#documentation-sidebar')[0].style.height="798px";
	}
	return false;
	}