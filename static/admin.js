
$.get("contacts-details", function( data ) {
  var html = "";
  data.contacts.forEach(function (contact, i) {
    var element = contact.sent_time + "<div> They say " + contact.message + " </div>";
    html = html + element;
  });

  $(document).ready(function () {
    document.body.innerHTML = html;
  });
});
