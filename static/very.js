function onbuttonclick() {
  var value = $("input").val();
  alert(value);
}

$(document).ready(function () {
  $('button').click(onbuttonclick);
});
