$(document).ready(function(){
    // Menu settings
    // $('#menuToggle, .menu-close').on('click', function(){
    //     $('#menuToggle').toggleClass('active');
    //     $('body').toggleClass('body-push-toleft');
    //     $('#theMenu').toggleClass('menu-open');
    // });
});


$(window).scroll(function(e){
  parallax();
});

function parallax(){
  var scrolled = $(window).scrollTop();
  $('#headerwrap').css('top',-(scrolled*0.2)+'px');
}

var win_height = 0;

$(window).load(function(){
  win_height = $(window).height();
  $('#e').css('margin-top', win_height);
});

$(window).resize(function(){
  if(win_height != $(window).height()) {
    win_height = $(window).height();
    $('#e').css('margin-top', win_height);
  }
});


$(".timeline-panel").on("click", function(e){
    e.preventDefault();
    $("#modal").modal({
        show: true,
        keyboard: true,
        backdrop: true
    });
});


function UpdateTableHeaders() {
   $(".persist-area").each(function() {

       var el             = $(this),
           offset         = el.offset(),
           scrollTop      = $(window).scrollTop(),
           floatingHeader = $(".floatingHeader", this)

       if ((scrollTop > offset.top) && (scrollTop < offset.top + el.height())) {
           floatingHeader.css({
            "visibility": "visible"
           });
       } else {
           floatingHeader.css({
            "visibility": "hidden"
           });
       };
   });
}

// DOM Ready
$(function() {

   var clonedHeaderRow;

   $(".persist-area").each(function() {
       clonedHeaderRow = $(".persist-header", this);
       clonedHeaderRow
         .before(clonedHeaderRow.clone())
         .css("width", clonedHeaderRow.width())
         .addClass("floatingHeader");

   });

   $(window)
    .scroll(UpdateTableHeaders)
    .trigger("scroll");

});
