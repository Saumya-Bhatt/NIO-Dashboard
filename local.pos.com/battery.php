<?php

    $data = $_REQUEST;
    $bat = $_REQUEST['battery'];
    $con1 = mysqli_connect('localhost','root','','command_log');
    $query1 = "INSERT INTO batteryupdate(percent) VALUES('$bat')";
    $pushbattery = mysqli_query($con1,$query1);
    print($bat);
    mysqli_close($con1);

?>