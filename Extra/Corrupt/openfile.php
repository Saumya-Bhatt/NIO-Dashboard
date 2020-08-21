<?php

$myfile = fopen("C:/xampp/htdocs/NIO/3.0/UPLOAD/bio.pdf", "r") or die("Unable to open file!");
echo fread($myfile,filesize("bio.pdf"));
fclose($myfile);

?>