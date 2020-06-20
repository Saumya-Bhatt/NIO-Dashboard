<?php 

    $con = mysqli_connect('localhost','root','','nio_dashboard');
    $get_latest_status = 'SELECT stat FROM connection ORDER BY id DESC limit 1';
    $latest_result = mysqli_query($con, $get_latest_status);
    $result_array = mysqli_fetch_array($latest_result, MYSQLI_ASSOC);
    $status = $result_array['stat'];
    echo $status;
    mysqli_close($con);

?>