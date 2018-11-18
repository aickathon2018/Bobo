/*$('input').keypress(function (e) {
    var key = e.which;
    if(key == 13)  // the enter key code
     {
       $('#submit_button').click();
       return false;  
     }
}); 

document.addEventListener('contextmenu', event => event.preventDefault());*/

// Grab elements, create settings, etc.
var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');
var video = document.getElementById('video');

// Get access to the camera!
if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    // Not adding `{ audio: true }` since we only want video now
    navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
        video.src = window.URL.createObjectURL(stream);
        video.play();
    });
}

// Trigger photo take
document.getElementById("snap").addEventListener("click", function() {
  if($('#suggest video').hasClass("on")){
    context.drawImage(video, 0, 0, 640, 480);
  }
});

$('#scan').click(function(){
  if($('#suggest').hasClass("on")){
    $('#suggest').addClass("off");
    $('#suggest').removeClass("on");
  }else{
    $('#suggest').addClass("on");
    $('#suggest').removeClass("off");
  }
});

$('#snap').click(function(){
  if($('#suggest video').hasClass("on")){
    $('#suggest video').addClass("off");
    $('#suggest video').removeClass("on");
    $('#suggest canvas').addClass("on");
    $('#suggest canvas').removeClass("off");
    $('#snap').html("Submit");
  }else{
    /*submit to API*/
    var formData = new FormData();
    canvas.toBlob(function(blob) {
      console.log(blob);
      var file = new File([blob], "blob.png", {type: "image/png", lastModified: Date.now()});
      formData.append("filename", blob);
      formData.append("access_key", "c2da496b4f1922f1274f");
      formData.append("secret_key", "e792831aa0aa4f33af651a083f8dd200fc0ab383");
      console.log(formData);
      $.ajax({
        url: "http://localhost:5000/upload_search",
        type: "POST",
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        success: function(response) {
            result(response);
        },
        error: function(jqXHR, textStatus, errorMessage) {
            console.log(errorMessage); // Optional
            $('#close').click();
        }
      }, 'image/png', 1);
    });
  }
});

$('#close').click(function(){
  $('#suggest').addClass("off");
  $('#suggest').removeClass("on");
  if($('#suggest video').hasClass("off")){
    $('#suggest video').addClass("on");
    $('#suggest video').removeClass("off");
    $('#suggest canvas').addClass("off");
    $('#suggest canvas').removeClass("on");
    $('#snap').html("Snap Photo");
  }
});

var result = function(data){
  console.log(data);
    window.location.replace('http://localhost:5000/result')
  /*
  $.ajax({
    url: "http://localhost:5000/result",
    type: "POST",
    data: data,
    cache: false,
    processData: false,
    contentType: 'application/json',
    success: function(response){
        console.log(response);
        window.open("http://localhost:5000/result", "result", results=response);
        $('#close').click();
    },
    error: function(jqXHR, textStatus, errorMessage) {
        console.log(errorMessage); // Optional
        $('#close').click();
    }
  });*/
};