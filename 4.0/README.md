# Setting up the Server

1. Go to [this link](https://www.apachefriends.org/download.html) to install XAMPP.
2. After downloading XAMPP, open the application. It should be in C:/xampp/xampp-control.exe
3. In the control pannel that opens up, click on the Apache and MySQL start button. It will start running once the text on the dashboard turns to green.

![This is how the XAMPP panel looks after clicking on the start button for Apache and MySQL](Extra/Images/xampp.png)

4. In your browser, open [localhost/phpmyadmin/](http://localhost/phpmyadmin/). It will open up a MySQL dashboard.
5. On the left-hand side, there would be a button called new. Click on it. It will open up a window saying 'Create Database'.
6. Just give the Database name as - `nio_python`. Click on 'Create' to continue.
<br></br>

![The Create Table window](Extra/Images/create_db.png)
<br></br>

7. You will automatically taken to the 'trial Database'. On the topbar, there would be an option of 'Import'. Click on it.
8. You will get an option to 'Choose file'. From the Folder 'SETUP' in this folder, choose and upload the file `mission_upload.db`.
9. Repeate the steps from 7-8 for the remaining databses given in the SETUP folder.

<br></br>

# Setting up the application

1. If you have [pipenv](https://pypi.org/project/pipenv/) installed, first run `pipenv shell`. It will automatically create a virtual environment inside your project.
2. Then run `pipenv install` to install the required libraries.

2. If you don't have pipenv installed, you can either install it using the command `pip install pipenv` and follow step 1.
3. If you don't want to use pipenv, you can manually install the libraries using pip by running `pip install -r SETUP/requirements.txt` in the root directory of the project.


<br></br>

# Running the application

__Note__: If you have installed the libraries using pipenv, you would first need to run `pipenv shell` in the root directory.

In the __APP folder__, open the command shell and type `streamlit run app.py`. It should automatically show open the browser and display the dashboard and also display the network URL and the local URL.

![Running the application](Extra/Images/running_app.png)

If the above mentioned step does not run, in the same root folder, open the command shell and type `streamlit run app.py`. Alawys keep the command shell on which the above file is running open. DO NOT CLOSE IT, as that would shut down the application.

<br></br>

# Server Side Panel

This panel will mimick the server side of the project while the original dashboard would be present on the browser (client) side. It has currently options for changing the latitude and longitude of the Boat, Home and C-Bot, but later variations would allow control over battery, pitch, yaw, etc.

<br>

![Server Side Panel](Extra/Images/server_panel.png)

## Setting up the server side panel

1. Copy the `Server` folder into the following path - `C:\xampp\htdocs` (If you have downloaded XAMPP in it's default manner)
2. Start the Apache and the MySQL servers from the XAMPP control panel.
3. Go to your browser the type the following link - [http://localhost/Server/panel.html](http://localhost/Server/panel.html)
4. The server side panel should now be visible as that in the above image.

<br></br>

# Using the consoles within the Dashboard

## **Map Console**

For offline maps, there's already trial files ready for use (The example locations are given of CSIR-NIO and of Melbourne). They can be found in the Extra\ marked as map_trial_1 and map_trial_2. 
Just copy those values and enter it in the Server Side Panel.

1. The mapping feature automatically gets it's location values from the MySQL table which can be updated by the server side panel.
<br></br>

![Format of writing in the locations.txt and refloc.txt file](Extra/Images/refloc.png)
<br>
The contents of the (longitude/latitude) should be in this manner in the refloc.txt

2. __For using the Offline map:__ 
    
    1. Select an image (preferable from google maps). That image will act as the background on which the locations would be plotted. Make sure that the locations specified within the locations.txt file are well contained within it. Make sure that the image is in [.PNG] format.
    2. Take the coordinates of the __top-left__ and the __bottom-right__ corners of the image, write it into a new file named- 'refloc.txt'.
    3. Open the console for the for the offline map within the dashboard. Then as instructed in the console, upload the files, refloc.txt and the image file which was selected. The offline map will start processing the files on it's own and display the result.

3. __For using the Online map:__

    There is no need for any other work as the online map directly gets the location values from the MySQL table and renders the map from the internet.

<br></br>

__Note__ : Continuously switching between the online and the offline map may cause the dashboard to hangup. If that happens, try to hit the 'kill processes' button or press `ctrl + shift + r`. If issue still occurs, close the application from the terminal and start again.

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

![Scroll to the bottom and click on Start Server](Extra/Images/ip_camera.jpg)

3. Click copy the url given. It should be of the format: http:\\192.168.43.129:8080

![Click copy the url given. Eg http:\\192.168.43.129:8080](Extra/Images/ip_address.png)

4. Open that URL into a browser. It should open up a new dashboard. In the video render option, select 'Javascript'.

![Open the copied link into the browser. It should display this window](Extra/Images/ip_browser.png)

5. Now the URL that you copied, just enter the 192.168.43.129:8080 part into the camera-feed console. It will open up a new window externally and start streaming video from the device on which IP camera application has been installed.

<br></br>

## **NOTE**

1. If while any of the process that are running crashes, in the browser, do a `ctrl + sht + r`. This will clear the memory cache of the program. If the problem still persists, try shutting down the application and start again.

2. If you have made (added an element\function\changed a variable) any changes to the files in the APP folder, the dashboard will give a prompt at it's top right corner. Click on `Always run`. This is a one-time-change, so that while the application is running and you make any changes, it will be instantly displayed on the dashboard.

3. To shut down the application, in the command shell on which it is running, type `ctrl + c`. Just closing the browser won't shut down the application. Make sure to stop the Apache and the MySQL server running on XAMPP.
