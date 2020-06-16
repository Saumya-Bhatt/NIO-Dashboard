<?php

    $data = $_REQUEST;
    $pres = $_REQUEST['pressure'];
    $con1 = mysqli_connect('localhost','root','','command_log');
    $query1 = "INSERT INTO pressureupdate(pascal) VALUES('$pres')";
    $pushbattery = mysqli_query($con1,$query1);
    print($pres);
    mysqli_close($con1);

?>