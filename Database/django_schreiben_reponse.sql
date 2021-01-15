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
-- Table structure for table `schreiben_reponse`
--

DROP TABLE IF EXISTS `schreiben_reponse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `schreiben_reponse` (
  `id` int NOT NULL AUTO_INCREMENT,
  `rep` longtext,
  `legal` tinyint(1) NOT NULL,
  `corrected` tinyint(1) NOT NULL,
  `excercice_id` int NOT NULL,
  `personne_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Schreiben_reponse_excercice_id_375d43b0_fk_Schreiben` (`excercice_id`),
  KEY `Schreiben_reponse_personne_id_09094ece_fk_Auth_personne_id` (`personne_id`),
  CONSTRAINT `Schreiben_reponse_excercice_id_375d43b0_fk_Schreiben` FOREIGN KEY (`excercice_id`) REFERENCES `schreiben_excercice` (`id`),
  CONSTRAINT `Schreiben_reponse_personne_id_09094ece_fk_Auth_personne_id` FOREIGN KEY (`personne_id`) REFERENCES `auth_personne` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schreiben_reponse`
--

LOCK TABLES `schreiben_reponse` WRITE;
/*!40000 ALTER TABLE `schreiben_reponse` DISABLE KEYS */;
INSERT INTO `schreiben_reponse` VALUES (29,'hdwbjfjnirskjydjntdjngggggggggggdhjhkhgggggggggukkkkkkkkkkkkykkkkkkblgiijmiydfkiy;c,g gjl::oimtlkju;,jh,yrtkiyètfrcdk,ccuikcijkjuuytktg,,,gh,kutl;ouruyhdwbjfjnirskjydjntdjngggggggggggdhjhkhgggggggggukkkkkkkkkkkkykkkkkkblgiijmiydfkiy;c,g gjl::oimtlkju;,jh,yrtkiyètfrcdk,ccuikcijkjuuytktg,,,gh,kutl;ouruyhdwbjfjnirskjydjntdjngggggggggggdhjhkhgggggggggukkkkkkkkkkkkykkkkkkblgiijmiydfkiy;c,g gjl::oimtlkju;,jh,yrtkiyètfrcdk,ccuikcijkjuuytktg,,,gh,kutl;ouruyhdwbjfjnirskjydjntdjngggggggggggdhjhkhggggggggg',1,0,3,4),(30,'nsqbdkg,lsr<k;pgtk<nsqbdkg,lsr<k;pgtk<gnrirhhbnVrizuhygnsqbdkg,lsr<k;pgtk<gnrirhhbnVrizuhygnsqbdkg,lsr<k;pgtk<gnrirhhbnVrizuhygnsqbdkg,lsr<k;pgtk<gnrirhhbnVrizuhygnsqbdkg,lsr<k;pgtk<gnrirhhbnVrizuhygvvvvgnrirhhbnVrizuhygnsqbdkg,lsr<k;pgtk<gnrirhhbnVrizuhygnsqbdkg,lsr<k;pgtk<gnrirhhbnVrizuhygnsqbdkg,lsr<k;pgtk<gnrirhhbnVrizuhyg',0,0,2,1),(31,'dsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsqdazadsq',0,0,6,1);
/*!40000 ALTER TABLE `schreiben_reponse` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-15 19:53:25
