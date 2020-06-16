<?php

   $data = $_REQUEST;

   $con = mysqli_connect('localhost','root','','dashboard');
   $insert = 'INSERT INTO connection(msg,stat) VALUES ("Request to connect","Awaiting status")';
   mysqli_query($con, $insert);
   mysqli_close($con);

?>