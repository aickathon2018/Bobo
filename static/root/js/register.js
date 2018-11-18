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
  if($('#autofill video').hasClass("on")){
    context.drawImage(video, 0, 0, 640, 480);
  }
});

$('#scan').click(function(){
  if($('#autofill').hasClass("on")){
    $('#autofill').addClass("off");
    $('#autofill').removeClass("on");
  }else{
    $('#autofill').addClass("on");
    $('#autofill').removeClass("off");
  }
});

$('#snap').click(function(){
  if($('#autofill video').hasClass("on")){
    $('#autofill video').addClass("off");
    $('#autofill video').removeClass("on");
    $('#autofill canvas').addClass("on");
    $('#autofill canvas').removeClass("off");
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
        url: "http://localhost:5000/upload",
        type: "POST",
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        success: function(response) {
            fillForm(JSON.parse(response));
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
  $('#autofill').addClass("off");
  $('#autofill').removeClass("on");
  if($('#autofill video').hasClass("off")){
    $('#autofill video').addClass("on");
    $('#autofill video').removeClass("off");
    $('#autofill canvas').addClass("off");
    $('#autofill canvas').removeClass("on");
    $('#snap').html("Snap Photo");
  }
});

var fillForm = function(data){
  console.log(data);
  $('#age').val(data['faces'][0]["age"]);
  console.log(data['faces'][0]["gender"]["confidence"]);
  if(data['faces'][0]["gender"]["confidence"] >= 60 && data['faces'][0]["gender"]["value"] == "Female") $('#gender').val("f");
  if(data['faces'][0]["gender"]["confidence"] >= 60 && data['faces'][0]["gender"]["value"] == "Male") $('#gender').val("m");
  if(data['faces'][0]["gender"]["confidence"] < 60) $('#gender').val("u");
  $('#close').click();
}