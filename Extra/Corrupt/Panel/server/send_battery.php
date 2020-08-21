<?php

    $data = $_REQUEST;
    $batpercent = $_REQUEST['send_battery'];

    $con = mysqli_connect('localhost','root','','dashboard');
    $insert = "INSERT INTO send_battery(percent) VALUES ('.$batpercent.')";
    mysqli_query($con,$insert);
    echo $batpercent;
    mysqli_close($con);

?>