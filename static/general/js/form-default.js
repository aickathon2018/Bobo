/*Author: Lim Wei Sean*/

$('input').keypress(function (e) {
    var key = e.which;
    if(key == 13)  // the enter key code
     {
       $('#submit').click();
       return false;
     }
}); 