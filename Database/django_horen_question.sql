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
-- Table structure for table `horen_question`
--

DROP TABLE IF EXISTS `horen_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `horen_question` (
  `id` int NOT NULL AUTO_INCREMENT,
  `quest` varchar(150) NOT NULL,
  `reponse` varchar(150) NOT NULL,
  `audio_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `audio_id` (`audio_id`),
  CONSTRAINT `Horen_question_audio_id_a1c21098_fk_Horen_track_id` FOREIGN KEY (`audio_id`) REFERENCES `horen_track` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `horen_question`
--

LOCK TABLES `horen_question` WRITE;
/*!40000 ALTER TABLE `horen_question` DISABLE KEYS */;
INSERT INTO `horen_question` VALUES (1,'Wann soll Frau Krause anrufen?','Vor 13 Uhr.',1),(2,'Was möchte Nina heute Abenda machen?','Einen Film sehen.',2),(3,'Was soll Sarah mitbringen?','Ein Wörterbuch.',3),(4,'Wo wollen sich die Frauena mit Sabine treffen?','Beim Konzert.',4),(5,'Wann will Herr Heinzea Frau Solms treffen?','Um 12 Uhr.',7),(6,'Wann kommt Frau Gruber wieder ins Büro','Am Mittwoch',8),(7,'Wohin gehen die Leute','Ins Cafe',9),(8,'Wann koööt der Zug in München an','Um 14,45 Uhr.',10),(9,'Wie viel kostet eine Kinokarte','8 Euro',11),(10,'Was macht Emil zum Abendessen','Suppe',12);
/*!40000 ALTER TABLE `horen_question` ENABLE KEYS */;
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
