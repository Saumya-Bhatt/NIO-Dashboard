<?php

$con = mysqli_connect('localhost','root','','dashboard');

$get_last_query = 'SELECT msg FROM load_mission ORDER BY id DESC limit 1';
$get_data = mysqli_query($con,$get_last_query);
$row_count = mysqli_num_rows( $get_data );
mysqli_close($con);

$arr = array();
if( $row_count > 0 ) {
    while( $row = mysqli_fetch_array( $get_data ) ) {
        array_push( $arr , $row );
    }
}

$command = json_encode($arr,true);
print($command);

?>