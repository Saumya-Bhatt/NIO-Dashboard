(function() {
    var video = document.getElementById('video');
    vendorURL = window.URL || window.webkitURL;

    navigator.getMedia = navigator.getUserMedia || 
                        navigator.webkitGetUserMedia;

    navigator.getMedia({
        video: true,
        audio: false
    }, function(stream) {
        video.srcObject = stream;
        video.play();
    }, function(error) {
        //
    });
})();