<?php

    $con = mysqli_connect('localhost','root','','nio_dashboard');
    $query = 'SELECT file_dir FROM mission_file ORDER BY id DESC LIMIT 1';
    $getdata = mysqli_query($con, $query);

    while($row = mysqli_fetch_assoc($getdata)) {
        $dir = $row['file_dir'];
    };

    $dir_arr = explode("/", $dir);
    $file = $dir_arr[7];

    mysqli_close($con);

    $command = escapeshellcmd("../UPLOAD/stringfrmt.py");
    $output = shell_exec("cd ../UPLOAD && python $file");
    
    if($output) {
        echo " <br> Mission file is running successfully.<br><br>OUTPUT : $output <br><br> Go <a href='../index.html'>back to dashboard</a>";
    } else {
        echo 'There was an error running the file';
    }

    $con2 = mysqli_connect('localhost','root','','nio_dashboard');
    $query2 = "INSERT INTO run_mission (file,output) VALUES ('$file','$output')";
    mysqli_query($con2, $query2);
    mysqli_close($con2);

?>