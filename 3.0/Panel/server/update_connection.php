<?php

    $data = $_REQUEST;
    $latest_status = $_REQUEST['connection_status'];
    $con = mysqli_connect('localhost','root','','dashboard');

    $get_last_request = "SELECT id FROM connection ORDER BY id DESC limit 1";
    $return_request = mysqli_query($con, $get_last_request);
    $row = mysqli_fetch_array( $return_request, MYSQLI_ASSOC );
    $last_id = $row['id'];

    $update_status = "UPDATE connection SET stat = '$latest_status' WHERE id = $last_id";
    mysqli_query($con, $update_status);
    mysqli_close($con);

    print_r($last_id);
    print_r($latest_status);
?>