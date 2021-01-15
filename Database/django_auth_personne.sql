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
-- Table structure for table `auth_personne`
--

DROP TABLE IF EXISTS `auth_personne`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_personne` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(30) NOT NULL,
  `password` varchar(80) NOT NULL,
  `nom` varchar(20) NOT NULL,
  `prenom` varchar(20) NOT NULL,
  `datedenaissance` date NOT NULL,
  `username` varchar(18) NOT NULL,
  `Address` varchar(80) NOT NULL,
  `Sexe` varchar(5) NOT NULL,
  `photo` varchar(255) NOT NULL,
  `valid` tinyint(1) NOT NULL,
  `succes_lesen` int NOT NULL,
  `succes_horen` int NOT NULL,
  `succes_grammar` int NOT NULL,
  `datecreationaccount` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_personne`
--

LOCK TABLES `auth_personne` WRITE;
/*!40000 ALTER TABLE `auth_personne` DISABLE KEYS */;
INSERT INTO `auth_personne` VALUES (1,'rachid.2004cde@outlook.fr','5ea8e4a2ad99c3bd767b6bf4e8d72d5d','Ziad','Bougrine','2002-02-01','smokerzzzz','Marjane 2 imm 89','Homme','pictures/-5980858009431811881.png',1,5,0,2,'2021-01-12'),(2,'aymanabouhali@icloud.com','447a52680d636d9af60709d0dd1472dd','ddddddd',' vhddddddd','2002-10-05','aymoooooooon','sdfs  sbsb','Homme','pictures/user_200_200.jpg',1,7,0,14,'2021-01-12'),(4,'ziadbougrine@gmail.com','2e95965d4485419043739063f2dda5f3','Ziad','Bougrine','2002-01-02','bougrine','Maroc,Meknes,','Homme','pictures/5170540091389977647.png',1,5,1,3,'2021-01-15');
/*!40000 ALTER TABLE `auth_personne` ENABLE KEYS */;
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
