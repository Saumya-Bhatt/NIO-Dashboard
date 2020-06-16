<?php

   $data = $_REQUEST;

   $con = mysqli_connect('localhost','root','','dashboard');
   $insert = 'INSERT INTO user_position(msg) VALUES ("Request to get User Position scan GPS")';
   mysqli_query($con, $insert);
   mysqli_close($con);

?>