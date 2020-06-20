<?php

   $data = $_REQUEST['file_path'];
   unlink($data);

   $con = mysqli_connect('localhost','root','','nio_dashboard');
   $drop = "DELETE FROM mission_file WHERE file_dir = '$data'";
   mysqli_query($con, $drop);
   mysqi_close($con);

?>