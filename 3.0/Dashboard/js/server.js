
//======= CONNECTION COMMAND =======
function connect_command() {
    $.ajax({
        url: 'http://localhost/NIO/3.0/Dashboard/Server/command.php',
        type: 'GET',
        data: '',
        dataType: 'text',
        success: function(response, status, http) {
            console.log('Connection to command.php made!');
        },
        error: function(http, status, error) {
            alert('ERROR: '+error);
        },
    })
}

//======= SENSOR COMMAND =======
function sensor_command() {
    $.ajax({
        url: 'http://localhost/NIO/3.0/Dashboard/Server/sensor.php',
        type: 'GET',
        data: '',
        dataType: 'text',
        success: function(response, status, http) {
            console.log('Connection to sensor.php made!');
        },
        error: function(http, status, error) {
            alert('ERROR: '+error);
        },
    })
}

//======= CAMERA COMMAND =======
function camera_connect() {
    $.ajax({
        url: 'http://localhost/NIO/3.0/Dashboard/Server/camera.php',
        type: 'GET',
        data: '',
        dataType: 'text',
        success: function(response, status, http) {
            console.log('Connection to camera.php made!');
        },
        error: function(http, status, error) {
            alert('ERROR: '+error);
        },
    })
}

//======= UPDATE LOAD MISSION CLI =======
function cli_load_mission() {
    $.ajax({
        url: 'http://localhost/NIO/3.0/Dashboard/Server/update_mission_cli.php',
        type: 'GET',
        data: '',
        dataType: 'text',
        success: function(response, status, http) {
            var file1 = response.split('[');
            var file2 = file1[1].split(']');
            var file3 = JSON.parse(file2[0]);
            var file = file3.file_dir;
            var test = file.split('/');
            if(response == null) {
                document.getElementById('command_status').innerHTML = `<rt style='color: orange'>No mission loaded/running<rt>`;
            } else {
                document.getElementById('command_status').innerHTML = `<rt style='color: blue'>Loaded : </rt>`+test[7];
            };
            document.getElementById('download').innerHTML =  `<a href="../UPLOAD/`+test[7]+`" download style='    
                                                                color: black;
                                                                background-color: darkgray;
                                                                padding: 10px 20px;
                                                                border-radius: 5px;
                                                                text-decoration: none;'
                                                                >Download Last Mission file</a>`;
        },
        error: function(http, status, error) {
            alert('ERROR: '+error);
        },
    })
}
cli_load_mission()

//======= UPDATE EXECUTE MISSION CLI =======
function cli_execute_mission() {
    $.ajax({
        url: 'http://localhost/NIO/3.0/Dashboard/Server/update_mission_cli.php',
        type: 'GET',
        data: '',
        dataType: 'text',
        success: function(response, status, http) {
            var file1 = response.split('[');
            var file2 = file1[1].split(']');
            var file3 = JSON.parse(file2[0]);
            var file = file3.file_dir;
            var test = file.split('/');
            var div = document.getElementById('command_status').innerHTML = `<rt style='color: green'>Running : </rt>`+test[7];
        },
        error: function(http, status, error) {
            alert('ERROR: '+error);
        },
    })
}

//======= ABORT MISSION COMMAND =======
function abort_mission() {
    $.ajax({
        url: 'http://localhost/NIO/3.0/Dashboard/Server/update_mission_cli.php',
        type: 'GET',
        data: '',
        dataType: 'text',
        success: function(response, status, http) {
            var file1 = response.split('[');
            var file2 = file1[1].split(']');
            var file3 = JSON.parse(file2[0]);
            var file = file3.file_dir;
            var test = file.split('/');
            var div = document.getElementById('command_status').innerHTML = `<rt style='color: red'>Aborted : </rt>`+test[7];
            $.ajax({
                url: 'http://localhost/NIO/3.0/Dashboard/Server/abort_mission.php',
                type: 'GET',
                data: 'file_path='+file,
                dataType: 'text',
                success: function(response, status, http) {
                    console.log('file aborted');
                },
                error: function(http, status, error) {
                    alert('ERROR :'+error);
                }
            });
        },
        error: function(http, status, error) {
            alert('ERROR: '+error);
        },
    })
}

//======= UPDATE STATUS =======
function updateStatus() {
    var getStatusID = document.getElementById('connect_status')
    $.ajax({
        url: 'http://localhost/NIO/3.0/Dashboard/Server/update_status.php',
        data: '',
        type: 'GET',
        dataType: 'text',
        success: function(response, status, http) {
            console.log(response);
            if(response == 'green') {
                getStatusID.style.backgroundColor = `greenyellow`;
            } else if(response == 'orange') {
                getStatusID.style.backgroundColor = `lightsalmon`;
            } else if(response == 'red') {
                getStatusID.style.backgroundColor = `tomato`;
            } else if(response == null) {
                getStatusID.style.backgroundColor = `#141414`;
            }
        },
        error: function(http, status, error) {
            alert('ERROR :'+error);
        },
    })
}
updateStatus();
setInterval(updateStatus,1000);

