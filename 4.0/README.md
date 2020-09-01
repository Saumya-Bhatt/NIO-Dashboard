# Setting up the Server

1. Go to [this link](https://www.apachefriends.org/download.html) to install XAMPP.
2. After downloading XAMPP, open the application. It should be in C:/xampp/xampp-control.exe
3. In the control pannel that opens up, click on the Apache and MySQL start button. It will start running once the text on the dashboard turns to green.

![This is how the XAMPP panel looks after clicking on the start button for Apache and MySQL](SETUP\Extra\Images\xampp.png?raw=true)

4. In your browser, open [localhost/phpmyadmin/](http://localhost/phpmyadmin/). It will open up a MySQL dashboard.
5. On the left-hand side, there would be a button called new. Click on it. It will open up a window saying 'Create Database'.
6. Just give the Database name as - `nio_python`. Click on 'Create' to continue.
<br></br>

![The Create Table window](SETUP\Extra\Images\create_db.png?raw=true)
<br></br>

7. You will automatically taken to the 'trial Database'. On the topbar, there would be an option of 'Import'. Click on it.
8. You will get an option to 'Choose file'. From the Folder 'SETUP' in this folder, choose and upload the file `mission_upload.db`.

<br></br>

# Setting up the application

1. In the 'SETUP' folder, there's a file named requirements.txt which has all the required python libraries to run this application
2. If you have Python Indexing Project Installed (PIP), in the command shell type
`pip install -r /path/to/requirements.txt`

3. If PIP is not installed or there's a problem during setup, try installing the packages manually from the requirements.txt

<br></br>

# Running the application

In the __APP folder__, open the command shell and type `python run.py`. It should automatically show open the browser and display the dashboard and also display the network URL and the local URL.

![Running the application](SETUP\Extra\Images\running_app.png?raw=true)

If the above mentioned step does not run, in the same root folder, open the command shell and type `streamlit run app.py`. Alawys keep the command shell on which the above file is running open. DO NOT CLOSE IT, as that would shut down the application.

<br></br>

# Using the consoles within the Dashboard

## **Map Console**

For offline maps, there's already trial files ready for use (The locations are that of NIO and Melbourne). They can be found in the SETUP\Extra\ marked as map_trial_1 and map_trial_2. There's also a video in that folder to see how t use the offline maps.

1. Firstly create a file - 'locations.txt'. It should have the coordinates of the places (currently accepts only 3 places) that you want to have it mapped in the lat-long format seperated by ','. New coordinate should start on a newline.
<br></br>

![Format of writing in the locations.txt and refloc.txt file](SETUP\Extra\Images\locations.png?raw=true)

2. __For using the Offline map:__ 
    
    1. Select an image (preferable from google maps). That image will act as the background on which the locations would be plotted. Make sure that the locations specified within the locations.txt file are well contained within it. Make sure that the image is in [.PNG] format.
    2. Take the coordinates of the __top-left__ and the __bottom-right__ corners of the image and in the same manner as that of the locations file, write it into a new file named- 'refloc.txt'.
    3. Open the console for the for the offline map within the dashboard. Then as instructed in the console, upload the files, locations.txt, refloc.txt and the image file which was selected. The offline map will start processing the files on it's own and display the result.

3. __For using the Online map:__

    1. Upload the locations.txt file which was earlier made.
    2. The application would automatically render a map showing the specified points.

<br></br>

## **File Upload**

There's no need for any extra setup here. Just upload the file that you want to run. That file will get uploaded in the database __nio_python__ that was created earlier. The files from there could be easily recalled by running an SQL script on the server side. The table also has a column for file status (running/uploaded/aborted). The server side script could read that and change functions accordingly.

The database already has an uploaded mission file (as a test) which would be shown up on the dashboard. You could remove that by clickicking on 'Abort Mission' button on the dashboard. This is a one-time-function only meaning, while starting the application again in the future, you won't have to do this again.

<br></br>

## **Camera Feed**

The dashboard uses a third-party IP camera to get the camera feed. This could be altered according to your requirements.

1. Go to [IP Camera](https://play.google.com/store/apps/details?id=com.pas.webcam) and install the application. This will be the third-party camera.
2. Make sure the application on which you are running the dashboard and the IP camera are over the same network.
2. Open the application and scroll to the bottom and click on the 'Start Server'
<br></br>

![Scroll to the bottom and click on Start Server](SETUP\Extra\Images\ip_camera.jpg?raw=true)

3. Click copy the url given. It should be of the format: http:\\192.168.43.129:8080

![Click copy the url given. Eg http:\\192.168.43.129:8080](SETUP\Extra\Images\ip_address.png?raw=true)

4. Open that URL into a browser. It should open up a new dashboard. In the video render option, select 'Javascript'.

![Open the copied link into the browser. It should display this window](SETUP\Extra\Images\ip_browser.png?raw=true)

5. Now the URL that you copied, just enter the 192.168.43.129:8080 part into the camera-feed console. It will open up a new window externally and start streaming video from the device on which IP camera application has been installed.

<br></br>

## **NOTE**

1. If while any of the process that are running crashes, in the browser, do a `ctrl + sht + r`. This will clear the memory cache of the program. If the problem still persists, try shutting down the application and start again.

2. If you have made (added an element\function\changed a variable) any changes to the files in the APP folder, the dashboard will give a prompt at it's top right corner. Click on `Always run`. This is a one-time-change, so that while the application is running and you make any changes, it will be instantly displayed on the dashboard.

3. To shut down the application, in the command shell on which it is running, type `ctrl + c`. Just closing the browser won't shut down the application. Make sure to stop the Apache and the MySQL server running on XAMPP.
