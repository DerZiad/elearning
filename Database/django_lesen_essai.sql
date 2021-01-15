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
-- Table structure for table `lesen_essai`
--

DROP TABLE IF EXISTS `lesen_essai`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lesen_essai` (
  `id` int NOT NULL AUTO_INCREMENT,
  `choix` varchar(50) NOT NULL,
  `numf_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Lesen_essai_numf_id_09a1e8eb_fk_Lesen_ubung_id` (`numf_id`),
  CONSTRAINT `Lesen_essai_numf_id_09a1e8eb_fk_Lesen_ubung_id` FOREIGN KEY (`numf_id`) REFERENCES `lesen_ubung` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lesen_essai`
--

LOCK TABLES `lesen_essai` WRITE;
/*!40000 ALTER TABLE `lesen_essai` DISABLE KEYS */;
INSERT INTO `lesen_essai` VALUES (2,'aus Deutschland',1),(3,'aus Freiburg',1),(4,'13',2),(5,'14',2),(7,'Bremen',3),(8,'Paris',3),(10,'Sie hat einen deutschen Freund',4),(12,'Sie mag die deutsche Sprache',4),(14,'zwölf Jahre',5),(15,'vierzehn Jahre',5),(16,'in der Schule',6),(17,'im Kino',6),(19,'Chemie',7),(20,'Physik',7),(22,'Sie kocht das Mittagessen.',8),(24,'Sie schläft lange.',8);
/*!40000 ALTER TABLE `lesen_essai` ENABLE KEYS */;
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
