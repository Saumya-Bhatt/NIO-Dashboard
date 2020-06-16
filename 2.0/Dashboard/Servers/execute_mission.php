<?php

   $data = $_REQUEST;

   $con = mysqli_connect('localhost','root','','dashboard');
   $insert = 'INSERT INTO execute_mission(msg) VALUES ("Request to Execute Mission")';
   mysqli_query($con, $insert);
   mysqli_close($con);

?>