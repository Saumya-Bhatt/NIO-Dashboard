
//=================================================
//=============== HOME POSITION ===================
//=================================================

function home_position() {
    var lat = $("#home_latitude").val();
    var long = $("#home_longitude").val();
    console.log(lat);
    console.log(long)
    $.ajax({
        url: "http://localhost/NIO/4.0/scripts/position/send_home_pos.php",
        data: {send_latitude: lat, send_longitude: long},
        type: 'GET',
        dataType: 'text',
        success: function(response, status, http) {
            console.log('Updated latitude value sent to send_home_lat.php !');
            console.log(response);
        },
        error: function(http, status, error) {
            alert('ERROR: '+error);
        },
    })
}

//=================================================
//=============== BOAT POSITION ===================
//=================================================

function boat_position() {
    var lat = $("#boat_latitude").val();
    var long = $("#boat_longitude").val();
    console.log(lat);
    console.log(long)
    $.ajax({
        url: "http://localhost/NIO/4.0/scripts/position/send_boat_pos.php",
        data: {send_latitude: lat, send_longitude: long},
        type: 'GET',
        dataType: 'text',
        success: function(response, status, http) {
            console.log('Updated latitude value sent to send_boat_lat.php !');
            console.log(response);
        },
        error: function(http, status, error) {
            alert('ERROR: '+error);
        },
    })
}

//=================================================
//=============== CBOT POSITION ===================
//=================================================

function cbot_position() {
    var lat = $("#cbot_latitude").val();
    var long = $("#cbot_longitude").val();
    console.log(lat);
    console.log(long)
    $.ajax({
        url: "http://localhost/NIO/4.0/scripts/position/send_cbot_pos.php",
        data: {send_latitude: lat, send_longitude: long},
        type: 'GET',
        dataType: 'text',
        success: function(response, status, http) {
            console.log('Updated latitude value sent to send_cbot_lat.php !');
            console.log(response);
        },
        error: function(http, status, error) {
            alert('ERROR: '+error);
        },
    })
}