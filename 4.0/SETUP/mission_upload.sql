-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 01, 2020 at 11:30 AM
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
(28, 'MaxDepth,20\r\nLF,3,4,372140,1708596,5,372265,1708650,0,200\r\nHD,3,4,95,40\r\nHD,3,4,295,30\r\nDP,2,0,15,50\r\nLF,2,4,372265,1708650,1,372390,1708686,2,300\r\nLF,2,4,372390,1708686,0,372519,1708733,2,300\r\nLF,2,4,372519,1708733,2,372506,1708617,2,300\r\nLF,2,4,372506,1708617,0,372333,1708580,0,300\r\nLF,2,4,372333,1708580,1,372166,1708543,2,300\r\nLF,2,4,372166,1708543,0,372140,1708596,0,300\r\nHD,3,4,95,20\r\nHD,2,4,150,30', '2020-08-31 17:38:14.199897', 'UPLOADED');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `mission_upload`
--
ALTER TABLE `mission_upload`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `mission_upload`
--
ALTER TABLE `mission_upload`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
