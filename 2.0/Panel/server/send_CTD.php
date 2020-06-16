<?php

    $data = $_REQUEST;
    $ctd_val = $_REQUEST['send_CTD'];

    $con = mysqli_connect('localhost','root','','dashboard');
    $insert = "INSERT INTO sensor_ctd(CTD) VALUES ('$ctd_val')";
    mysqli_query($con,$insert);
    echo $ctd_val;

    mysqli_close($con);

?>