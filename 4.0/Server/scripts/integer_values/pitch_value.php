<?php

    $data = $_REQUEST;
    $pitch_val = $_REQUEST['pitch_value'];

    $con = mysqli_connect('localhost','root','','nio_python');
    $insert = "INSERT INTO pitch_value(value) VALUES ('$pitch_val')";
    mysqli_query($con,$insert);
    mysqli_close($con);

?>