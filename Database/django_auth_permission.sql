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
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add ubung',7,'add_ubung'),(26,'Can change ubung',7,'change_ubung'),(27,'Can delete ubung',7,'delete_ubung'),(28,'Can view ubung',7,'view_ubung'),(29,'Can add reponse',8,'add_reponse'),(30,'Can change reponse',8,'change_reponse'),(31,'Can delete reponse',8,'delete_reponse'),(32,'Can view reponse',8,'view_reponse'),(33,'Can add essai',9,'add_essai'),(34,'Can change essai',9,'change_essai'),(35,'Can delete essai',9,'delete_essai'),(36,'Can view essai',9,'view_essai'),(37,'Can add model test',10,'add_modeltest'),(38,'Can change model test',10,'change_modeltest'),(39,'Can delete model test',10,'delete_modeltest'),(40,'Can view model test',10,'view_modeltest'),(41,'Can add track',11,'add_track'),(42,'Can change track',11,'change_track'),(43,'Can delete track',11,'delete_track'),(44,'Can view track',11,'view_track'),(45,'Can add reponse horen',12,'add_reponsehoren'),(46,'Can change reponse horen',12,'change_reponsehoren'),(47,'Can delete reponse horen',12,'delete_reponsehoren'),(48,'Can view reponse horen',12,'view_reponsehoren'),(49,'Can add question',13,'add_question'),(50,'Can change question',13,'change_question'),(51,'Can delete question',13,'delete_question'),(52,'Can view question',13,'view_question'),(53,'Can add choix',14,'add_choix'),(54,'Can change choix',14,'change_choix'),(55,'Can delete choix',14,'delete_choix'),(56,'Can view choix',14,'view_choix'),(57,'Can add text',15,'add_text'),(58,'Can change text',15,'change_text'),(59,'Can delete text',15,'delete_text'),(60,'Can view text',15,'view_text'),(61,'Can add ubung',16,'add_ubung'),(62,'Can change ubung',16,'change_ubung'),(63,'Can delete ubung',16,'delete_ubung'),(64,'Can view ubung',16,'view_ubung'),(65,'Can add reponse',17,'add_reponse'),(66,'Can change reponse',17,'change_reponse'),(67,'Can delete reponse',17,'delete_reponse'),(68,'Can view reponse',17,'view_reponse'),(69,'Can add essai',18,'add_essai'),(70,'Can change essai',18,'change_essai'),(71,'Can delete essai',18,'delete_essai'),(72,'Can view essai',18,'view_essai'),(73,'Can add excercice',19,'add_excercice'),(74,'Can change excercice',19,'change_excercice'),(75,'Can delete excercice',19,'delete_excercice'),(76,'Can view excercice',19,'view_excercice'),(77,'Can add reponse',20,'add_reponse'),(78,'Can change reponse',20,'change_reponse'),(79,'Can delete reponse',20,'delete_reponse'),(80,'Can view reponse',20,'view_reponse'),(81,'Can add correction',21,'add_correction'),(82,'Can change correction',21,'change_correction'),(83,'Can delete correction',21,'delete_correction'),(84,'Can view correction',21,'view_correction'),(85,'Can add personne',22,'add_personne'),(86,'Can change personne',22,'change_personne'),(87,'Can delete personne',22,'delete_personne'),(88,'Can view personne',22,'view_personne'),(89,'Can add message',23,'add_message'),(90,'Can change message',23,'change_message'),(91,'Can delete message',23,'delete_message'),(92,'Can view message',23,'view_message');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
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
