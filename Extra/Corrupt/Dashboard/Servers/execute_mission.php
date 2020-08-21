<?php

   $data = $_REQUEST;
   $con = mysqli_connect('localhost','root','','dashboard');
   $getlatest = 'SELECT msg FROM load_mission ORDER BY id DESC limit 1';
   $getdata = mysqli_query($con,$getlatest);

   $row_count = mysqli_num_rows( $getdata );
   $arr = array();
  
  if( $row_count > 0 ) {
     while( $row = mysqli_fetch_array( $getdata ) ) {
        array_push( $arr , $row );
     }
  }

   mysqli_close($con);
   $command = json_encode($arr,true);
   print($command);

?>