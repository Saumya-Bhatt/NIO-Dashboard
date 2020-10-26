<?php

    $data = $_REQUEST;
    $yaw_val = $_REQUEST['yaw_value'];

    $con = mysqli_connect('localhost','root','','nio_python');
    $insert = "INSERT INTO yaw_value(value) VALUES ('$yaw_val')";
    mysqli_query($con,$insert);
    mysqli_close($con);

?>