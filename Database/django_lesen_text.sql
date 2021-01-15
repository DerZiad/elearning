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
-- Table structure for table `lesen_text`
--

DROP TABLE IF EXISTS `lesen_text`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lesen_text` (
  `id` int NOT NULL,
  `title` varchar(50) NOT NULL,
  `text` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lesen_text`
--

LOCK TABLES `lesen_text` WRITE;
/*!40000 ALTER TABLE `lesen_text` DISABLE KEYS */;
INSERT INTO `lesen_text` VALUES (1,'Juliana in Deutschland','Juliana kommt aus Paris. Das ist die Hauptstadt von Frankreich. In diesem Sommer macht sie einen Sprachkurs in Freiburg. Das ist eine Universitätsstadt im Süden von Deutschland.\r\nEs gefällt ihr hier sehr gut. Morgens um neun beginnt der Unterricht, um vierzehn Uhr ist er zu Ende. In ihrer Klasse sind außer Juliana noch 14 weitere Schüler, acht Mädchen und sechs Jungen. Sie kommen alle aus Frankreich, aber nicht aus Paris.\r\nJulianas beste Freundin Marie macht auch gerade einen Sprachkurs, aber in Hamburg, das liegt ganz im Norden von Deutschland.\r\nWenn die beiden ihre Schule beendet haben, wollen sie in Deutschland studieren. Juliana will Tierärztin werden, ihre beste Freundin auch. Aber Maries Eltern sind beide Zahnärzte, deshalb wird Marie wahrscheinlich auch Zahnärztin werden.\r\nJuliana und Marie verbringen insgesamt sechs Wochen in Deutschland. Nach dem Sprachkurs machen sie eine Prüfung.'),(2,'Vorstellung','Mein Name ist Anna. Ich komme aus Österreich und lebe seit drei Jahren in Deutschland. Ich bin 15 Jahre alt und habe zwei Geschwister: Meine Schwester heißt Klara und ist 13 Jahre alt, mein Bruder Michael ist 18 Jahre alt. Wir wohnen mit unseren Eltern in einem Haus in der Nähe von München. Meine Mutter ist Köchin, mein Vater arbeitet in einer Bank.\r\nIch lese gerne und mag Tiere: Wir haben einen Hund, zwei Katzen und im Garten einen Teich mit Goldfischen. Ich gehe auch gerne in die Schule, mein Lieblingsfach ist Mathematik. Physik und Chemie mag ich nicht so gerne.\r\nNach der Schule gehe ich oft mit meinen Freundinnen im Park spazieren, manchmal essen wir ein Eis. Am Samstag gehen wir oft ins Kino. Am Sonntag schlafe ich lange, dann koche ich mit meiner Mutter das Mittagessen. Nach dem Essen gehen wir mit dem Hund am See spazieren. Sonntag ist mein Lieblingstag!');
/*!40000 ALTER TABLE `lesen_text` ENABLE KEYS */;
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
