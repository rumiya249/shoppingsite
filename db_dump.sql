-- MySQL dump 10.13  Distrib 5.5.59, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: shop_db2
-- ------------------------------------------------------
-- Server version	5.5.59-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add group',4,'add_group'),(11,'Can change group',4,'change_group'),(12,'Can delete group',4,'delete_group'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add file data model',7,'add_filedatamodel'),(20,'Can change file data model',7,'change_filedatamodel'),(21,'Can delete file data model',7,'delete_filedatamodel'),(22,'Can add product',8,'add_product'),(23,'Can change product',8,'change_product'),(24,'Can delete product',8,'delete_product'),(25,'Can add image data model',9,'add_imagedatamodel'),(26,'Can change image data model',9,'change_imagedatamodel'),(27,'Can delete image data model',9,'delete_imagedatamodel'),(28,'Can add user',10,'add_userprofilemodel'),(29,'Can change user',10,'change_userprofilemodel'),(30,'Can delete user',10,'delete_userprofilemodel');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$100000$iTeTsjZg7GYz$B0ak6WWlYFOPawmH2ToglvPxN1k+KCllq4N2nilNwrQ=','2018-02-05 06:39:06',1,'rumiya','','','rr@gmail.com',1,1,'2018-02-05 06:37:54'),(2,'',NULL,0,'','','','',0,1,'2018-02-05 17:50:09'),(4,'',NULL,0,'rr1@gmail.com','test','user','rr1@gmail.com',0,1,'2018-02-05 18:01:42'),(5,'122222222',NULL,0,'sdlfjsdlkf@kldsjfs.com','fdkgldkfs','lsekjfsejk','sdlfjsdlkf@kldsjfs.com',0,1,'2018-02-05 18:06:28'),(6,'pbkdf2_sha256$100000$bwI9nArg4hmW$Dzbwzjkz0fUHYaJTsPHYk4/YLHcAPjqbyNT62m+dwI0=',NULL,0,'rumer@rumer.com','test','rumer','rumer@rumer.com',0,1,'2018-02-05 18:08:14');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(4,'auth','group'),(2,'auth','permission'),(3,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(7,'shopping_site','filedatamodel'),(9,'shopping_site','imagedatamodel'),(8,'shopping_site','product'),(10,'shopping_site','userprofilemodel');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-01-30 18:22:27'),(2,'auth','0001_initial','2018-01-30 18:22:33'),(3,'admin','0001_initial','2018-01-30 18:22:34'),(4,'admin','0002_logentry_remove_auto_add','2018-01-30 18:22:34'),(5,'contenttypes','0002_remove_content_type_name','2018-01-30 18:22:35'),(6,'auth','0002_alter_permission_name_max_length','2018-01-30 18:22:36'),(7,'auth','0003_alter_user_email_max_length','2018-01-30 18:22:36'),(8,'auth','0004_alter_user_username_opts','2018-01-30 18:22:36'),(9,'auth','0005_alter_user_last_login_null','2018-01-30 18:22:38'),(10,'auth','0006_require_contenttypes_0002','2018-01-30 18:22:38'),(11,'auth','0007_alter_validators_add_error_messages','2018-01-30 18:22:38'),(12,'auth','0008_alter_user_username_max_length','2018-01-30 18:22:40'),(13,'auth','0009_alter_user_last_name_max_length','2018-01-30 18:22:41'),(14,'sessions','0001_initial','2018-01-30 18:22:42'),(15,'shopping_site','0001_initial','2018-01-30 18:22:42'),(16,'shopping_site','0002_product_barcode_path','2018-01-31 17:58:51'),(17,'shopping_site','0003_product_barode_id','2018-02-01 07:06:41'),(18,'shopping_site','0004_auto_20180202_0526','2018-02-02 05:26:21'),(19,'shopping_site','0005_auto_20180205_1738','2018-02-05 17:38:11');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('0rii6ffoo75384le3yu6cv070wfbdvk7','NjVjMzY4NmE5ZDEwYjY5NzQzMGM2YmRkY2RhN2I2ZTkyOTdhYzZmYTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMmMxZjg3MzhiZThlYzc5YmJkMjgyNDgyYWU3YjFiZjEwYWYyNjllNSIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2018-02-19 06:39:06');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shopping_site_filedatamodel`
--

DROP TABLE IF EXISTS `shopping_site_filedatamodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shopping_site_filedatamodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_date` datetime NOT NULL,
  `path` varchar(100) NOT NULL,
  `test_fields` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shopping_site_filedatamodel`
