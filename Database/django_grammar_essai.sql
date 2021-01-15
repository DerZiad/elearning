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
-- Table structure for table `grammar_essai`
--

DROP TABLE IF EXISTS `grammar_essai`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grammar_essai` (
  `id` int NOT NULL AUTO_INCREMENT,
  `choix` varchar(15) NOT NULL,
  `numf_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Grammar_essai_numf_id_1169ab50_fk_Grammar_ubung_id` (`numf_id`),
  CONSTRAINT `Grammar_essai_numf_id_1169ab50_fk_Grammar_ubung_id` FOREIGN KEY (`numf_id`) REFERENCES `grammar_ubung` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=114 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grammar_essai`
--

LOCK TABLES `grammar_essai` WRITE;
/*!40000 ALTER TABLE `grammar_essai` DISABLE KEYS */;
INSERT INTO `grammar_essai` VALUES (1,'was',1),(2,'wie',1),(3,'wo',1),(4,'wer',2),(5,'warum',2),(6,'wo',2),(7,'wie',3),(8,'was',3),(9,'wo',3),(10,'warum',4),(11,'was',4),(12,'wie',4),(13,'wohin',5),(14,'warum',5),(15,'was',5),(16,'Warum',6),(17,'Wie',6),(18,'Was',6),(19,'wer',7),(20,'warum',7),(21,'wie',7),(22,'was',8),(23,'wo',8),(24,'wer',8),(25,'warum',9),(26,'wohin',9),(27,'woher',9),(28,'wie',10),(29,'wer',10),(30,'was',10),(31,'warum',11),(32,'wo',11),(33,'wann',11),(34,'wer',12),(35,'wo',12),(36,'wann',12),(37,'gut',13),(38,'stark',13),(39,'traurig',13),(40,'glucklig',14),(41,'dick',14),(42,'teuer',14),(43,'treu',15),(44,'warm',15),(45,'heiss',15),(46,'trocken',16),(47,'schlecht',16),(49,'gesund',17),(50,'krank',17),(51,'klein',16),(52,'sauber',17),(53,'gross',18),(54,'hoch',18),(55,'warm',18),(56,'schmutzig',19),(57,'krank',19),(58,'schnell',19),(59,'sauber',20),(60,'hungirg',20),(61,'klein',20),(62,'traurig',20),(63,'sauber',21),(64,'billig',21),(65,'gut',21),(66,'reich',22),(67,'krank',22),(68,'arm',22),(69,'gesund',22),(70,'breit',23),(71,'schmal',23),(72,'alt',23),(73,'dunn',24),(74,'kalt',24),(75,'tbomke',24),(76,'das',25),(77,'die',25),(78,'der',26),(79,'das',26),(80,'der',27),(81,'die',27),(82,'das',28),(83,'die',28),(84,'der',29),(85,'das',29),(86,'der',30),(87,'das',30),(88,'das',31),(89,'die',31),(90,'das',32),(91,'der',32),(92,'die',33),(93,'das',33),(94,'die',34),(95,'der',34),(96,'der',35),(97,'das',35),(98,'die',36),(99,'der',36),(100,'eine',37),(101,'ein',38),(102,'eine',39),(103,'eine',40),(104,'eine',41),(105,'ein',42),(106,'eine',34),(107,'ein',44),(108,'eine',36),(109,'eine',46),(110,'eine',47),(111,'ein',48),(112,'eine',43),(113,'eine',45);
/*!40000 ALTER TABLE `grammar_essai` ENABLE KEYS */;
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
