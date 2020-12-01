-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 01, 2020 at 08:27 AM
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
-- Database: `nio_python`
--

-- --------------------------------------------------------

--
-- Table structure for table `battery_value`
--

CREATE TABLE `battery_value` (
  `id` int(11) NOT NULL,
  `value` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `battery_value`
--

INSERT INTO `battery_value` (`id`, `value`) VALUES
(1, '42'),
(2, '78'),
(3, '88'),
(4, '72'),
(5, '36'),
(6, 'fgh'),
(7, '78'),
(8, '42'),
(9, '44');

-- --------------------------------------------------------

--
-- Table structure for table `boat_position`
--

CREATE TABLE `boat_position` (
  `id` int(11) NOT NULL,
  `latitude` varchar(255) NOT NULL,
  `longitude` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `boat_position`
--

INSERT INTO `boat_position` (`id`, `latitude`, `longitude`) VALUES
(1, '73.797515', '15.456070'),
(2, '73.8', '15.5'),
(3, '15.456058', '73.797539'),
(4, '73.797539', '15.456058');

-- --------------------------------------------------------

--
-- Table structure for table `cbot_position`
--

CREATE TABLE `cbot_position` (
  `id` int(11) NOT NULL,
  `latitude` varchar(255) NOT NULL,
  `longitude` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cbot_position`
--

INSERT INTO `cbot_position` (`id`, `latitude`, `longitude`) VALUES
(1, '73.799479', '15.457993'),
(2, '73.799479', '15.48'),
(3, '73.799479', '15.458'),
(4, '73.799479', '15.465'),
(5, '73.798631', '15.456132'),
(6, '73.77', '15.44'),
(7, '73.803311', '15.451560'),
(8, '73.799417', '15.452511'),
(9, ' 73.799479', '15.457993'),
(10, '73.801689', '15.458551');

-- --------------------------------------------------------

--
-- Table structure for table `depth`
--

CREATE TABLE `depth` (
  `id` int(11) NOT NULL,
  `value` text NOT NULL,
  `time stamp` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `home_position`
--

CREATE TABLE `home_position` (
  `id` int(11) NOT NULL,
  `latitude` varchar(255) NOT NULL,
  `longitude` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `home_position`
--

INSERT INTO `home_position` (`id`, `latitude`, `longitude`) VALUES
(1, '73.801925', '15.456380');

-- --------------------------------------------------------

--
-- Table structure for table `mission_upload`
--

CREATE TABLE `mission_upload` (
  `id` int(11) NOT NULL,
  `input` mediumtext DEFAULT NULL,
  `time_stamp` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `mission_upload`
--

INSERT INTO `mission_upload` (`id`, `input`, `time_stamp`, `status`) VALUES
(38, 'text1', '10:30', 'RUNNING'),
(39, 'text2', '10:32', 'ABORTED');

-- --------------------------------------------------------

--
-- Table structure for table `pitch_value`
--

CREATE TABLE `pitch_value` (
  `id` int(255) NOT NULL,
  `value` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pitch_value`
--

INSERT INTO `pitch_value` (`id`, `value`) VALUES
(1, '73.8');

-- --------------------------------------------------------

--
-- Table structure for table `yaw_value`
--

CREATE TABLE `yaw_value` (
  `id` int(255) NOT NULL,
  `value` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `yaw_value`
--

INSERT INTO `yaw_value` (`id`, `value`) VALUES
(1, '42.5'),
(2, '56.17');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `battery_value`
--
ALTER TABLE `battery_value`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `boat_position`
--
ALTER TABLE `boat_position`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cbot_position`
--
ALTER TABLE `cbot_position`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `depth`
--
ALTER TABLE `depth`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `home_position`
--
ALTER TABLE `home_position`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `mission_upload`
--
ALTER TABLE `mission_upload`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pitch_value`
--
ALTER TABLE `pitch_value`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `yaw_value`
--
ALTER TABLE `yaw_value`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `battery_value`
--
ALTER TABLE `battery_value`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `boat_position`
--
ALTER TABLE `boat_position`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `cbot_position`
--
ALTER TABLE `cbot_position`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `depth`
--
ALTER TABLE `depth`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `home_position`
--
ALTER TABLE `home_position`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `mission_upload`
--
ALTER TABLE `mission_upload`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;

--
-- AUTO_INCREMENT for table `pitch_value`
--
ALTER TABLE `pitch_value`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `yaw_value`
--
ALTER TABLE `yaw_value`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
