-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 25, 2020 at 07:48 AM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.4.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `nio_server`
--

-- --------------------------------------------------------

--
-- Table structure for table `auvinstances`
--

CREATE TABLE `auvinstances` (
  `ID` int(11) NOT NULL,
  `AUV_Name` varchar(255) NOT NULL,
  `AUV_Key` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auvstatus`
--

CREATE TABLE `auvstatus` (
  `ID` int(11) NOT NULL,
  `Battery` varchar(255) NOT NULL,
  `Roll` varchar(255) NOT NULL,
  `Pitch` varchar(255) NOT NULL,
  `Yaw` varchar(255) NOT NULL,
  `Depth` varchar(255) NOT NULL,
  `Instance_AUVStatus_ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `coordinates`
--

CREATE TABLE `coordinates` (
  `ID` int(11) NOT NULL,
  `Home_Latitude` varchar(255) NOT NULL,
  `Home_Longitude` varchar(255) NOT NULL,
  `Boat_Latitude` varchar(255) NOT NULL,
  `Boat_Longitude` varchar(255) NOT NULL,
  `CBot_Latitude` varchar(255) NOT NULL,
  `CBot_Longitude` varchar(255) NOT NULL,
  `Instance_Cordi_ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `missionfile`
--

CREATE TABLE `missionfile` (
  `ID` int(11) NOT NULL,
  `Uploaded_File` varchar(255) NOT NULL,
  `Time_Stamp` varchar(255) NOT NULL,
  `Instance_missionFile_ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auvinstances`
--
ALTER TABLE `auvinstances`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `auvstatus`
--
ALTER TABLE `auvstatus`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `coordinates`
--
ALTER TABLE `coordinates`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `missionfile`
--
ALTER TABLE `missionfile`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Instance_missionFile_ID` (`Instance_missionFile_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auvinstances`
--
ALTER TABLE `auvinstances`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `auvstatus`
--
ALTER TABLE `auvstatus`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `coordinates`
--
ALTER TABLE `coordinates`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `missionfile`
--
ALTER TABLE `missionfile`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `missionfile`
--
ALTER TABLE `missionfile`
  ADD CONSTRAINT `missionfile_ibfk_1` FOREIGN KEY (`Instance_missionFile_ID`) REFERENCES `auvinstances` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
