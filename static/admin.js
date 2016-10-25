
$.get("contacts-details", function( data ) {
  var html = "";
  data.contacts.forEach(function (contact, i) {
    var element = "<div> They say " + contact.hi + " </div>";
    html = html + element;
  });

  $(document).ready(function () {
    document.body.innerHTML = html;
  });
});
