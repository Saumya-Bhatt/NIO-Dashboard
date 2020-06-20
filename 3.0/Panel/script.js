

//COLUMN 1
function connection() {
    $.ajax({
        url: 'http://localhost/NIO/3.0/Panel/Server/connection.php',
        data: '',
        type: 'GET',
        dataType: 'text',
        success: function(response, status, http) {
            var dat1 = response.split('[');
            var dat2 = dat1[1].split(']');
            var foo = JSON.parse(dat2[0]);
            $('#connection_command').val(foo.msg);
            console.log(foo.msg);
        },
        error: function(http, status, error) {
            alert('ERROR: '+error);
        },
    })
}
setInterval(connection, 1000);

function connection_green() {
    var constat = 'green';
    $.ajax({
        url: 'http://localhost/NIO/3.0/Panel/Server/update_connection.php',
        data: 'connection_status='+constat,
        type: 'GET',
        dataType: 'text',
        success: function(response, status, http) {
            console.log('Connection: Green to update_connection.php');
            console.log(response);
        },
        error: function(http, status, error) {
            alert('ERROR :'+error);
        },
    })
}
function connection_orange() {
    var constat = 'orange';
    $.ajax({
        url: 'http://localhost/NIO/3.0/Panel/Server/update_connection.php',
        data: 'connection_status='+constat,
        type: 'GET',
        dataType: 'text',
        success: function(response, status, http) {
            console.log('Connection: Orange to update_connection.php');
            console.log(response);
        },
        error: function(http, status, error) {
            alert('ERROR :'+error);
        },
    })
}
function connection_red() {
    var constat = 'red';
    $.ajax({
        url: 'http://localhost/NIO/3.0/Panel/Server/update_connection.php',
        data: 'connection_status='+constat,
        type: 'GET',
        dataType: 'text',
        success: function(response, status, http) {
            console.log('Connection: Red to update_connection.php');
            console.log(response);
        },
        error: function(http, status, error) {
            alert('ERROR :'+error);
        },
    })
}

function sensor() {
    $.ajax({
        url: 'http://localhost/NIO/3.0/Panel/Server/sensor.php',
        data: '',
        type: 'GET',
        dataType: 'text',
        success: function(response, status, http) {
            var dat1 = response.split('[');
            var dat2 = dat1[1].split(']');
            var foo = JSON.parse(dat2[0]);
            $('#sensor_command').val(foo.msg);
            console.log(foo.msg);
        },
        error: function(http, status, error) {
            alert('ERROR: '+error);
        },
    })
}
setInterval(sensor,1000);

function camera() {
    $.ajax({
        url: 'http://localhost/NIO/3.0/Panel/Server/camera.php',
        data: '',
        type: 'GET',
        dataType: 'text',
        success: function(response, status, http) {
            var dat1 = response.split('[');
            var dat2 = dat1[1].split(']');
            var foo = JSON.parse(dat2[0]);
            $('#camera_connect').val(foo.msg);
            console.log(foo.msg);
        },
        error: function(http, status, error) {
            alert('ERROR: '+error);
        },
    })
}
setInterval(camera, 1000);

//SEND BATTERY DATA
function send_battery() {
    var batpercent = $("#send_battery").val();
    console.log(batpercent);
    $.ajax({
        url: "http://localhost/NIO/3.0/Panel/Server/send_battery.php",
        data: 'send_battery='+batpercent,
        type: 'GET',
        dataType: 'text',
        success: function(response, status, http) {
            console.log('Updated battery value sent to send_battery.php !');
            console.log(response);
        },
        error: function(http, status, error) {
            alert('ERROR: '+error);
        },
    })
}

//SEND YAW DATA
function send_yaw() {
    var yaw = $("#send_yaw").val();
    console.log(yaw);
    $.ajax({
        url: "http://localhost/NIO/3.0/Panel/Server/send_yaw.php",
        data: 'send_yaw='+yaw,
        type: 'GET',
        dataType: 'text',
        success: function(response, status, http) {
            console.log('Updated yaw value sent to send_yaw.php !');
            console.log(response);
        },
        error: function(http, status, error) {
            alert('ERROR: '+error);
        },
    })
}

//SEND DEPTH
function send_depth() {
    var depth = $("#depth").val();
    console.log(depth);
    $.ajax({
        url: "http://localhost/NIO/3.0/Panel/Server/send_depth.php",
        data: 'send_depth='+depth,
        type: 'GET',
        dataType: 'text',
        success: function(response, status, http) {
            console.log('Updated depth value sent to send_depth.php !');
            console.log(response);
        },
        error: function(http, status, error) {
            alert('ERROR: '+error);
        },
    })
}

//SEND LATITUDE
function send_latitude() {
    var lat = $("#latitude").val();
    console.log(lat);
    $.ajax({
        url: "http://localhost/NIO/3.0/Panel/Server/send_latitude.php",
        data: 'send_latitude='+lat,
        type: 'GET',
        dataType: 'text',
        success: function(response, status, http) {
            console.log('Updated latitude value sent to send_latitude.php !');
            console.log(response);
        },
        error: function(http, status, error) {
            alert('ERROR: '+error);
        },
    })
}

//SEND LONGITUDE
function send_longitude() {
    var long = $("#longitude").val();
    console.log(long);
    $.ajax({
        url: "http://localhost/NIO/3.0/Panel/Server/send_longitude.php",
        data: 'send_longitude='+long,
        type: 'GET',
        dataType: 'text',
        success: function(response, status, http) {
            console.log('Updated longitude value sent to send_longitude.php !');
            console.log(response);
        },
        error: function(http, status, error) {
            alert('ERROR: '+error);
        },
    })
}

//SEND PAR
function send_PAR() {
    var par = $("#PAR").val();
    console.log(par);
    $.ajax({
        url: "http://localhost/NIO/3.0/Panel/Server/send_PAR.php",
        data: 'send_PAR='+par,
        type: 'GET',
        dataType: 'text',
        success: function(response, status, http) {
            console.log('Updated PAR value sent to send_PAR.php !');
            console.log(response);
        },
        error: function(http, status, error) {
            alert('ERROR: '+error);
        },
    })
}

    //SEND CTD
    function send_CTD() {
        var ctd = $("#CTD").val();
        console.log(ctd);
        $.ajax({
            url: "http://localhost/NIO/3.0/Panel/Server/send_CTD.php",
            data: 'send_CTD='+ctd,
            type: 'GET',
            dataType: 'text',
            success: function(response, status, http) {
                console.log('Updated CTD value sent to send_CTD.php !');
                console.log(response);
            },
            error: function(http, status, error) {
                alert('ERROR: '+error);
            },
        })
    }