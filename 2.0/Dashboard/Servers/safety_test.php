<?php

   $data = $_REQUEST;

   $con = mysqli_connect('localhost','root','','dashboard');
   $insert = 'INSERT INTO safety_test(msg) VALUES ("Request to Execute Safety Test")';
   mysqli_query($con, $insert);
   mysqli_close($con);

?>