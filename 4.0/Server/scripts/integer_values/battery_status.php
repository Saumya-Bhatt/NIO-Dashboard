<?php

    $data = $_REQUEST;
    $bat_val = $_REQUEST['battery_status'];

    $con = mysqli_connect('localhost','root','','nio_python');
    $insert = "INSERT INTO battery_value(value) VALUES ('$bat_val')";
    mysqli_query($con,$insert);
    mysqli_close($con);

?>