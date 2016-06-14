function onbuttonclick() {
  var value = $("input").val();
  console.log(value);
}

$(document).ready(function () {
  $('button').click(onbuttonclick);
});
