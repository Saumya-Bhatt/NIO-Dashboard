# Working Dashboard Example

Used jQuery and Ajax scripts to send and receive data from MySQL database. PHP as server side script and HTML/CSS/JS for interface.

1. Can perform basic CRUD operations on files which can be added locally onto server.
2. Can send and receive updates to and fro from the dashboard and the receiving panel.
3. Work done in version wise.

About the versions:
1. 1.0 gives the very basic dashboard where the only functionality is that the receiving panel sends inputs to the dashboard. The communication is 1-way.
2. 2.0 comes with the addition of extra commands. The user sends commands from dashboard and it get's received in the receiving panel. The communication is 2-ways.
3. 3.0 has the ability to interract with the local system as well. User can upload files to it which it can run (currently python only). The result is stored onto a databse.
4. Corrupt version works on version 2.0 and has it's capabilities. Not suitable tho as files are not organized efficiently.

The latest working version is 3.0 which can upload basic python files and run them.The details of the tables are as follows:
1. The result is stored in run_mission table
2. The files are uploaded in the UPLOAD folder, their path is stored in mission_file.
3. Abort mission deletes the file from the UPLOAD folder as well as it's path from the mission_file table.
4. Even after aborting mission, the one which was uploaded immediately before that could be downloaded from the Download last mission button.