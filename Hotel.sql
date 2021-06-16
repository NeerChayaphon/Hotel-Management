-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jun 07, 2021 at 10:35 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 7.4.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `FinalProject`
--

-- --------------------------------------------------------

--
-- Table structure for table `Booking`
--

CREATE TABLE `Booking` (
  `BookingID` int(11) NOT NULL,
  `CheckInDate` date NOT NULL DEFAULT current_timestamp(),
  `CheckOutDate` date NOT NULL DEFAULT '0000-00-00',
  `UserID` int(11) DEFAULT NULL,
  `DiscountCode` varchar(10) DEFAULT NULL,
  `TotalPrice` double(8,2) NOT NULL DEFAULT 0.00,
  `TotalDiscount` double(8,2) NOT NULL DEFAULT 0.00,
  `BookingStatus` varchar(10) NOT NULL DEFAULT 'Booked',
  `TotalGuest` int(11) DEFAULT NULL,
  `TotalBreakfast` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Booking`
--

INSERT INTO `Booking` (`BookingID`, `CheckInDate`, `CheckOutDate`, `UserID`, `DiscountCode`, `TotalPrice`, `TotalDiscount`, `BookingStatus`, `TotalGuest`, `TotalBreakfast`) VALUES
(11, '2021-06-25', '2021-05-28', 7, NULL, 4000.00, 0.00, 'Check Out', 1, 1),
(13, '2021-05-20', '2021-05-21', 19, NULL, 3500.00, 0.00, 'Check Out', 3, 3),
(14, '2021-05-20', '2021-05-21', 5, NULL, 1500.00, 0.00, 'Check Out', 1, 0),
(15, '2021-05-20', '2021-05-21', 9, NULL, 1500.00, 0.00, 'Check Out', 1, 0),
(16, '2021-05-11', '2021-05-13', 1, NULL, 2700.00, 0.00, 'Check Out', 1, 0),
(17, '2021-05-11', '2021-05-13', 25, NULL, 3960.00, 440.00, 'Check Out', 9, 0),
(19, '2021-05-28', '2021-05-29', 2, NULL, 3800.00, 0.00, 'Check Out', 2, 2),
(20, '2021-05-29', '2021-05-30', 2, NULL, 3600.00, 0.00, 'Check Out', 2, 0),
(21, '2021-05-29', '2021-05-31', 9, 'SAVE10', 3420.00, 380.00, 'Check Out', 4, 3),
(23, '2021-06-02', '2021-06-03', 1, 'SAVE20', 3520.00, 880.00, 'Check Out', 4, 4),
(24, '2021-06-02', '2021-06-03', 20, 'SAVE20', 5100.00, 900.00, 'Check Out', 5, 3),
(26, '2021-06-03', '2021-06-05', 3, NULL, 7300.00, 0.00, 'Check Out', 6, 11),
(27, '2021-06-12', '2021-06-14', 26, 'SAVE20', 3700.00, 0.00, 'Check Out', 1, 1),
(29, '2021-06-12', '2021-06-14', 30, 'SAVE10', 3600.00, 0.00, 'Check Out', NULL, NULL),
(31, '2021-06-02', '2021-06-06', 3, NULL, 4200.00, 0.00, 'Check Out', 1, 1),
(32, '2021-06-05', '2021-06-08', 3, 'SAVE20', 4760.00, 740.00, 'Check Out', 2, 2),
(35, '2021-06-06', '2021-06-09', 23, NULL, 5200.00, 0.00, 'Check In', 1, 1),
(36, '2021-06-05', '2021-06-07', 39, 'SAVE20', 6880.00, 1720.00, 'Check Out', 4, 4),
(37, '2021-06-09', '2021-06-11', 39, 'SAVE20', 5920.00, 1480.00, 'Booked', 4, 4),
(38, '2021-06-07', '2021-06-10', 31, 'SAVE20', 4000.00, 0.00, 'Check In', 5, 3),
(40, '2021-06-07', '2021-06-09', 5, 'SAVE20', 5000.00, 0.00, 'Check In', 4, 4),
(41, '2021-06-08', '2021-06-09', 6, 'SAVE20', 3000.00, 0.00, 'Booked', 5, 5),
(42, '2021-06-07', '2021-06-10', 3, 'SAVE20', 11400.00, 0.00, 'Check In', 5, 5),
(43, '2021-06-09', '2021-06-11', 41, 'SAVE20', 6880.00, 1720.00, 'Booked', 4, 4),
(44, '2021-06-07', '2021-06-09', 3, 'SAVE20', 4000.00, 0.00, 'Booked', 5, 5);

-- --------------------------------------------------------

--
-- Table structure for table `Discount`
--

CREATE TABLE `Discount` (
  `DiscountCode` varchar(10) NOT NULL,
  `DiscountPercent` double(5,2) NOT NULL,
  `StartDate` date NOT NULL DEFAULT current_timestamp(),
  `ExpireDate` date NOT NULL DEFAULT '0000-00-00'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Discount`
--

INSERT INTO `Discount` (`DiscountCode`, `DiscountPercent`, `StartDate`, `ExpireDate`) VALUES
('SAVE10', 10.00, '2021-05-01', '2021-06-08'),
('SAVE20', 20.00, '2021-06-02', '2021-06-12'),
('SAVE30', 30.00, '2021-06-06', '2021-06-08');

-- --------------------------------------------------------

--
-- Table structure for table `GuestInfo`
--

CREATE TABLE `GuestInfo` (
  `GuestID` int(11) NOT NULL,
  `FirstName` varchar(32) NOT NULL,
  `LastName` varchar(32) NOT NULL,
  `PhoneNumber` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `GuestInfo`
--

INSERT INTO `GuestInfo` (`GuestID`, `FirstName`, `LastName`, `PhoneNumber`) VALUES
(1, 'Kanano', 'Mono', '0841234554'),
(2, 'Uzui', ' Tengen', '0988512443'),
(3, 'Tokito', ' Muichiro', '0624591024'),
(4, 'Himejima', ' Gyomei', '0632959234'),
(5, 'Iguro', 'Obanai', '0862347654'),
(6, 'Kanroji', 'Mitsuri', '0635039938'),
(7, 'Rengoku', 'Kyojuro', '0597492837'),
(8, 'Shinazugawa', 'Sanemi', '0923473634'),
(9, 'Ubuyashiki', 'Kagaya', '0220010097'),
(10, 'Kibutsuji', 'Muzan', '0945625374'),
(11, 'Urokodaki', 'Sakonji', '0628462389'),
(12, 'Hashibira', 'Inosuke', '0484734847'),
(13, 'Monkey D. ', 'Luffy', '0984563830'),
(14, 'Roronoa', 'Zoro', '0749364846'),
(15, 'Vinsmoke', 'Sanji', '0752937495'),
(16, 'TonyTony', 'Chopper', '0375937845'),
(17, 'Nico', 'Robin', '0475937593'),
(18, 'Hamming', 'Brook', '0586938596'),
(19, 'Gold D.', 'Roger', '0586938569'),
(20, 'Silvers', ' Rayleigh', '0576947859'),
(21, 'Edward', 'Newgate', '0585693859'),
(22, 'Portgas D.', 'Ace', '0586949586'),
(23, 'Mikaze', 'Ai', '0586948593'),
(24, 'Arima', 'Kousei', '0472394857'),
(25, 'Shiota', 'Nagisa', '0586938571'),
(26, 'Kise', 'Ryota', '0495041576'),
(27, 'Kurosaki', 'Ichigo', '0957483910'),
(28, 'Kurusu', 'Syo', '0340503858'),
(29, 'Yukinoshita', 'Yukino', '0594837501'),
(30, 'Yoshioka', 'Futaba', '0295748134'),
(31, 'Jotaro', 'Kujo', '0443568595'),
(32, 'Onodera', 'Kosaki', '0596869482'),
(33, 'Zenitsu', 'Agatsuma', '0962651221'),
(34, 'Neer', 'Chayaphon', '0850961559'),
(42, 'Tom', 'Jerry', '0865123231'),
(43, 'Sam', 'Sky', '0971231771'),
(44, 'Paul', 'sky', '0981231441'),
(45, 'Deno', 'Samy', '0981512662');

-- --------------------------------------------------------

--
-- Table structure for table `MemberInfo`
--

CREATE TABLE `MemberInfo` (
  `UserID` int(11) NOT NULL,
  `FirstName` varchar(32) NOT NULL,
  `LastName` varchar(32) NOT NULL,
  `UserName` varchar(32) NOT NULL,
  `PassWord` varchar(32) NOT NULL,
  `Email` varchar(32) NOT NULL,
  `PhoneNumber` varchar(10) NOT NULL,
  `SignUpDate` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `MemberInfo`
--

INSERT INTO `MemberInfo` (`UserID`, `FirstName`, `LastName`, `UserName`, `PassWord`, `Email`, `PhoneNumber`, `SignUpDate`) VALUES
(1, 'Chayaphon', 'Bunyakan', 'Chayaphon1551', 'Ngneer12345@', 'neerza555@gmail.com', '0850961551', '2021-04-15 22:04:47'),
(2, 'Tanjiro', 'Kamado', 'Tanjiro1551', 'Kamado1234', 'Tanjiro@gmail.com', '0987651423', '2021-05-15 23:48:30'),
(3, 'Nezuko', 'Kamado', 'Nezuko1551', 'Kamado1551', 'Nezuko@gmail.com', '0850715113', '2021-04-17 17:18:30'),
(4, 'Sample', 'Sample', 'Sample', 'Sample', 'Sample@gmail.com', '0850961551', '2021-06-06 03:28:44'),
(5, 'Lee', 'Jieun', 'IU_official', 'LoveJieunmak2', 'IU_socute@gmail.com', '0974234234', '2021-06-05 01:28:25'),
(6, 'Uzui', ' Tengen', 'GodUzuiiii', 'Tengen_god77', 'uzui_2222@gmail.com', '0988512443', '2021-06-07 03:43:00'),
(7, 'Tokito', ' Muichiro', 'Muichiro99', 'Muiqwert56', 'Muichiro99@mail.com', '0624591024', '2021-06-08 03:12:00'),
(8, 'Himejima', ' Gyomei', 'GyoHimejima', 'loveIUsocute', 'GyoHimejimamei', '0632959234', '2021-06-11 04:28:00'),
(9, 'Iguro', 'Obanai', 'Snake2fish2', 'Loveyoukunroji', 'Snake2@fish2mail.com', '0862347654', '2021-06-22 07:54:00'),
(10, 'Kanroji', 'Mitsuri', 'love_Kanroji', 'cutecute_kanroji', 'Kanroji25@lovemail.com', '0635039938', '2021-06-25 11:02:00'),
(11, 'Rengoku', 'Kyojuro', 'Kyojuro_Umai', 'Umai_umaiumai', 'Kyojuro05@firemail.com', '0597492837', '2021-06-29 18:44:00'),
(12, 'Shinazugawa', 'Sanemi', 'Sanemi2254', 'zxcvbn1234', 'Sanemi@windmail.com', '0923473634', '2021-07-01 09:24:00'),
(13, 'Ubuyashiki', 'Kagaya', 'Ubuyashiki097', 'Kagaya97', 'Ubuyashiki@headmail.com', '0220010097', '2021-07-05 22:34:00'),
(14, 'Kibutsuji', 'Muzan', 'Muzan001', 'Muzan_no1', 'Muzan@headmail.com', '0945625374', '2021-07-10 04:02:00'),
(15, 'Urokodaki', 'Sakonji', 'Urokodaki_Sa', 'Urokodaki023123', 'Sakonji053@watermail.com', '0628462389', '2021-07-15 10:44:00'),
(16, 'Hashibira', 'Inosuke', 'InosukeisGod', 'GodInosuke99', 'Inosukegod@beastmail.com', '0484734847', '2021-07-24 14:02:00'),
(17, 'Monkey D. ', 'Luffy', 'LuffyKingofsea', 'Luffyloveniku', 'LuffyD@mail.com', '0984563830', '2021-06-25 00:36:00'),
(18, 'Roronoa', 'Zoro', 'Roronoa1234', 'Zoro0987', 'Roronoa82@gmail.com', '0749364846', '2021-07-30 09:04:00'),
(19, 'Vinsmoke', 'Sanji', 'Sanjilovelove', '12Sanji456', '12Sanji@mail.com', '0752937495', '2021-08-01 16:08:00'),
(20, 'TonyTony', 'Chopper', 'TonyTonyTony', 'ChopperChopeer', 'DoctorChopper@mail.com', '0375937845', '2021-08-03 06:40:00'),
(21, 'Nico', 'Robin', 'NicoRobin', 'RobinNico1234', 'RobinRobin@gmail.com', '0475937593', '2021-08-04 16:56:54'),
(22, 'Hamming', 'Brook', 'Yohohohohooo', 'hohohoho_yo', 'BrookYohoho@mail.kmutt.ac.th', '0586938596', '2021-08-05 03:05:03'),
(23, 'Gold D.', 'Roger', 'RogerD_roger', 'GoldDGoldD', 'DRoger@mail.com', '0586938569', '2021-08-06 05:00:01'),
(24, 'Silvers', ' Rayleigh', 'RRayleigh', 'Silver_Rey', 'SReyleigh@gmail.com', '0576947859', '2021-08-06 16:12:54'),
(25, 'Edward', 'Newgate', 'WhiteBeard01', 'Edward1234', 'EdWard@whitemail.com', '0585693859', '2021-08-06 22:21:01'),
(26, 'Portgas D.', 'Ace', 'ACE_ACE', 'PortgasD_ACE', 'Ace_D@gmail.com', '0586949586', '2021-08-07 15:33:54'),
(27, 'Diamond', 'Jozu', 'JDaimond', 'JozuJoz_123', 'DJozu@gmail,com', '0576839104', '2021-08-07 16:57:54'),
(28, ' Benn', 'Beckman', 'Benn004', 'Bbeckman624', 'Bbeckman@mail.com', '0576899294', '2021-08-09 05:46:00'),
(29, 'Lucky', 'Roux', 'LuckyLuck', 'RouxRoux253', 'Rlucky_343@mail,com', '0683019578', '2021-08-09 08:32:41'),
(30, ' Sharotto', 'Rinrin', 'Rinrinrinrin', 'SharottoRin724', 'Rinrinrin@hotmail.com', '0195738295', '2021-08-09 09:32:14'),
(31, 'Marshall D.', 'Teach', 'Blackbeard444', 'TeachDteach', 'MarshallTeach@blackmail.com', '0475919475', '2021-08-09 21:21:23'),
(32, 'Kozuki', 'Oden', 'KozukiOden', 'OdeneatOden', 'Oden_nishoro@mail.com', '0586939486', '2021-08-10 08:00:12'),
(33, 'Sam', 'Nara', 'Sam123', 'Sam12345', 'Sam123@gmail.com', '0850981441', '2021-06-06 07:48:47'),
(34, 'Sam', 'Nara', 'Sam123', '12345', 'Sam123@gmail.com', '0850981441', '2021-06-06 07:50:49'),
(35, 'Sky', 'Katana', 'Sky1234', '12345', 'Sky@gmail.com', '0981231551', '2021-06-06 08:00:05'),
(36, 'Sam', 'Sky', 'SamSky123', '1234', 'SamSky@gmail.com', '0981231551', '2021-06-06 08:03:53'),
(37, 'samsu', 'Jerry', 'sam12', 'Tom1234', 'Tom1231S@gmail.com', '0980761441', '2021-06-06 15:18:15'),
(38, 'Bill', 'Musk', 'Bill123', 'Bill1234', 'Bill@gmail.com', '0981651441', '2021-06-06 08:14:07'),
(39, 'Tim', 'Cook', 'Tim123', 'Tim12345', 'Tim123@gmail.com', '0861511661', '2021-06-07 01:05:03'),
(41, 'Tom', 'Jerry', 'Tom1234', 'Tom12345', 'Tom@gmail.com', '0861425144', '2021-06-06 18:12:18');

-- --------------------------------------------------------

--
-- Table structure for table `PaymentInfo`
--

CREATE TABLE `PaymentInfo` (
  `PaymentID` int(11) NOT NULL,
  `BookingID` int(11) NOT NULL,
  `PaymentDate` datetime NOT NULL DEFAULT current_timestamp(),
  `PaymentMethod` varchar(15) NOT NULL,
  `PaymentStatus` varchar(10) NOT NULL,
  `StaffID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `PaymentInfo`
--

INSERT INTO `PaymentInfo` (`PaymentID`, `BookingID`, `PaymentDate`, `PaymentMethod`, `PaymentStatus`, `StaffID`) VALUES
(5, 13, '2021-05-03 13:42:04', 'Credit Card', 'Paid', 7),
(6, 14, '2021-05-03 13:44:51', 'Credit Card', 'Pending', 2),
(7, 15, '2021-05-03 14:14:51', 'Credit', 'Paid', NULL),
(8, 16, '2021-05-03 14:16:21', 'Credit', 'Paid', NULL),
(9, 17, '2021-05-03 14:17:43', 'Credit', 'Paid', NULL),
(11, 19, '2021-05-28 10:09:10', 'Credit', 'Paid', NULL),
(12, 20, '2021-05-28 10:11:25', 'Credit', 'Paid', NULL),
(13, 21, '2021-05-28 14:46:26', 'Credit', 'Paid', NULL),
(14, 23, '2021-06-02 11:22:57', 'Credit', 'Paid', NULL),
(15, 24, '2021-06-02 11:40:57', 'Credit', 'Paid', NULL),
(16, 27, '2021-06-03 18:18:31', 'Credit', 'Paid', NULL),
(19, 32, '2021-06-04 17:29:43', 'Credit', 'Paid', NULL),
(22, 36, '2021-06-06 15:29:42', 'Credit', 'Paid', NULL),
(23, 37, '2021-06-06 15:45:14', 'Credit', 'Paid', NULL),
(24, 38, '2021-06-06 16:42:47', 'Cash', 'Paid', 2),
(26, 40, '2021-06-06 17:22:17', 'Cash', 'Paid', 8),
(27, 41, '2021-06-06 17:38:12', 'Cash', 'Paid', 18),
(29, 42, '2021-06-06 18:20:09', 'Credit Card', 'Pending', 9),
(30, 43, '2021-06-07 01:17:19', 'Credit', 'Paid', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `Room`
--

CREATE TABLE `Room` (
  `RoomID` int(11) NOT NULL,
  `RoomType` varchar(32) NOT NULL,
  `RoomFloor` int(11) NOT NULL,
  `Building` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Room`
--

INSERT INTO `Room` (`RoomID`, `RoomType`, `RoomFloor`, `Building`) VALUES
(1201, 'Standard Double Room', 3, 'Building 4'),
(1202, 'Standard Double Room', 2, 'Building 1'),
(1203, 'Standard Double Room', 1, 'Building 1'),
(1204, 'Standard Double Room', 1, 'Building 1'),
(1205, 'Standard Double Room', 1, 'Building 1'),
(1206, 'Standard Double Room', 1, 'Building 1'),
(1207, 'Standard Double Room', 2, 'Building 1'),
(1208, 'Standard Double Room', 2, 'Building 1'),
(1209, 'Standard Double Room', 2, 'Building 1'),
(1210, 'Standard Double Room', 2, 'Building 1'),
(1301, 'Standard Double Room', 3, 'Building 1'),
(1302, 'Standard Double Room', 3, 'Building 1'),
(1303, 'Standard Double Room', 3, 'Building 1'),
(1304, 'Standard Double Room', 3, 'Building 1'),
(1305, 'Standard Double Room', 3, 'Building 1'),
(1306, 'Standard Double Room', 3, 'Building 1'),
(1307, 'Standard Double Room', 3, 'Building 1'),
(1308, 'Standard Double Room', 3, 'Building 1'),
(1309, 'Standard Double Room', 3, 'Building 1'),
(1310, 'Standard Double Room', 3, 'Building 1'),
(2201, 'Standard Twin Room', 2, 'Building 1'),
(2202, 'Standard Twin Room', 2, 'Building 1'),
(2203, 'Standard Twin Room', 2, 'Building 1'),
(2204, 'Standard Twin Room', 2, 'Building 1'),
(2205, 'Standard Twin Room', 2, 'Building 1'),
(2206, 'Standard Twin Room', 2, 'Building 1'),
(2207, 'Standard Twin Room', 2, 'Building 1'),
(2208, 'Standard Twin Room', 2, 'Building 1'),
(2209, 'Standard Twin Room', 2, 'Building 1'),
(2210, 'Standard Twin Room', 2, 'Building 1'),
(2211, 'Standard Twin Room', 2, 'Building 1'),
(2212, 'Standard Twin Room', 2, 'Building 1'),
(2213, 'Standard Twin Room', 2, 'Building 1'),
(2214, 'Standard Twin Room', 2, 'Building 1'),
(2215, 'Standard Twin Room', 2, 'Building 1'),
(3301, 'Super Deluxe Room', 3, 'Building 2'),
(3302, 'Super Deluxe Room', 3, 'Building 2'),
(3303, 'Super Deluxe Room', 3, 'Building 2'),
(3304, 'Super Deluxe Room', 3, 'Building 2'),
(3305, 'Super Deluxe Room', 3, 'Building 2'),
(3401, 'Super Deluxe Room', 4, 'Building 2'),
(3402, 'Super Deluxe Room', 4, 'Building 2'),
(3403, 'Super Deluxe Room', 4, 'Building 2'),
(3404, 'Super Deluxe Room', 4, 'Building 2'),
(3405, 'Super Deluxe Room', 4, 'Building 2');

-- --------------------------------------------------------

--
-- Table structure for table `RoomBooking`
--

CREATE TABLE `RoomBooking` (
  `RoomID` int(11) NOT NULL,
  `BookingID` int(11) NOT NULL,
  `GuestAmount` int(11) DEFAULT 0,
  `AdditionBed` int(11) DEFAULT 0,
  `BreakFast` int(11) DEFAULT 0,
  `GuestID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `RoomBooking`
--

INSERT INTO `RoomBooking` (`RoomID`, `BookingID`, `GuestAmount`, `AdditionBed`, `BreakFast`, `GuestID`) VALUES
(1201, 21, 0, 0, 0, NULL),
(1201, 23, 0, 0, 0, NULL),
(1201, 26, 5, 1, 5, 33),
(1201, 35, 1, 1, 1, 1),
(1201, 37, 0, 0, 0, NULL),
(1202, 14, 0, 0, 0, NULL),
(1202, 17, 4, 4, 0, 1),
(1202, 21, 0, 0, 0, NULL),
(1202, 23, 0, 0, 0, NULL),
(1202, 26, 1, 0, 6, 33),
(1202, 37, 0, 0, 0, NULL),
(1204, 38, 2, 0, 2, 42),
(1205, 32, 2, 0, 2, 34),
(1206, 15, 0, 0, 0, NULL),
(1206, 17, 4, 2, 0, 1),
(1206, 24, 1, 1, 1, 1),
(1206, 40, 4, 3, 4, 44),
(1207, 14, 1, 1, 0, 1),
(1209, 41, 4, 2, 4, 45),
(1310, 38, 3, 1, 1, 34),
(2201, 32, 2, 0, 2, 34),
(2201, 36, 0, 0, 0, NULL),
(2201, 43, 0, 0, 0, NULL),
(2202, 31, 1, 1, 1, 4),
(2202, 36, 0, 0, 0, NULL),
(2202, 43, 0, 0, 0, NULL),
(2212, 27, 1, 0, 1, 10),
(2214, 16, 1, 1, 1, 4),
(3301, 11, 1, 1, 1, 28),
(3302, 13, 3, 1, 3, 12);

-- --------------------------------------------------------

--
-- Table structure for table `RoomType`
--

CREATE TABLE `RoomType` (
  `RoomType` varchar(32) NOT NULL,
  `RoomDescription` text NOT NULL,
  `RoomPrice` int(6) NOT NULL,
  `MaxGuest` tinyint(4) NOT NULL,
  `BedDetail` text NOT NULL,
  `Area` varchar(10) NOT NULL,
  `Picture` blob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `RoomType`
--

INSERT INTO `RoomType` (`RoomType`, `RoomDescription`, `RoomPrice`, `MaxGuest`, `BedDetail`, `Area`, `Picture`) VALUES
('Standard Double Room', 'Have 1 bathroom and 1 beds and see the sea view and large living room', 1500, 4, 'Double Bed', '25.5 x 12', 0x62226227686d732f7374617469632f696d672f726f6f6d312e6a70672722),
('Standard Twin Room', 'Have 1 bathroom and 2 beds and see the sea view and large living room', 1800, 4, 'Twin bed', '26.5 x 12', 0x622727),
('Super Deluxe Room', 'Have 1 bathroom and 2 beds and see the sea view and large living room', 2300, 4, 'Twin bed', '28.5 x 13', 0x6227625c27625c5c5c27625c5c5c5c5c5c5c276222625c5c5c5c5c5c5c5c5c5c5c5c5c5c5c275c5c5c5c5c5c5c5c5c5c5c5c5c5c5c27225c5c5c5c5c5c5c275c5c5c275c2727);

-- --------------------------------------------------------

--
-- Table structure for table `Service`
--

CREATE TABLE `Service` (
  `ServiceID` int(11) NOT NULL,
  `Service` varchar(32) NOT NULL,
  `ServiceDetails` varchar(255) NOT NULL,
  `Price` double(8,2) NOT NULL,
  `BookingID` int(11) NOT NULL,
  `RoomID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `StaffInfo`
--

CREATE TABLE `StaffInfo` (
  `StaffID` int(11) NOT NULL,
  `FirstName` varchar(32) NOT NULL,
  `LastName` varchar(32) NOT NULL,
  `UserName` varchar(32) NOT NULL,
  `Password` varchar(32) NOT NULL,
  `Email` varchar(32) NOT NULL,
  `PhoneNumber` varchar(10) NOT NULL,
  `Gender` varchar(6) NOT NULL,
  `DOB` date NOT NULL,
  `Address` text NOT NULL,
  `Position` varchar(32) NOT NULL,
  `Salary` double(8,2) NOT NULL,
  `BankAccount` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `StaffInfo`
--

INSERT INTO `StaffInfo` (`StaffID`, `FirstName`, `LastName`, `UserName`, `Password`, `Email`, `PhoneNumber`, `Gender`, `DOB`, `Address`, `Position`, `Salary`, `BankAccount`) VALUES
(1, 'Chayaphon', 'Bunyakan', 'Chayaphon1234', 'password', 'sample@gmail.com', '0851234567', 'Female', '2000-04-06', '67 Soi sumaree Hatyai songkhal 90110 Thailand', 'Manager', 200000.00, '4567891234'),
(2, 'Tomioka', 'Giyu', 'Giyu1234', 'Tomioka1234', 'Giyu@gmail.com', '0942471331', 'Male', '2000-12-12', 'Tokyo', 'Manager', 150000.00, '4567891234'),
(3, 'Kanao', 'Tsuyuri', 'Kanao', 'Kamado', 'Kanao@gmail.com', '0987456321', 'Female', '2000-02-23', 'Tokyo japan', 'Staff', 50000.00, '123456'),
(7, 'Conan', 'Edogawa', 'Conan_1234', 'Edogawa4567', 'Conan_Edogawa@gmail.com', '0985674123', 'Male', '1988-09-17', '110 Sirithorn Bangkok 10700', 'Chef', 60000.00, '4183456198'),
(8, ' Amy', 'Yeager', ' Amy_Y1', ' Yeager1234', ' Amy_Y1234@gmail.com', '0876985543', 'Female', '1988-09-17', '110 Sirithorn Bangkok 10700', 'Chef', 60000.00, '4183456198'),
(9, 'Rachel', 'Moore', 'Mori_run', 'Run_912', 'Mori_run@gmail.com', '0945567213', 'Female', '1989-09-12', '100 Sirithorn soi4 Bangkok 10700', 'Cleaning staff', 22000.00, '4176543219'),
(10, 'Richard', 'Moore', 'Mori_Kogoro', 'Kogoro_sleep', 'Mori_Kogoro@gmail.com', '0871657234', 'Male', '1980-06-21', '100 Sirithorn soi4 Bangkok 10700', 'Security guard', 20000.00, '4181123125'),
(11, 'Kudo', 'Jimmy', 'Kudo1234', 'Shinichi', 'Kudo_shinichi@gmail.com', '0807786345', 'Male', '1988-04-04', '109 Sirithorn soi8 Bangkok 10700', 'Room service', 29000.00, '4175674329'),
(12, 'Heiji', 'Hattori', 'Heiji_H', 'Heiji1234', 'Hattori_H@gmail.com', '0876124453', 'Male', '1988-02-28', '109 Prachautid 45 Bangkok 10140', 'Room service', 29000.00, '4176785124'),
(13, 'Kazuha', 'Toyama', 'Toyama_K', 'Toyama_12', 'Toyama_kazuha@gmail.com', '0861237456', 'Female', '1988-09-02', '110 Prachautid 45 Bangkok 10140', 'Cleaning staff', 20000.00, '4189085642'),
(14, 'Aoko', ' Nakamori', 'Aoko_mori', 'Aoko1234', 'Nakamori@gmail.com', '0981762365', 'Female', '1986-07-26', 'Cosmo Prachautid 45 Bangkok 10140', 'Reception', 25000.00, '4198126784'),
(15, 'Kaitou', 'Kid', 'Kid_kaito', 'Kid1412', 'Kid1412@gmail.com', '0907756125', 'Male', '1986-01-11', 'Cosmohome Prachautid 45 Bangkok 10140', 'Staff', 50000.00, '4198879063'),
(16, 'Juzo', 'Megure', 'Megure_J', 'Megure1234', 'Juzo_Megure@gmail.com', '0876615823', 'Male', '1979-03-15', 'Mansion Prachautid 45 Bangkok 10140', 'Security guard', 20000.00, '4163224419'),
(17, 'Kaito', 'Kuroba', 'Kuroba_kaito', 'Kurobakid', 'Kuroba_kaito@gmail.com', '0907750978', 'Male', '1989-08-19', 'Cosmo Prachautid 44 Bangkok 10140', 'Accountant', 22000.00, '4180657783'),
(18, 'Eri', 'Kisaki', 'Kisaki_1', 'Kisaki1234', 'Kisaki@gmail.com', '0974561121', 'Female', '1980-05-07', 'Cosmo mansion Prachautid 45 Bangkok 10140', 'Manager', 90000.00, '4171145236'),
(19, 'Masumi', 'Sera', 'Sera_1', 'Seramasumi123', 'Masumi_S@gmail.com', '0921123476', 'Female', '1991-10-12', 'Mansion Prachautid 40 Bangkok 10140', 'Reception', 30000.00, '4129088125'),
(20, 'Miwako', 'Sato', 'Sato_09', 'Sato1123', 'Miwako_S@gmail.com', '0990654432', 'Female', '1982-11-05', 'Condo Prachautid 41 Bangkok 10140', 'Manager', 90000.00, '4113342156'),
(21, 'Mitsuhiko', 'Tsuburaya', 'Tsuburaya11', 'Tsuburaya0908', 'Mitsuhiko@gmail.com', '0842349971', 'Male', '1990-12-25', 'Condo Prachautid 35 Bangkok 10140', 'Staff', 200000.00, '4124536897'),
(22, 'Hiroshi', 'Agasa', 'Agasa12', 'Agasa_1234', 'Hiroshi1121@gmail.com', '0813235432', 'Male', '1985-03-18', 'Prachautid 39 Bangkok 10140', 'Chef', 65000.00, '4145126548'),
(23, 'Ginzo', 'Nakamori', 'Nakamori01', 'Nakamori1234', 'Nakamori@gmail.com', '0819786123', 'Male', '1983-07-13', 'Prachautid 39 Bangkok 10140', 'Security guard', 30000.00, '4146547891'),
(24, 'Kazunobu', 'Chiba', 'Kazunobu21', 'Kazunobu14532', 'Kazunobu_chiba@gmail.com', '0851532465', 'Male', '1987-09-24', 'Mansion Prachautid 39 Bangkok 10140', 'Security guard', 30000.00, '4146541123'),
(25, 'Eisuke', 'Hondou', 'Hondou21', 'Hondou123', 'Hondou_E@gmail.com', '0851122435', 'Male', '1989-02-20', 'Mansion Prachautid 34 Bangkok 10140', 'Reception', 25000.00, '4171234786'),
(26, 'Elena', 'Miyano', 'Miyano', 'Miyano11234', 'Miyano_E@gmail.com', '0812234558', 'Female', '1986-09-26', 'Prachautid 33 Bangkok 10140', 'Accountant', 23000.00, '4121342546'),
(27, 'Mary', 'Sera', 'Sera_Mary', 'Mary_11234', 'Sera_Mary@gmail.com', '0997651234', 'Female', '1981-01-02', 'Condo Prachautid 46 Bangkok 10140', 'Room service', 40000.00, '4134156738'),
(28, 'Maria', 'Higashio', 'Higashio_M', 'Higashio8796', 'Higashio@gmail.com', '0991122435', 'Female', '1981-04-09', 'Condo Prachautid 46 Bangkok 10140', 'Room service', 35000.00, '4191231234'),
(29, 'Midori', 'Kuriyama', 'Kuriyama_M', 'Kuriyama_0128', 'Kuriyama@gmail.com', '0921543778', 'Female', '1982-05-19', 'Condo Prachautid 47 Bangkok 10140', 'Room service', 35000.00, '4196578432'),
(30, 'Midori', 'Megure', 'Megure12', 'Megure5512', 'Megure@gmail.com', '0912345765', 'Female', '1983-08-29', 'Mansion Prachautid 47 Bangkok 10140', 'Cleaning staff', 35000.00, '4196223412'),
(31, 'Minerva', 'Glass', 'Glass_mi', 'Glass67134', 'Glass_mi@gmail.com', '0912390987', 'Female', '1983-10-20', 'Mansion Prachautid 45 Bangkok 10140', 'Cleaning staff', 32000.00, '4196778952'),
(32, 'Genta', 'Kojima', 'Kojima77', 'Kojima123456', 'Kojima_gen@gmail.com', '0968975332', 'Male', '1989-11-01', 'Mansion Prachautid 45 Bangkok 10140', 'Cleaning staff', 30000.00, '4131245561'),
(33, 'Goro', 'Otaki', 'Otaki07', 'Otaki090412', 'Otaki_12@gmail.com', '0963322154', 'Male', '1989-11-01', 'Mansion Prachautid 46 Bangkok 10140', 'Chef', 50000.00, '4213456712'),
(34, 'Hideo', 'Akagi', 'Akagi_1009', 'Akagi_Hi12', 'Akagi@gmail.com', '0921345678', 'Male', '1988-10-05', 'Mansion Prachautid 46 Bangkok 10140', 'Chef', 50000.00, '4215541678'),
(35, 'Hidemi', 'Hondou', 'Hondou_108', 'Hondou714', 'Hondou@gmail.com', '0876651475', 'Female', '1988-11-05', 'Cosmo mansion Prachautid 45 Bangkok 10140', 'Staff', 45000.00, '4112367839'),
(36, 'Keiko', 'Momoi', 'Momoi_K', 'Momoi8901', 'Momoi_kei@gmail.com', '0854441876', 'Female', '1988-11-22', 'Cosmo Prachautid 45 Bangkok 10140', 'Staff', 43000.00, '4112367709'),
(37, 'Azusa', 'Enomoto', 'Enomoto_007', 'Enomoto1azusa', 'Enomoto_A@gmail.com', '0811123556', 'Female', '1990-05-10', 'Condo Prachautid 47 Bangkok 10140', 'Accountant', 23000.00, '4234156789'),
(38, 'Kansuke', 'Yamato', 'Yamato_907', 'Yamato51476', 'Yamato_A@gmail.com', '0810987123', 'Male', '1980-09-13', 'Mansion Prachautid 47 Bangkok 10140', 'Accountant', 26000.00, '4230087789');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Booking`
--
ALTER TABLE `Booking`
  ADD PRIMARY KEY (`BookingID`),
  ADD KEY `booking_ibfk_1` (`UserID`),
  ADD KEY `booking_ibfk_2` (`DiscountCode`);

--
-- Indexes for table `Discount`
--
ALTER TABLE `Discount`
  ADD PRIMARY KEY (`DiscountCode`);

--
-- Indexes for table `GuestInfo`
--
ALTER TABLE `GuestInfo`
  ADD PRIMARY KEY (`GuestID`);

--
-- Indexes for table `MemberInfo`
--
ALTER TABLE `MemberInfo`
  ADD PRIMARY KEY (`UserID`);

--
-- Indexes for table `PaymentInfo`
--
ALTER TABLE `PaymentInfo`
  ADD PRIMARY KEY (`PaymentID`),
  ADD KEY `paymentinfo_ibfk_1` (`StaffID`),
  ADD KEY `paymentinfo_ibfk_2` (`BookingID`);

--
-- Indexes for table `Room`
--
ALTER TABLE `Room`
  ADD PRIMARY KEY (`RoomID`),
  ADD KEY `room_ibfk_1` (`RoomType`);

--
-- Indexes for table `RoomBooking`
--
ALTER TABLE `RoomBooking`
  ADD PRIMARY KEY (`RoomID`,`BookingID`),
  ADD KEY `roombooking_ibfk_1` (`GuestID`),
  ADD KEY `roombooking_ibfk_2` (`BookingID`),
  ADD KEY `roombooking_ibfk_3` (`RoomID`);

--
-- Indexes for table `RoomType`
--
ALTER TABLE `RoomType`
  ADD PRIMARY KEY (`RoomType`);

--
-- Indexes for table `Service`
--
ALTER TABLE `Service`
  ADD PRIMARY KEY (`ServiceID`),
  ADD KEY `service_ibfk_1` (`RoomID`),
  ADD KEY `service_ibfk_2` (`BookingID`);

--
-- Indexes for table `StaffInfo`
--
ALTER TABLE `StaffInfo`
  ADD PRIMARY KEY (`StaffID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Booking`
--
ALTER TABLE `Booking`
  MODIFY `BookingID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `GuestInfo`
--
ALTER TABLE `GuestInfo`
  MODIFY `GuestID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `MemberInfo`
--
ALTER TABLE `MemberInfo`
  MODIFY `UserID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;

--
-- AUTO_INCREMENT for table `PaymentInfo`
--
ALTER TABLE `PaymentInfo`
  MODIFY `PaymentID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `Service`
--
ALTER TABLE `Service`
  MODIFY `ServiceID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `StaffInfo`
--
ALTER TABLE `StaffInfo`
  MODIFY `StaffID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Booking`
--
ALTER TABLE `Booking`
  ADD CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `MemberInfo` (`UserID`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `booking_ibfk_2` FOREIGN KEY (`DiscountCode`) REFERENCES `Discount` (`DiscountCode`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `PaymentInfo`
--
ALTER TABLE `PaymentInfo`
  ADD CONSTRAINT `paymentinfo_ibfk_1` FOREIGN KEY (`StaffID`) REFERENCES `StaffInfo` (`StaffID`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `paymentinfo_ibfk_2` FOREIGN KEY (`BookingID`) REFERENCES `Booking` (`BookingID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Room`
--
ALTER TABLE `Room`
  ADD CONSTRAINT `room_ibfk_1` FOREIGN KEY (`RoomType`) REFERENCES `RoomType` (`RoomType`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `RoomBooking`
--
ALTER TABLE `RoomBooking`
  ADD CONSTRAINT `roombooking_ibfk_1` FOREIGN KEY (`GuestID`) REFERENCES `GuestInfo` (`GuestID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `roombooking_ibfk_2` FOREIGN KEY (`BookingID`) REFERENCES `Booking` (`BookingID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `roombooking_ibfk_3` FOREIGN KEY (`RoomID`) REFERENCES `Room` (`RoomID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `Service`
--
ALTER TABLE `Service`
  ADD CONSTRAINT `service_ibfk_1` FOREIGN KEY (`RoomID`) REFERENCES `RoomBooking` (`RoomID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `service_ibfk_2` FOREIGN KEY (`BookingID`) REFERENCES `RoomBooking` (`BookingID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
