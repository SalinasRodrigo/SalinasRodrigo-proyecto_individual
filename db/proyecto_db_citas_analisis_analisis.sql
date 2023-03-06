CREATE DATABASE  IF NOT EXISTS `proyecto_db` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `proyecto_db`;
-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: proyecto_db
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
-- Table structure for table `citas_analisis_analisis`
--

DROP TABLE IF EXISTS `citas_analisis_analisis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `citas_analisis_analisis` (
  `id` int NOT NULL AUTO_INCREMENT,
  `analisis_id` int NOT NULL,
  `cita_analisis_id` int NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_cita_analisis_analisis_analisis1_idx` (`analisis_id`),
  KEY `fk_cita_analisis_analisis_cita_analisis1_idx` (`cita_analisis_id`),
  CONSTRAINT `fk_cita_analisis_analisis_analisis1` FOREIGN KEY (`analisis_id`) REFERENCES `analisis` (`id`),
  CONSTRAINT `fk_cita_analisis_analisis_cita_analisis1` FOREIGN KEY (`cita_analisis_id`) REFERENCES `citas_analisis` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `citas_analisis_analisis`
--

LOCK TABLES `citas_analisis_analisis` WRITE;
/*!40000 ALTER TABLE `citas_analisis_analisis` DISABLE KEYS */;
INSERT INTO `citas_analisis_analisis` VALUES (30,1,14,'2023-03-05 21:14:54','2023-03-05 21:14:54'),(31,2,14,'2023-03-05 21:14:54','2023-03-05 21:14:54'),(32,5,14,'2023-03-05 21:14:54','2023-03-05 21:14:54');
/*!40000 ALTER TABLE `citas_analisis_analisis` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-05 21:50:18
