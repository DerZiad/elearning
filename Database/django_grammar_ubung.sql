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
-- Table structure for table `grammar_ubung`
--

DROP TABLE IF EXISTS `grammar_ubung`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grammar_ubung` (
  `id` int NOT NULL AUTO_INCREMENT,
  `frage` varchar(200) NOT NULL,
  `losung` varchar(200) NOT NULL,
  `type` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grammar_ubung`
--

LOCK TABLES `grammar_ubung` WRITE;
/*!40000 ALTER TABLE `grammar_ubung` DISABLE KEYS */;
INSERT INTO `grammar_ubung` VALUES (1,'? ist diese Frau? Das ist meine Mutter.','warum','frage'),(2,'? hast du Geburtstag? Am 10. Januar','wann','frage'),(3,'? bist du in Deutschland? Ich möchte Deutsch lernen.','warum','frage'),(4,'? ist mein neues Buch? Es liegt auf dem Tisch.','wo','frage'),(5,'? heißt du? Ich heiße Ayman','wie','frage'),(6,'? wohnst du? Ich wohne in Berlin','Wo','frage'),(7,'? machst du morgen? Ich werde meine Mutter besuchen.','was','frage'),(8,'? alt bist du? Ich bin 18 Jahre alt.','wie','frage'),(9,'? bist du? Ich bin der neue Schüler.','wer','frage'),(10,'? bist du so spät? Ich habe verschlafen.','warum','frage'),(11,'? ist das? Das ist ein Hund.','was','frage'),(12,'? kostet das? Es kostet 10 dh','was','frage'),(13,'dick--\'?\'','dunn','gegen'),(14,'voll--\'?\'','leer','gegen'),(15,'alt--\'?\'','jung','gegen'),(16,'hungrig--\'?\'','satt','gegen'),(17,'jung--\'?\'','alt','gegen'),(18,'schwach --\'?\'','stark','gegen'),(19,'billig --\'?\'','teuer','gegen'),(20,'arm--\'?\'','reich','gegen'),(21,'langsam--\'?\'','schnell','gegen'),(22,'warm --\'?\'','kalt','gegen'),(23,'leicht--\'?\'','schwer','gegen'),(24,'glücklich--\'?\'','traurig','gegen'),(25,'\'?\' Mann','der','ba'),(26,'\'?\' Frau','die','ba'),(27,'\'?\' Kind','das','ba'),(28,'\'?\' Brduer','der','ba'),(29,'\'?\' Schwester','die','ba'),(30,'\'?\' Eltern','die','ba'),(31,'\'?\' Vater','der','ba'),(32,'\'?\' Mutter','die','ba'),(33,'\'?\' Freund','der','ba'),(34,'\'?\' Haus','das','ba'),(35,'\'?\' Wohnung','die','ba'),(36,'\'?\' Auto','das','ba'),(37,'\'?\'-- Mann','ein','ua'),(38,'\'?\'-- Frau','eine','ua'),(39,'\'?\'-- Kind','ein','ua'),(40,'\'?\'-- Junge','ein','ua'),(41,'\'?\'-- Madchen','ein','ua'),(42,'\'?\'-- Freundin','eine','ua'),(43,'\'?\'--  Huas','ein','ua'),(44,'\'?\'-- Wohnung','eine','ua'),(45,'\'?\'-- Auto','ein','ua'),(46,'\'?\'-- Name','ein','ua'),(47,'\'?\'-- Beruf','ein','ua'),(48,'\'?\'-- Arbeit','eine','ua');
/*!40000 ALTER TABLE `grammar_ubung` ENABLE KEYS */;
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
