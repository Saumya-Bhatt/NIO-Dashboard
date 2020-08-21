<?php

    $data = $_REQUEST;
    $lat_val = $_REQUEST['send_latitude'];

    $con = mysqli_connect('localhost','root','','dashboard');
    $insert = "INSERT INTO send_latitude(val) VALUES ('$lat_val')";
    mysqli_query($con,$insert);
    echo $lat_val;

    mysqli_close($con);

?>