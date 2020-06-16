<?php

   $data = $_REQUEST;

   $con = mysqli_connect('localhost','root','','dashboard');
   $insert = 'INSERT INTO compass(msg) VALUES ("Request to Execute compass caliberation")';
   mysqli_query($con, $insert);
   mysqli_close($con);

?>