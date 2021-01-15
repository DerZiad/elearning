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
-- Table structure for table `horen_track`
--

DROP TABLE IF EXISTS `horen_track`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `horen_track` (
  `id` int NOT NULL AUTO_INCREMENT,
  `trackname` varchar(30) NOT NULL,
  `track` varchar(100) NOT NULL,
  `modeltest_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Horen_track_modeltest_id_661c48b3_fk_Horen_modeltest_id` (`modeltest_id`),
  CONSTRAINT `Horen_track_modeltest_id_661c48b3_fk_Horen_modeltest_id` FOREIGN KEY (`modeltest_id`) REFERENCES `horen_modeltest` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `horen_track`
--

LOCK TABLES `horen_track` WRITE;
/*!40000 ALTER TABLE `horen_track` DISABLE KEYS */;
INSERT INTO `horen_track` VALUES (1,'Track1','Track/Track_119.mp3',1),(2,'Track2','Track/Track_013.mp3',1),(3,'Track3','Track/Track_005.mp3',1),(4,'Track4','Track/Track_012.mp3',1),(7,'Track5','Track/Track_015.mp3',1),(8,'Track6','Track/Track_110.mp3',2),(9,'Track7','Track/Track_011.mp3',2),(10,'Track8','Track/Track_112.mp3',2),(11,'Track9','Track/Track_117.mp3',2),(12,'Track10','Track/Track_118.mp3',2);
/*!40000 ALTER TABLE `horen_track` ENABLE KEYS */;
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
