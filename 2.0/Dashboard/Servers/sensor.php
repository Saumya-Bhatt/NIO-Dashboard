<?php

   $data = $_REQUEST;

   $con = mysqli_connect('localhost','root','','dashboard');
   $insert = 'INSERT INTO sensor(msg) VALUES ("Request to connect to sensor")';
   mysqli_query($con, $insert);
   mysqli_close($con);

?>