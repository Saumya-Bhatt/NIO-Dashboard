<?php

    if(isset($_FILES['file'])) {
        $uploadDir = 'C:/xampp/htdocs/NIO/3.0/UPLOAD/';
        $uploadFile = $uploadDir.basename($_FILES['file']['name']);
        if(move_uploaded_file($_FILES['file']['tmp_name'], $uploadFile)) {
            echo 'File was uploaded successfully.';
        } else {
            echo 'There was a problem saving the uploaded file';
        }
        echo '<br/><a href="FileUpload.php">Back to Uploader</a>';
    } else {
        ?>
        <form action="sendfile.php" method="POST" enctype="multipart/form-data">
    
            <label for="file">File : </label>
            <input type="file" name="file" id="file"><br>
            <input type="submit" value="SEND">

        </form>

        <?php
    }

?>