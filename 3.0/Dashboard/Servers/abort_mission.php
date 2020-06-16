<?php

   $data = $_REQUEST['file_path'];
   unlink($data);

   $con = mysqli_connect('localhost','root','','dashboard');
   $drop = "DELETE FROM load_mission WHERE msg = '$data'";
   mysqli_query($con, $drop);
   mysqi_close($con);

?>