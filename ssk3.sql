-- MySQL dump 10.16  Distrib 10.2.9-MariaDB, for osx10.11 (x86_64)
--
-- Host: localhost    Database: ssk2
-- ------------------------------------------------------
-- Server version	10.2.9-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `appointment`
--

DROP TABLE IF EXISTS `appointment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `appointment` (
  `aid` varchar(20) NOT NULL,
  `pid` varchar(30) DEFAULT NULL,
  `sid` varchar(30) DEFAULT NULL,
  `timing` datetime DEFAULT NULL,
  `status` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`aid`),
  KEY `pid` (`pid`),
  KEY `sid` (`sid`),
  CONSTRAINT `appointment_ibfk_1` FOREIGN KEY (`pid`) REFERENCES `patient` (`pid`),
  CONSTRAINT `appointment_ibfk_2` FOREIGN KEY (`sid`) REFERENCES `specialist` (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointment`
--

LOCK TABLES `appointment` WRITE;
/*!40000 ALTER TABLE `appointment` DISABLE KEYS */;
INSERT INTO `appointment` VALUES ('1234','20170404','54678234','2018-03-24 03:45:00','approved'),('1235','20170409','54679876','2018-07-12 02:30:00','pending'),('1236','20170409','54887777','2018-06-15 02:30:00','done'),('1237','20170476','54887777','2018-07-15 02:30:00','pending'),('1238','20180202','54889976','2018-07-20 05:00:00','approved');
/*!40000 ALTER TABLE `appointment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `patient` (
  `pid` varchar(30) NOT NULL,
  `pname` varchar(30) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `parent_name` varchar(30) DEFAULT NULL,
  `phno` varchar(30) DEFAULT NULL,
  `address` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient`
--

LOCK TABLES `patient` WRITE;
/*!40000 ALTER TABLE `patient` DISABLE KEYS */;
INSERT INTO `patient` VALUES ('20170404','Abdul Kumar','2002-04-05','Faizal Kumar','8928765445','2nd cross,RR nagar,Banglore'),('20170409','Lakskmi Shetty','2011-12-04','Niranjan shetty','8912345678','6th cross,Jaynagar,Mysore'),('20170476','Lakshman Hegde','2009-06-07','Srinath Hegde','8928767898','12nd cross,Kuvampunagar,Mysore'),('20180202','Ram Prasad','2001-09-08','Uttam Prasad','8926589845','1st cross,Jaynagar,Banglore');
/*!40000 ALTER TABLE `patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `specialist`
--

DROP TABLE IF EXISTS `specialist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `specialist` (
  `sid` varchar(30) NOT NULL,
  `sname` varchar(30) DEFAULT NULL,
  `dept_name` varchar(40) DEFAULT NULL,
  `phno` varchar(10) DEFAULT NULL,
  `emailid` varchar(30) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `specialist`
--

LOCK TABLES `specialist` WRITE;
/*!40000 ALTER TABLE `specialist` DISABLE KEYS */;
INSERT INTO `specialist` VALUES ('54678234','Prashanth Kumar','Paediatrics','7569086758','prashanth.kumar@gmail.com','pk'),('54679876','Balkrishna Hedge','Orthopaedics','9900886758','balkrishna.hegde@gmail.com','bh'),('54885467','Shraddha Kapoor','STnA','7799009958','shraddha.kapoor@gmail.com','sk'),('54887000','Pradeep Pai','ENT','7799009958','pradeep.pai@gmail.com','pp'),('54887777','Akhila Bharti','Dentist','9999009958','akhila.bharti@gmail.com','ab'),('54889976','Roopa Prakash','Psycology','9909876758','roopa.prakash@gmail.com','rp');
/*!40000 ALTER TABLE `specialist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unavailability`
--

DROP TABLE IF EXISTS `unavailability`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `unavailability` (
  `sid` varchar(30) DEFAULT NULL,
  `startdate` datetime DEFAULT NULL,
  `enddate` datetime DEFAULT NULL,
  KEY `sid` (`sid`),
  CONSTRAINT `unavailability_ibfk_1` FOREIGN KEY (`sid`) REFERENCES `specialist` (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unavailability`
--

LOCK TABLES `unavailability` WRITE;
/*!40000 ALTER TABLE `unavailability` DISABLE KEYS */;
INSERT INTO `unavailability` VALUES ('54678234','2018-07-28 10:00:00','2018-07-28 09:00:00'),('54679876','2018-07-28 11:00:00','2018-07-16 08:00:00'),('54885467','2018-07-14 04:00:00','2018-07-14 04:00:00'),('54887777','2018-07-14 06:00:00','2018-07-18 05:00:00');
/*!40000 ALTER TABLE `unavailability` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-07-07 22:05:39
