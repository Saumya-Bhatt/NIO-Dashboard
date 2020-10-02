
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

//=================================================
//=============== MISSION FILE ====================
//=================================================

function get_mission_file() {
    $.ajax({
        url: 'http://localhost/NIO/4.0/scripts/get_mission_file.php',
        data: '',
        type: 'GET',
        success: function(response, status, http) {
            if (response === null) {
                document.getElementById('file_content').innerHTML = `No mission file uploaded`;
                document.getElementById('file_time').innerHTML = `NA`;
                document.getElementById(`file_status`).innerHTML = `NA`;
            } else {
                output = JSON.parse(response);
                document.getElementById('file_content').innerHTML = `<rt style='font-weight:bold'>File contents : </rt><br>`+output.input;
                document.getElementById('file_time').innerHTML = `<rt style='font-weight:bold'>Time stamp : </rt>`+output.time_stamp;
                document.getElementById('file_status').innerHTML = `<rt style='font-weight:bold'>Status : </rt>`+output.status;
            }
        },
        error: function(http, status, error){
            alert('ERROR'+error);
        }
    })
}
get_mission_file()
setInterval(get_mission_file,1000)