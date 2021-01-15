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
-- Table structure for table `lesen_ubung`
--

DROP TABLE IF EXISTS `lesen_ubung`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lesen_ubung` (
  `id` int NOT NULL AUTO_INCREMENT,
  `frage` varchar(100) NOT NULL,
  `losung` varchar(50) NOT NULL,
  `type` varchar(10) NOT NULL,
  `numtext_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Lesen_ubung_numtext_id_c1d0619a_fk_Lesen_text_id` (`numtext_id`),
  CONSTRAINT `Lesen_ubung_numtext_id_c1d0619a_fk_Lesen_text_id` FOREIGN KEY (`numtext_id`) REFERENCES `lesen_text` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lesen_ubung`
--

LOCK TABLES `lesen_ubung` WRITE;
/*!40000 ALTER TABLE `lesen_ubung` DISABLE KEYS */;
INSERT INTO `lesen_ubung` VALUES (1,'Woher kommt Juliana?','aus Paris','frage',1),(2,'Wie viele Schüler sind in Julianas Sprachkurs?','15','frage',1),(3,'In welcher Stadt macht Marie einen Sprachkurs?','Hamburg','frage',1),(4,'Warum macht Marie einen Sprachkurs?','Sie möchte in Deutschland studieren','frage',1),(5,'Wie alt ist Annas Schwester?','dreizehn Jahre','frage',2),(6,'Wo arbeitet Annas Vater?','in einer Bank','frage',2),(7,'Was ist Annas Lieblingsfach in der Schule?','Mathematik','frage',2),(8,'Was macht Anna nach der Schule?','Sie geht mit ihren Freundinnen spazieren.','frage',2);
/*!40000 ALTER TABLE `lesen_ubung` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-15 19:53:23
