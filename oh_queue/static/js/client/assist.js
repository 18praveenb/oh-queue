$(document).ready(function(){
  requestNotificationPermission();

  // Bind event listeners
  $('body').on('click', '.resolve', function(event) {
    $.post($(this).attr('data-url'));
  });

  // opening Socket
  var socket = io.connect('http://' + document.domain + ':' + location.port);

  // Socket handler for adding tickets
  socket.on('create_response', function(message) {
    $('#queue').append(message.assist_html);
    var details = {
      body: message.name + " - " + message.assignment + message.question + " in " + message.location
    }
    notifyUser("OH Queue: " + message.name + " in " + message.location, details);
  });

  socket.on('resolve_response', function(message) {
    $('#queue-ticket-' + message.id).remove();
    $('#resolved').append(message.html);
  });
});
