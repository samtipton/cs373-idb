$(document).ready(function() {


	var bindex;
	var page = getCurentFileName()

	switch(page) {
		case "games/" :   bindex = 2; break;
		case "teams/" :   bindex = 3; break;
		case "players/" : bindex = 4; break;
		case "contact/" : bindex = 5; break;
		default : break;
	}

	// activate correct nav button
	if (bindex != null) {
		var active_element = '.masthead ul li:nth-child(' + bindex.toString() + ')';
		$(active_element).addClass('active');
	}

	// navbar animation
	$('.masthead ul li').mouseenter(function() {
		$( this ).addClass( 'active' );
	});
	$('.masthead ul li').mouseleave(function() {
		$( this ).removeClass( 'active' );
	});

	function getCurentFileName() {
	    var pagePathName= window.location.pathname;
	    return pagePathName.substring(pagePathName.indexOf("/") + 1);
	}
});