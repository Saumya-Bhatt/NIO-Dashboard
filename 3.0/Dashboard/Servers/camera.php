<?php

   $data = $_REQUEST;

   $con = mysqli_connect('localhost','root','','dashboard');
   $insert = 'INSERT INTO camera(msg) VALUES ("Request to connect to camera")';
   mysqli_query($con, $insert);
   mysqli_close($con);

?>