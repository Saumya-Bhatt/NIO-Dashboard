<?php

    $data = $_REQUEST;
    $long_val = $_REQUEST['send_longitude'];

    $con = mysqli_connect('localhost','root','','dashboard');
    $insert = "INSERT INTO send_longitude(val) VALUES ('$long_val')";
    mysqli_query($con,$insert);
    echo $long_val;

    mysqli_close($con);

?>