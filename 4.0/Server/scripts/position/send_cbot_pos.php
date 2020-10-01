<?php

    $data = $_REQUEST;
    $lat_val = $_REQUEST['send_latitude'];
    $long_val = $_REQUEST['send_longitude'];

    $con = mysqli_connect('localhost','root','','nio_python');
    $insert = "INSERT INTO cbot_position(latitude, longitude) VALUES ('$lat_val','$long_val')";
    mysqli_query($con,$insert);
    mysqli_close($con);

?>