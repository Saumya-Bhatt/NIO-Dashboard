<?php

   $data = $_REQUEST;

   $con = mysqli_connect('localhost','root','','dashboard');
   $insert = 'INSERT INTO download_mission(msg) VALUES ("Request to download last mission logs")';
   mysqli_query($con, $insert);
   mysqli_close($con);

?>