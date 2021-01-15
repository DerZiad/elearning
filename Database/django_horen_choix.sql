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
-- Table structure for table `horen_choix`
--

DROP TABLE IF EXISTS `horen_choix`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `horen_choix` (
  `id` int NOT NULL AUTO_INCREMENT,
  `choix` varchar(150) NOT NULL,
  `question_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Horen_choix_question_id_7d7ce3a8_fk_Horen_question_id` (`question_id`),
  CONSTRAINT `Horen_choix_question_id_7d7ce3a8_fk_Horen_question_id` FOREIGN KEY (`question_id`) REFERENCES `horen_question` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `horen_choix`
--

LOCK TABLES `horen_choix` WRITE;
/*!40000 ALTER TABLE `horen_choix` DISABLE KEYS */;
INSERT INTO `horen_choix` VALUES (1,'Am Montag',6),(2,'Ins Restaurant',6),(3,'Am Dienstag',2),(4,'In den Supermarkt',7),(5,'Um 14,25 Uhr',8),(6,'Um 14,35 Uhr',8),(7,'9 Euro',9),(8,'11 Euro',9),(9,'Pizza',10),(10,'Salat',10),(11,'Vor 11 Uhr',1),(12,'Vor 2 Uhr',1),(13,'Zu Hause',2),(14,'Kilos maticha',3),(15,'Orangensaft',3),(16,'Beim Park',4),(17,'Neben dem Turm',4),(18,'Um 7 Uhr.',5),(19,'Um 2 Uhr.',5);
/*!40000 ALTER TABLE `horen_choix` ENABLE KEYS */;
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
