<?php

    $data = $_REQUEST;
    $depth_val = $_REQUEST['send_depth'];

    $con = mysqli_connect('localhost','root','','dashboard');
    $insert = "INSERT INTO send_depth(val) VALUES ('$depth_val')";
    mysqli_query($con,$insert);
    echo $depth_val;

    mysqli_close($con);

?>