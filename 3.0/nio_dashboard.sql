-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 20, 2020 at 02:53 PM
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
-- Database: `nio_dashboard`
--

-- --------------------------------------------------------

--
-- Table structure for table `camera`
--

CREATE TABLE `camera` (
  `id` int(11) NOT NULL,
  `msg` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `camera`
--

INSERT INTO `camera` (`id`, `msg`) VALUES
(1, 'Request to connect to camera');

-- --------------------------------------------------------

--
-- Table structure for table `connection`
--

CREATE TABLE `connection` (
  `id` int(11) NOT NULL,
  `msg` varchar(200) NOT NULL,
  `stat` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `connection`
--

INSERT INTO `connection` (`id`, `msg`, `stat`) VALUES
(1, 'Request to connect', 'red');

-- --------------------------------------------------------

--
-- Table structure for table `mission_file`
--

CREATE TABLE `mission_file` (
  `id` int(11) NOT NULL,
  `file_dir` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `mission_file`
--

INSERT INTO `mission_file` (`id`, `file_dir`) VALUES
(4, 'C:/xampp/htdocs/NIO/3.0/Dashboard/UPLOAD/');

-- --------------------------------------------------------

--
-- Table structure for table `run_mission`
--

CREATE TABLE `run_mission` (
  `id` int(11) NOT NULL,
  `file` varchar(200) NOT NULL,
  `output` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `run_mission`
--

INSERT INTO `run_mission` (`id`, `file`, `output`) VALUES
(1, 'stringfrmt.py', 'Chris bought 4 item(s) at a price of 3.24 each for a total of 12.96\n'),
(2, 'pandas.py', ''),
(3, 'stringfrmt.py', 'Chris bought 4 item(s) at a price of 3.24 each for a total of 12.96\n'),
(4, 'test.py', 'Hello World!\n');

-- --------------------------------------------------------

--
-- Table structure for table `send_battery`
--

CREATE TABLE `send_battery` (
  `id` int(11) NOT NULL,
  `percent` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `send_battery`
--

INSERT INTO `send_battery` (`id`, `percent`) VALUES
(1, 4),
(2, 42),
(3, 42),
(4, 42),
(5, 42);

-- --------------------------------------------------------

--
-- Table structure for table `send_depth`
--

CREATE TABLE `send_depth` (
  `id` int(11) NOT NULL,
  `val` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `send_depth`
--

INSERT INTO `send_depth` (`id`, `val`) VALUES
(1, '2'),
(2, '287'),
(3, '287'),
(4, '287.'),
(5, '287.67'),
(6, '287.672'),
(7, '287.672');

-- --------------------------------------------------------

--
-- Table structure for table `send_latitude`
--

CREATE TABLE `send_latitude` (
  `id` int(11) NOT NULL,
  `val` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `send_latitude`
--

INSERT INTO `send_latitude` (`id`, `val`) VALUES
(1, '89'),
(2, '89'),
(3, '891'),
(4, '891.'),
(5, '891.8'),
(6, '891.80');

-- --------------------------------------------------------

--
-- Table structure for table `send_longitude`
--

CREATE TABLE `send_longitude` (
  `id` int(11) NOT NULL,
  `val` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `send_longitude`
--

INSERT INTO `send_longitude` (`id`, `val`) VALUES
(1, '1'),
(2, '13'),
(3, '13.'),
(4, '13.65'),
(5, '13.65'),
(6, ''),
(7, '6'),
(8, '68'),
(9, '6852'),
(10, '6852'),
(11, '6852.'),
(12, '6852.56'),
(13, '6852.56'),
(14, '6852.56'),
(15, '6852.56'),
(16, '682.56'),
(17, '62.56');

-- --------------------------------------------------------

--
-- Table structure for table `send_yaw`
--

CREATE TABLE `send_yaw` (
  `id` int(11) NOT NULL,
  `val` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `send_yaw`
--

INSERT INTO `send_yaw` (`id`, `val`) VALUES
(1, 7),
(2, 72);

-- --------------------------------------------------------

--
-- Table structure for table `sensor`
--

CREATE TABLE `sensor` (
  `id` int(11) NOT NULL,
  `msg` varchar(200) NOT NULL,
  `PAR` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sensor`
--

INSERT INTO `sensor` (`id`, `msg`, `PAR`) VALUES
(1, 'Request to connect to sensor', NULL),
(2, '', '67'),
(3, '', '67'),
(4, '', ''),
(5, '', '6'),
(6, '', '623'),
(7, '', '623'),
(8, '', '6238'),
(9, 'Request to connect to sensor', NULL),
(10, '', '623'),
(11, '', '62345'),
(12, '', '62345');

-- --------------------------------------------------------

--
-- Table structure for table `sensor_ctd`
--

CREATE TABLE `sensor_ctd` (
  `id` int(11) NOT NULL,
  `CTD` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sensor_ctd`
--

INSERT INTO `sensor_ctd` (`id`, `CTD`) VALUES
(1, '3'),
(2, '35'),
(3, '35'),
(4, '35 4'),
(5, '35 47'),
(6, '35 47'),
(7, '35 47 2'),
(8, '35 47 28');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `camera`
--
ALTER TABLE `camera`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `connection`
--
ALTER TABLE `connection`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `mission_file`
--
ALTER TABLE `mission_file`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `run_mission`
--
ALTER TABLE `run_mission`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `send_battery`
--
ALTER TABLE `send_battery`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `send_depth`
--
ALTER TABLE `send_depth`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `send_latitude`
--
ALTER TABLE `send_latitude`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `send_longitude`
--
ALTER TABLE `send_longitude`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `send_yaw`
--
ALTER TABLE `send_yaw`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sensor`
--
ALTER TABLE `sensor`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sensor_ctd`
--
ALTER TABLE `sensor_ctd`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `camera`
--
ALTER TABLE `camera`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `connection`
--
ALTER TABLE `connection`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `mission_file`
--
ALTER TABLE `mission_file`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `run_mission`
--
ALTER TABLE `run_mission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `send_battery`
--
ALTER TABLE `send_battery`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `send_depth`
--
ALTER TABLE `send_depth`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `send_latitude`
--
ALTER TABLE `send_latitude`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `send_longitude`
--
ALTER TABLE `send_longitude`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `send_yaw`
--
ALTER TABLE `send_yaw`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `sensor`
--
ALTER TABLE `sensor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `sensor_ctd`
--
ALTER TABLE `sensor_ctd`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
