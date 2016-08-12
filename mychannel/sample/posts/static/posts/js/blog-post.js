$(function () {
    // Correctly decide between ws:// and wss://
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var ws_path = ws_scheme + '://' + window.location.host + window.location.pathname + "stream/";
    console.log("Connecting to " + ws_path);
    var socket = new ReconnectingWebSocket(ws_path);
    // Handle incoming messages
    socket.onmessage = function(message) {
        // Decode the JSON
        console.log("Got message " + message.data);
        var data = JSON.parse(message.data);
        // Create the inner content of the post div
        var content = "<h2>" + data.created + "</h2>" + data.html;
        // See if there's a div to replace it in, or if we should add a new one
        var existing = $("div[data-post-id=" + data.id + "]");
        if (existing.length) {
            existing.html(content);
        } else {
            var newdiv = $("<div class='post' data-post-id='" + data.id + "'>" + content + "</div>");
            $("#posts").prepend(newdiv);
        }
    };
    // Helpful debugging
    socket.onopen = function() { console.log("Connected to notification socket"); }
    socket.onclose = function() { console.log("Disconnected to notification socket"); }
});