;(function(){

	// Menu settings
	$('#menuToggle, .menu-close').on('click', function(){
		$('#menuToggle').toggleClass('active');
		$('body').toggleClass('body-push-toleft');
		$('#theMenu').toggleClass('menu-open');
	});

})(jQuery)


$(window).scroll(function(e){
  parallax();
});

function parallax(){
  var scrolled = $(window).scrollTop();
  $('#headerwrap').css('top',-(scrolled*0.175)+'px');
}

var win_width = 0;

$(window).load(function(){
  win_width = $(window).width();
  $('#e').css('margin-top', win_width);
});

$(window).resize(function(){
  if(win_width != $(window).width()) {
    win_width = $(window).width();
    $('#e').css('margin-top', win_width);
  }
});