<?php

   $data = $_REQUEST;

   $con = mysqli_connect('localhost','root','','dashboard');
   $insert = 'INSERT INTO abort_mission(msg) VALUES ("Request to Abort Mission")';
   mysqli_query($con, $insert);
   mysqli_close($con);

?>