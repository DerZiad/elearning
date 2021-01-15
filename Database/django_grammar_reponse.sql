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
-- Table structure for table `grammar_reponse`
--

DROP TABLE IF EXISTS `grammar_reponse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grammar_reponse` (
  `id` int NOT NULL AUTO_INCREMENT,
  `valide` tinyint(1) NOT NULL,
  `pers_id` int NOT NULL,
  `ubung_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ubung_id` (`ubung_id`),
  KEY `Grammar_reponse_pers_id_1f082015_fk_Auth_personne_id` (`pers_id`),
  CONSTRAINT `Grammar_reponse_pers_id_1f082015_fk_Auth_personne_id` FOREIGN KEY (`pers_id`) REFERENCES `auth_personne` (`id`),
  CONSTRAINT `Grammar_reponse_ubung_id_3fa28190_fk_Grammar_ubung_id` FOREIGN KEY (`ubung_id`) REFERENCES `grammar_ubung` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grammar_reponse`
--

LOCK TABLES `grammar_reponse` WRITE;
/*!40000 ALTER TABLE `grammar_reponse` DISABLE KEYS */;
INSERT INTO `grammar_reponse` VALUES (68,1,4,1),(69,1,4,2),(70,1,4,3);
/*!40000 ALTER TABLE `grammar_reponse` ENABLE KEYS */;
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
