<?php

    $data = $_REQUEST;
    $temp = $_REQUEST['temperature'];
    $con1 = mysqli_connect('localhost','root','','command_log');
    $query1 = "INSERT INTO temperatureupdate(kelvin) VALUES('$temp')";
    $pushbattery = mysqli_query($con1,$query1);
    print($temp);
    mysqli_close($con1);

?>