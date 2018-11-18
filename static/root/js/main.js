jQuery(document).ready(function ($) { 
    /********************************************
    Slider styling code 
    Author: zuraiz
    Source: https://codepen.io/zuraizm/pen/vGDHl/
    *********************************************/
    setInterval(function () {
        moveRight();
    }, 3000);

    var slideCount = $('#slider ul li').length;
    var slideWidth = $('#slider ul li').width();
    var slideHeight = $('#slider ul li').height();
    var sliderUlWidth = slideCount * slideWidth;
    
    $('#slider').css({ width: slideWidth, height: slideHeight });
    
    $('#slider ul').css({ width: sliderUlWidth, marginLeft: - slideWidth });
    
    $('#slider ul li:last-child').prependTo('#slider ul');

    function moveLeft() {
        $('#slider ul').animate({
            left: + slideWidth
        }, 200, function () {
            $('#slider ul li:last-child').prependTo('#slider ul');
            $('#slider ul').css('left', '');
        });
    };

    function moveRight() {
        $('#slider ul').animate({
            left: - slideWidth
        }, 200, function () {
            $('#slider ul li:first-child').appendTo('#slider ul');
            $('#slider ul').css('left', '');
        });
    };

    $('a.control_prev').click(function () {
        moveLeft();
    });

    $('a.control_next').click(function () {
        moveRight();
    });

/*************************************************************************************************************/

    function menuToggle(){
        if($('#nav-item').hasClass("on")){
            $('#nav-item').addClass("off");
            $('#nav-item').removeClass("on");
        }else{
            $('#nav-item').addClass("on");
            $('#nav-item').removeClass("off");
        }
    };

    $('#nav').click(function(){
        menuToggle();
    })
  }); 