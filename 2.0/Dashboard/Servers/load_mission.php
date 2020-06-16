<?php

   $data = $_REQUEST;

   $con = mysqli_connect('localhost','root','','dashboard');
   $insert = 'INSERT INTO load_mission(msg) VALUES ("Request to load mission")';
   mysqli_query($con, $insert);
   mysqli_close($con);

?>