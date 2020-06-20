<?php

   $data = $_REQUEST;

   $con = mysqli_connect('localhost','root','','dashboard');
   $insert = 'INSERT INTO builtin_test(msg) VALUES ("Request to Execute Built-in test")';
   mysqli_query($con, $insert);
   mysqli_close($con);

?>