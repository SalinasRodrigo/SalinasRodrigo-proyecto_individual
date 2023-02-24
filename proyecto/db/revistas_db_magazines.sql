CREATE DATABASE  IF NOT EXISTS `revistas_db` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `revistas_db`;
-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: revistas_db
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
-- Table structure for table `magazines`
--

DROP TABLE IF EXISTS `magazines`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `magazines` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `contents` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_magazines_users_idx` (`user_id`),
  CONSTRAINT `fk_magazines_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `magazines`
--

LOCK TABLES `magazines` WRITE;
/*!40000 ALTER TABLE `magazines` DISABLE KEYS */;
INSERT INTO `magazines` VALUES (2,'Lorem Ipsum','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus at semper magna. Nulla pharetra tellus lorem, tincidunt dapibus felis bibendum id. Sed ac eros ut quam tincidunt dignissim non et enim. Etiam aliquet tempus odio at ornare. Donec scelerisque luctus.','2023-02-02 14:09:43','2023-02-02 14:09:43',1),(3,'Lorem Ipsum','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus at semper magna. Nulla pharetra tellus lorem, tincidunt dapibus felis bibendum id. Sed ac eros ut quam tincidunt dignissim non et enim. Etiam aliquet tempus odio at ornare. Donec scelerisque luctus.','2023-02-02 14:09:51','2023-02-02 14:09:51',1),(4,'Lorem Ipsum','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus at semper magna. Nulla pharetra tellus lorem, tincidunt dapibus felis bibendum id. Sed ac eros ut quam tincidunt dignissim non et enim. Etiam aliquet tempus odio at ornare. Donec scelerisque luctus.','2023-02-02 14:12:20','2023-02-02 14:12:20',2),(5,'Lorem Ipsum','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus at semper magna. Nulla pharetra tellus lorem, tincidunt dapibus felis bibendum id. Sed ac eros ut quam tincidunt dignissim non et enim. Etiam aliquet tempus odio at ornare. Donec scelerisque luctus.','2023-02-02 14:45:29','2023-02-02 14:45:29',2),(8,'Lorem Ipsum','Lorem ipsum dolor sit amet, consectetur adipiscing elit. In at mauris at arcu fermentum scelerisque. Nunc hendrerit sapien et tristique volutpat. Etiam venenatis vel ante sit amet consequat. Suspendisse ante nibh, finibus sit amet pharetra tincidunt, maximus eu nulla. In vel congue est. Cras sed magna commodo, rutrum orci et, ultricies erat. Sed ullamcorper turpis et elementum imperdiet. Pellentesque urna ex, luctus at risus vel, porttitor placerat justo. Curabitur augue nisi, facilisis quis auctor ut, faucibus vel ante. Sed vel justo aliquam, mollis lacus vel, ornare sem.\r\n\r\nNam luctus tempus consequat. In congue, sem viverra imperdiet pretium, justo quam accumsan ipsum, ac tincidunt metus sapien ut orci. Vestibulum lorem elit, tempus in libero ac, tincidunt ultrices leo. Vestibulum vel quam nibh. Sed consectetur porttitor mauris, ut pellentesque tellus maximus ac. Maecenas porttitor tincidunt leo, nec pulvinar libero semper sit amet. In malesuada hendrerit accumsan. Pellentesque placerat posuere risus ac gravida. Aenean eu ante vitae felis posuere efficitur. Sed imperdiet orci sit amet lorem luctus dapibus nec eu tortor.','2023-02-02 15:25:03','2023-02-02 15:25:03',3),(9,'Lorem Ipsum','Lorem ipsum dolor sit amet, consectetur adipiscing elit. In at mauris at arcu fermentum scelerisque. Nunc hendrerit sapien et tristique volutpat. Etiam venenatis vel ante sit amet consequat. Suspendisse ante nibh, finibus sit amet pharetra tincidunt, maximus eu nulla. In vel congue est. Cras sed magna commodo, rutrum orci et, ultricies erat. Sed ullamcorper turpis et elementum imperdiet. Pellentesque urna ex, luctus at risus vel, porttitor placerat justo. Curabitur augue nisi, facilisis quis auctor ut, faucibus vel ante. Sed vel justo aliquam, mollis lacus vel, ornare sem.\r\n\r\nNam luctus tempus consequat. In congue, sem viverra imperdiet pretium, justo quam accumsan ipsum, ac tincidunt metus sapien ut orci. Vestibulum lorem elit, tempus in libero ac, tincidunt ultrices leo. Vestibulum vel quam nibh. Sed consectetur porttitor mauris, ut pellentesque tellus maximus ac. Maecenas porttitor tincidunt leo, nec pulvinar libero semper sit amet. In malesuada hendrerit accumsan. Pellentesque placerat posuere risus ac gravida. Aenean eu ante vitae felis posuere efficitur. Sed imperdiet orci sit amet lorem luctus dapibus nec eu tortor.\r\n\r\nCras eu elit eget turpis suscipit consectetur id quis purus. Praesent ac leo eget justo cursus sodales. Suspendisse interdum lectus sit amet elit consectetur, quis consequat ante efficitur. Curabitur vestibulum orci tincidunt, hendrerit augue et, molestie magna. In vel massa ut mauris pharetra luctus nec a elit. Praesent imperdiet, augue non tincidunt commodo, turpis ante pharetra mauris, ac tempor urna tortor fringilla arcu. Nulla ultrices auctor cursus. Curabitur posuere ullamcorper ipsum, sed vehicula sapien volutpat et. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum justo ligula, faucibus vitae nisl ac, sollicitudin maximus sapien. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Cras interdum, felis id convallis sodales, velit quam semper purus, quis viverra purus tortor sit amet massa. Praesent sagittis, ipsum vel tincidunt laoreet, lorem magna varius nunc, non volutpat ante nisi vel lorem. Mauris ut elit arcu. Morbi commodo euismod sodales.','2023-02-02 15:25:14','2023-02-02 15:25:14',3);
/*!40000 ALTER TABLE `magazines` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-02 15:42:32
