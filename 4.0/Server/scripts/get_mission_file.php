<?php 

    $con = mysqli_connect('localhost','root','','nio_python');
    $get_latest_status = 'SELECT * FROM mission_upload ORDER BY id DESC limit 1';
    $latest_result = mysqli_query($con, $get_latest_status);
    $result_array = mysqli_fetch_array($latest_result, MYSQLI_ASSOC);
    mysqli_close($con);
    $json_format = json_encode($result_array, JSON_FORCE_OBJECT);
    print_r($json_format)

?>