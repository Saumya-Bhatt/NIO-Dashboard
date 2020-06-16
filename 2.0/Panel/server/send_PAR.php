<?php

    $data = $_REQUEST;
    $par_val = $_REQUEST['send_PAR'];

    $con = mysqli_connect('localhost','root','','dashboard');
    $insert = "INSERT INTO sensor(PAR) VALUES ('$par_val')";
    mysqli_query($con,$insert);
    echo $par_val;

    mysqli_close($con);

?>