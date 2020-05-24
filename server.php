<?php

    $data = $_REQUEST;
    $val = $_REQUEST["command_log"];
    
    $con = mysqli_connect("localhost",'root','','command_log');

    $insert = "INSERT INTO log(cmd) VALUES('$val')";
    $insert_log = mysqli_query( $con , $insert );

    mysqli_close($con);

    print var_dump($val);

?>