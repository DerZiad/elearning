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
-- Table structure for table `schreiben_excercice`
--

DROP TABLE IF EXISTS `schreiben_excercice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `schreiben_excercice` (
  `id` int NOT NULL AUTO_INCREMENT,
  `text` longtext NOT NULL,
  `sujet` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schreiben_excercice`
--

LOCK TABLES `schreiben_excercice` WRITE;
/*!40000 ALTER TABLE `schreiben_excercice` DISABLE KEYS */;
INSERT INTO `schreiben_excercice` VALUES (1,'Sie möchten eine CD im Internet kaufen, aber Sie wissen nicht, wie Sie die Rechnung bezahlen sollen.\r\nSie rufen die Firma an, aber es ist immer besetzt. Jetzt schreiben Sie eine E-Mail.\\n\r\n\r\n       – Fragen Sie: Auf welches Konto sollen Sie das Geld überweisen?\\n\r\n       – Sagen Sie: Sie können auch mit Kreditkarte zahlen oder das Geld bar mit der Post schicken.\\n\r\n\r\nSchreiben Sie zu jedem Punkt ein bis zwei Sätze.\\n','im Internet kaufen'),(2,'Ihr Freund, Michael verstehet viel von Computern. Schreiben Sie eine E v mail an Michael.\r\n\r\n– Sie sollten einen neuen Computer kaufen.\r\n– Bitten Sie Michael : er soll mit Ihnen einkaufen.\r\n– Fragen Sie : Wann hat Michael Zeit?','E-mail an Michael'),(3,'Eine Bekannte, Frau Meyer-Siebeck, hat Sie zu ihrer Geburtstagsparty am Samstag\r\neingeladen. Schreiben Sie an Frau Meyer-Siebeck\r\n\r\n– Sie danken für die Einladung.\r\n– Sie entschuldigen sich: Sie können nicht kommen.\r\n– Was machen Sie am Wochenende?','Einladung zu einer Geburstagparty'),(4,'Ihre Tochter Anna ist krank. Bitte schreiben Sie eine Entschuldigung für die Schule. Annas Lehrerin heißt\r\nFrau Kleinert.\\n\r\n\r\n– Schreiben Sie, dass Ihre Tochter vom 10. Oktober bis 13. Oktober den Unterricht nicht besuchen kann.\\n\r\n– Schreiben Sie, warum Ihre Tochter nicht in die Schule kommen kann: Sie hat Bauchschmerzen und Fieber.\\n\r\n– Fragen Sie nach Annas Hausaufgaben. Welche Hausaufgaben muss Anna machen?\\n\r\nSchreiben Sie zu jedem Punkt ein bis zwei Sätze.\\n','Entschuldigung für die Schule'),(5,'Ihre Freundin Irene will Sie im August besuchen. Schreiben Sie an Irene.\r\n\r\n– Sie müssen im August für Ihre Firma nach Berlin fahren.\r\n– Bitte Sie Ihre Freundin: Sie soll im September kommen.\r\n– Sie haben am 10.9 Geburtstag.','planen mit Ihre Freundin'),(6,'Schreiben Sie eine E-Mail an das Hotel „Kaiser Wilhelm“ in Hamburg.\r\n– Sie brauchen ein Doppelzimmer mit Halbpension.\r\n– Sie bleiben vier Nächte, Ankunft: 05.06 Flughafen Fuhlsbüttel\r\n– Das Hotelauto soll Sie am Flughafen abholen','E-Mail an das Hotel');
/*!40000 ALTER TABLE `schreiben_excercice` ENABLE KEYS */;
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
