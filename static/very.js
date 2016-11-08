function onbuttonclick() {
  var value = $("input").val();
  $.post("/contact-us", {message: value}, function (data, status, response) {
    console.log(data)
    alert(data);
  });
}

function onReady() {
  $('button').click(onbuttonclick);
}

$(document).ready(onReady);