--

LOCK TABLES `shopping_site_filedatamodel` WRITE;
/*!40000 ALTER TABLE `shopping_site_filedatamodel` DISABLE KEYS */;
INSERT INTO `shopping_site_filedatamodel` VALUES (1,'2018-01-30 18:28:23','data_files/csv/test_file_jClB4hu.csv',0),(2,'2018-01-30 18:30:06','data_files/csv/test_file_gRn10dB.csv',0),(3,'2018-01-30 18:43:03','data_files/csv/test_file_8XTqf49.csv',0),(4,'2018-02-01 07:24:33','data_files/csv/test_file_Ev7jqeP.csv',0);
/*!40000 ALTER TABLE `shopping_site_filedatamodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shopping_site_imagedatamodel`
--

DROP TABLE IF EXISTS `shopping_site_imagedatamodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shopping_site_imagedatamodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_date` datetime NOT NULL,
  `path` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shopping_site_imagedatamodel`
--

LOCK TABLES `shopping_site_imagedatamodel` WRITE;
/*!40000 ALTER TABLE `shopping_site_imagedatamodel` DISABLE KEYS */;
INSERT INTO `shopping_site_imagedatamodel` VALUES (1,'2018-02-02 05:27:30','data_files/csv/one.jpg'),(2,'2018-02-02 05:30:06','data_files/csv/one_xjJLcvW.jpg'),(3,'2018-02-02 05:33:37','one.jpg'),(4,'2018-02-02 05:35:39','data_files/svg/one_s8XmnlQ.jpg'),(5,'2018-02-02 05:37:58','data_files/svg/two_Tp9uxQm.jpg'),(6,'2018-02-02 05:38:32','data_files/svg/two_PR2JyU9.jpg'),(7,'2018-02-02 06:05:35','data_files/svg/one.jpg');
/*!40000 ALTER TABLE `shopping_site_imagedatamodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shopping_site_product`
--

DROP TABLE IF EXISTS `shopping_site_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shopping_site_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `pub_date` datetime NOT NULL,
  `description` longtext NOT NULL,
  `stock` int(11) NOT NULL,
  `available` tinyint(1) DEFAULT NULL,
  `catagory` varchar(200) NOT NULL,
  `productID` varchar(220) NOT NULL,
  `Barcode_Path` varchar(100) DEFAULT NULL,
  `barode_id` varchar(220) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shopping_site_product`
--

LOCK TABLES `shopping_site_product` WRITE;
/*!40000 ALTER TABLE `shopping_site_product` DISABLE KEYS */;
INSERT INTO `shopping_site_product` VALUES (66,'product1',35.00,'2018-02-01 07:24:33','test_product1',5,0,'googd_product1','000010002','/home/rumiya/workspace/mysite/data_files/svg/product1000010002.svg','100027'),(67,'product2',36.00,'2018-02-01 07:24:33','test_product2',6,0,'googd_product2','000010003','/home/rumiya/workspace/mysite/data_files/svg/product2000010003.svg','100036'),(68,'product3',37.00,'2018-02-01 07:24:33','test_product3',7,0,'googd_product3','000010004','/home/rumiya/workspace/mysite/data_files/svg/product3000010004.svg','100045'),(69,'product4',38.00,'2018-02-01 07:24:33','test_product4',8,0,'googd_product4','000010005','/home/rumiya/workspace/mysite/data_files/svg/product4000010005.svg','100054'),(70,'product5',39.00,'2018-02-01 07:24:34','test_product5',9,0,'googd_product5','000010006','/home/rumiya/workspace/mysite/data_files/svg/product5000010006.svg','100063'),(71,'product6',40.00,'2018-02-01 07:24:34','test_product6',10,0,'googd_product6','000010007','/home/rumiya/workspace/mysite/data_files/svg/product6000010007.svg','100072'),(72,'product7',41.00,'2018-02-01 07:24:34','test_product7',11,0,'googd_product7','000010008','/home/rumiya/workspace/mysite/data_files/svg/product7000010008.svg','100081'),(73,'product8',42.00,'2018-02-01 07:24:34','test_product8',12,0,'googd_product8','000010009','/home/rumiya/workspace/mysite/data_files/svg/product8000010009.svg','100090'),(74,'product9',43.00,'2018-02-01 07:24:34','test_product9',13,0,'googd_product9','000010010','/home/rumiya/workspace/mysite/data_files/svg/product9000010010.svg','100106'),(75,'product10',44.00,'2018-02-01 07:24:34','test_product10',14,0,'googd_product10','000010011','','0'),(76,'product11',45.00,'2018-02-01 07:24:34','test_product11',15,0,'googd_product11','000010012','','0'),(77,'product12',46.00,'2018-02-01 07:24:34','test_product12',16,0,'googd_product12','000010013','','0'),(78,'product13',47.00,'2018-02-01 07:24:34','test_product13',17,0,'googd_product13','000010014','','0'),(79,'product14',48.00,'2018-02-01 07:24:34','test_product14',18,0,'googd_product14','000010015','','0'),(80,'product15',49.00,'2018-02-01 07:24:34','test_product15',19,0,'googd_product15','000010016','','0'),(81,'product16',50.00,'2018-02-01 07:24:34','test_product16',20,0,'googd_product16','000010017','','0'),(82,'product17',51.00,'2018-02-01 07:24:34','test_product17',21,0,'googd_product17','000010018','','0'),(83,'product18',52.00,'2018-02-01 07:24:34','test_product18',22,0,'googd_product18','000010019','','0'),(84,'product19',53.00,'2018-02-01 07:24:34','test_product19',23,0,'googd_product19','000010020','','0'),(85,'product20',54.00,'2018-02-01 07:24:34','test_product20',24,0,'googd_product20','000010021','','0'),(86,'product21',55.00,'2018-02-01 07:24:34','test_product21',25,0,'googd_product21','000010022','','0'),(87,'product22',56.00,'2018-02-01 07:24:34','test_product22',26,0,'googd_product22','000010023','','0'),(88,'product23',57.00,'2018-02-01 07:24:34','test_product23',27,0,'googd_product23','000010024','','0'),(89,'product24',58.00,'2018-02-01 07:24:35','test_product24',28,0,'googd_product24','000010025','','0'),(90,'product25',59.00,'2018-02-01 07:24:35','test_product25',29,0,'googd_product25','000010026','','0'),(91,'product26',60.00,'2018-02-01 07:24:35','test_product26',30,0,'googd_product26','000010027','','0'),(92,'product27',61.00,'2018-02-01 07:24:35','test_product27',31,0,'googd_product27','000010028','','0'),(93,'product28',62.00,'2018-02-01 07:24:35','test_product28',32,0,'googd_product28','000010029','','0'),(94,'product29',63.00,'2018-02-01 07:24:35','test_product29',33,0,'googd_product29','000010030','','0'),(95,'product30',64.00,'2018-02-01 07:24:35','test_product30',34,0,'googd_product30','000010031','','0'),(96,'product31',65.00,'2018-02-01 07:24:35','test_product31',35,0,'googd_product31','000010032','','0');
/*!40000 ALTER TABLE `shopping_site_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shopping_site_userprofilemodel`
--

DROP TABLE IF EXISTS `shopping_site_userprofilemodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shopping_site_userprofilemodel` (
  `user_ptr_id` int(11) NOT NULL,
  `user_types` varchar(32) NOT NULL,
  PRIMARY KEY (`user_ptr_id`),
  CONSTRAINT `shopping_site_userpr_user_ptr_id_760c2b04_fk_auth_user` FOREIGN KEY (`user_ptr_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shopping_site_userprofilemodel`
--

LOCK TABLES `shopping_site_userprofilemodel` WRITE;
/*!40000 ALTER TABLE `shopping_site_userprofilemodel` DISABLE KEYS */;
INSERT INTO `shopping_site_userprofilemodel` VALUES (2,'user'),(4,'user'),(5,'admin'),(6,'user');
/*!40000 ALTER TABLE `shopping_site_userprofilemodel` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-02-18 22:35:22
