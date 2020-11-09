CREATE TABLE `auvInstances` (
  `ID` int PRIMARY KEY AUTO_INCREMENT,
  `AUV_Name` varchar(255),
  `AUV_Key` varchar(255)
);

CREATE TABLE `coordinates` (
  `ID` int PRIMARY KEY AUTO_INCREMENT,
  `Home_Latitude` varchar(255),
  `Home_Longitude` varchar(255),
  `Boat_Latitude` varchar(255),
  `Boat_Longitude` varchar(255),
  `CBot_Latitude` varchar(255),
  `CBot_Longitude` varchar(255),
  `Instance_Cordi_ID` int
);

CREATE TABLE `missionFile` (
  `ID` int PRIMARY KEY AUTO_INCREMENT,
  `Uploaded_File` mediumblob,
  `Time_Stamp` timestamp,
  `Instance_MissionFile_ID` int
);

CREATE TABLE `auvStatus` (
  `ID` int PRIMARY KEY AUTO_INCREMENT,
  `Battery` int,
  `Roll` varchar(255),
  `Pitch` varchar(255),
  `Yaw` varchar(255),
  `Depth` varchar(255),
  `Instance_AUVStatus_ID` int
);

ALTER TABLE `auvInstances` ADD FOREIGN KEY (`ID`) REFERENCES `coordinates` (`Instance_Cordi_ID`);

ALTER TABLE `auvInstances` ADD FOREIGN KEY (`ID`) REFERENCES `missionFile` (`Instance_MissionFile_ID`);

ALTER TABLE `auvInstances` ADD FOREIGN KEY (`ID`) REFERENCES `auvStatus` (`Instance_AUVStatus_ID`);
