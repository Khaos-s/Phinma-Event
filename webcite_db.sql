-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 25, 2024 at 04:18 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `webcite_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `list_db`
--

CREATE TABLE `list_db` (
  `num_id` int(11) NOT NULL,
  `school_id` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `age` int(99) NOT NULL,
  `school_email` varchar(255) NOT NULL,
  `course` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `list_db`
--

INSERT INTO `list_db` (`num_id`, `school_id`, `name`, `age`, `school_email`, `course`) VALUES
(9, '0423-123-123', 'Neil Mars', 24, 'Neil@yahoo.com', 'BSIT 2nd Year'),
(11, '04-2324-03123', 'Lopez, John', 16, 'johnnarveylopez0@gmail.com', 'BSIT'),
(12, '04-2324-039475', 'NEil', 26, 'joel.cabales.ui@phinmaed.com', 'BSIT');

-- --------------------------------------------------------

--
-- Table structure for table `sign_up`
--

CREATE TABLE `sign_up` (
  `school_id` int(15) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `age` int(99) NOT NULL,
  `school_email` varchar(255) NOT NULL,
  `course` varchar(255) NOT NULL,
  `year_level` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sign_up`
--

INSERT INTO `sign_up` (`school_id`, `first_name`, `last_name`, `age`, `school_email`, `course`, `year_level`) VALUES
(1234, 'hot', 'sauce', 0, 'hahah@yahoo.com', 'BSIT', '2nd year'),
(123124, 'Arvy', 'Lopez', 0, 'joza.lopez@phinmaed.com', 'BSIT', '2nd year');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `list_db`
--
ALTER TABLE `list_db`
  ADD PRIMARY KEY (`num_id`);

--
-- Indexes for table `sign_up`
--
ALTER TABLE `sign_up`
  ADD PRIMARY KEY (`school_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `list_db`
--
ALTER TABLE `list_db`
  MODIFY `num_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
