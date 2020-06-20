<?php

    $data = $_REQUEST;
    $yaw_val = $_REQUEST['send_yaw'];

    $con = mysqli_connect('localhost','root','','dashboard');
    $insert = "INSERT INTO send_yaw(val) VALUES ('.$yaw_val.')";
    mysqli_query($con,$insert);
    echo $yaw_val;

    mysqli_close($con);

?>