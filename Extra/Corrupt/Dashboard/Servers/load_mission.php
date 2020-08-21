<?php

    if(isset($_FILES['file'])) {
        $uploadDir = 'C:/xampp/htdocs/NIO/3.0/UPLOAD/';
        $uploadFile = $uploadDir.basename($_FILES['file']['name']);
        if(move_uploaded_file($_FILES['file']['tmp_name'], $uploadFile)) {
            echo 'File was uploaded successfully.';
        } else {
            echo 'There was a problem saving the uploaded file';
        }
        echo '<br/><a href="../index.html">Back to Dashboard</a>';
    } else {
        echo 'Please choose a file';
    }

    $con = mysqli_connect('localhost','root','','dashboard');
    $insert = "INSERT INTO load_mission(msg) VALUES ('$uploadFile')";
    mysqli_query($con, $insert);
    mysqli_close($con);

?>