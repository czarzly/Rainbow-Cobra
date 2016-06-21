function onbuttonclick() {
  var value = $("input").val();
  $.post("/contact-us", {key: value});
}

function onReady() {
  $('button').click(onbuttonclick);
}

$(document).ready(onReady);
