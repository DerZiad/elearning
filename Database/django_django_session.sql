-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: django
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('0yi30y7vx1rha55wur0qfo9rak9fs4u8','.eJxFzkFuwkAMBdC7zDogGAiBrBCrbrhAN8gZ_6ZRMzOVTVQE4u54hKBLv2_L_-ZSjq51nwOxq9yv4Dkf8tTLkGDGdAYj0aBKKcBCP1vO_GLhLZwUkigW7f5PFJciHznGMhKzQNXkSJJDdcRPglaWINIwml_t_et-3xecB-thhUj1LwvbTg3aYk2eeLcLq46bTdNtuq81ttx4rkt9nUKAnkYokmvrN3xnKbB8Qy8UI4lrV_cHTXtUlw:1l0LJe:TZwgzffRqQf5KsGE3HWHH0zSxPMj7C50rgCW7e-O3hM','2021-01-29 09:22:46.694924'),('d62uoq4u27rb1k1e68sq6ll9impgioo4','.eJxVjDsOwjAQBe_iGllZfwMlfc5grb1eHEC2FCcV4u4QKQW0b2beSwTc1hK2npcwk7gIEKffLWJ65LoDumO9NZlaXZc5yl2RB-1yapSf18P9OyjYy7d2oAk8ZTdkpzRjJGZvkzFnz3EYiVRWSVmw1kTnAVgbp4nRMo7GgxfvD-s_N9U:1l00cb:haMUMVYKknTH54RYCpVfqrLx1UrVPcJBJUfzZozlWcE','2021-01-28 11:16:57.706170'),('zgzk76b0k1i2thi4864rprudnaf7pz0w','.eJxNkM1OAzEMhN_F57TabJKymxPixKUvwAW5sbtdsUlQ3FX5Ee9OAqj0Ymm-icfRfELIxCfwaV0WBRxxXsDDx4x0yOtU5sT3U4PbkCMoSHV6eKp2Fa-Ff_XD39PKCM9MnHAWwRS4mv1Gb_qu66u5CpeEsdHD_4rwWyOPOcYmkaiwSCV7LDmoPb8kFtXuocglF2qhPLpx58jawVk9dtbcmbHbmWNPhO5oWuwaAsvzwsIJvLuCUy4N6CuYCsaIBbxRP23UeG21HQbd_pxuO9nmxITvN5V8fQPCBGbn:1l0QND:k1KMjGChF359SYdettaupHFEOquoLvcs0R4nmM1oTlM','2021-01-29 14:46:47.884394'),('zwwx9wa2zmdpkrq06dpckw1h5qauvixb','.eJxVkN1uwyAMhV-l4nqNgBBIejXtZrvZM0QGmyZbAlPc7EfT3n2krTbVd_7OsX3gW4SM9CgOQqq67ZQWdyLlufR4qdK_LXRBu_fhnyKcCCnByAwpUJGbvZJ7LeW2Y2VaEswbhq85XysVhelzo095LuqdAMSFmAthjLzbsWdfMM0wTpdhSODzOsA03o9hyitWoaQpsYD5Iy9YXMY4aLRtJdraYgfRSic7lIjKOH2Oy2sIxP1ETEkc5B8Y8nILjgvMMyxn1MN6GvrtLf243VHihnkIr5Q2AV8gHXMJlk7L6KvNUl1Vrp7LD08PV-_NggF4KNNW1agckpVkdR3BY4yuCcZ0LnrZImrSQTeqaYy3TqlYG1tjhCZCa5xy4ucXwx2SFA:1kzHUz:iHRVG2MewtA0jLQgQBc0icwLtXc9FSFCEPtLi4wiD_w','2021-01-26 11:06:05.792948');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-15 19:53:24