//======= UPDATE BATTERY STATUS =======
function updateBattery() {
    $.ajax({
        url:'http://localhost/NIO/3.0/Dashboard/Server/update_battery.php',
        data: '',
        type: 'GET',
        dataType:'text',
        success: function(response,status,http) {
            var bat1 = response.split('[');
            var bat2 = bat1[1].split(']');
            var bat3 = JSON.parse(bat2[0]);
            var batpercent = bat3.percent;
            document.getElementById('battery_percent').innerHTML = 'Battery:'+batpercent+'%';
            console.log(batpercent);
            if(batpercent == null) {
                var fill = document.getElementById('batteryfill').style.height = `100px`;
            }
            var fill = document.getElementById('batteryfill').style.height = `${100-batpercent}px`;
        },
        error: function(http,status,error) {
            alert('ERROR: '+error);
        }
    })
};
updateBattery();
setInterval(updateBattery,1000);

//======= UPDATE YAW =======
function updateYaw() {
    $.ajax({
        url:'http://localhost/NIO/3.0/Dashboard/Server/update_yaw.php',
        data: '',
        type: 'GET',
        dataType:'text',
        success: function(response,status,http) {
            var yaw1 = response.split('[');
            var yaw2 = yaw1[1].split(']');
            var yaw3 = JSON.parse(yaw2[0]);
            var yaw_val = yaw3.val;
            console.log(yaw_val);
            document.querySelector('.dial_fill').style.transform = `rotate(${yaw_val/1000}turn)`;
            document.getElementById('compass_yaw').innerHTML = 'Yaw : '+yaw_val;
        },
        error: function(http,status,error) {
            alert('ERROR: '+error);
        }
    })
};
updateYaw();
setInterval(updateYaw,1000);

//======= UPDATE DEPTH =======
function updateDepth() {
    $.ajax({
        url:'http://localhost/NIO/3.0/Dashboard/Server/update_depth.php',
        data: '',
        type: 'GET',
        dataType:'text',
        success: function(response,status,http) {
            var depth1 = response.split('[');
            var depth2 = depth1[1].split(']');
            var depth3 = JSON.parse(depth2[0]);
            var depth_val = depth3.val;
            console.log(depth_val);
            document.getElementById('depth').innerHTML = `Depth :  `+ depth_val + ` ft`;
        },
        error: function(http,status,error) {
            alert('ERROR: '+error);
        }
    })
};
updateDepth();
setInterval(updateDepth,1000);

//======= UPDATE LATITUDE =======
function updateLat() {
    $.ajax({
        url:'http://localhost/NIO/3.0/Dashboard/Server/update_latitude.php',
        data: '',
        type: 'GET',
        dataType:'text',
        success: function(response,status,http) {
            var lat1 = response.split('[');
            var lat2 = lat1[1].split(']');
            var lat3 = JSON.parse(lat2[0]);
            var lat_val = lat3.val;
            console.log(lat_val);
            document.getElementById('latitude').innerHTML = `Latitude :  `+ lat_val + ` °N`;
        },
        error: function(http,status,error) {
            alert('ERROR: '+error);
        }
    })
};
updateLat();
setInterval(updateLat,1000);

//======= UPDATE LONGITUDE =======
function updateLong() {
    $.ajax({
        url:'http://localhost/NIO/3.0/Dashboard/Server/update_longitude.php',
        data: '',
        type: 'GET',
        dataType:'text',
        success: function(response,status,http) {
            var long1 = response.split('[');
            var long2 = long1[1].split(']');
            var long3 = JSON.parse(long2[0]);
            var long_val = long3.val;
            console.log(long_val);
            document.getElementById('longitude').innerHTML = `Longitude :  `+ long_val + ` °E`;
        },
        error: function(http,status,error) {
            alert('ERROR: '+error);
        }
    })
};
updateLong();
setInterval(updateLong,1000);

//======= UPDATE PAR VALUE =======
function updatePAR() {
    $.ajax({
        url:'http://localhost/NIO/3.0/Dashboard/Server/update_PAR.php',
        data: '',
        type: 'GET',
        dataType:'text',
        success: function(response,status,http) {
            var par1 = response.split('[');
            var par2 = par1[1].split(']');
            var par3 = JSON.parse(par2[0]);
            var par_val = par3.PAR;
            console.log(par_val);
            document.getElementById('PAR').innerHTML = par_val;
        },
        error: function(http,status,error) {
            alert('ERROR: '+error);
        }
    })
};
updatePAR();
setInterval(updatePAR,1000);

//======= UPDATE CTD VALUE =======
function updateCTD() {
    $.ajax({
        url:'http://localhost/NIO/3.0/Dashboard/Server/update_CTD.php',
        data: '',
        type: 'GET',
        dataType:'text',
        success: function(response,status,http) {
            var ctd1 = response.split('[');
            var ctd2 = ctd1[1].split(']');
            var ctd3 = JSON.parse(ctd2[0]);
            var ctd_val = ctd3.CTD;
            console.log(ctd_val);
            document.getElementById('CTD').innerHTML = ctd_val;
        },
        error: function(http,status,error) {
            alert('ERROR: '+error);
        }
    })
};
updateCTD();
setInterval(updateCTD,1000);