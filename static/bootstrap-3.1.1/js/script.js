$(document).ready(function() {


	var bindex;
	var page = getCurrentFileName()

	switch(page) {
		case "" : 		  bindex = 1; break;
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
		$(active_element).attr('id', 'active');
	}

	// navbar animation
	$('.masthead ul li').mouseenter(function() {
		$( this ).addClass( 'active' );	
	});

	$('.masthead ul li').mouseleave(function() {

		if(this.hasAttribute('id')) return;

		$( this ).removeClass( 'active' );	
	});

	function getCurrentFileName() {
	    var pagePathName= window.location.pathname;
	    return pagePathName.substring(pagePathName.indexOf("/") + 1);
	}
});