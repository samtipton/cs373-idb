$(document).ready(function() {

	// navbar animation
	$('.masthead ul li').mouseenter(function() {
		$( this ).addClass( 'active' );
	});
	$('.masthead ul li').mouseleave(function() {
		$( this ).removeClass( 'active' );
	});
});