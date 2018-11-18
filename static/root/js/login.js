$('input').keypress(function (e) {
    var key = e.which;
    if(key == 13)  // the enter key code
     {
       $('#submit_button').click();
       return false;  
     }
}); 

document.addEventListener('contextmenu', event => event.preventDefault());