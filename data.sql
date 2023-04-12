-- MariaDB dump 10.19  Distrib 10.5.18-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: masm
-- ------------------------------------------------------
-- Server version	10.5.18-MariaDB-0+deb11u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Addresses`
--

DROP TABLE IF EXISTS `Addresses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Addresses` (
  `ID` tinyint(4) DEFAULT NULL,
  `Street` varchar(14) DEFAULT NULL,
  `Housenummer` tinyint(4) DEFAULT NULL,
  `Citycode` smallint(6) DEFAULT NULL,
  `City` varchar(11) DEFAULT NULL,
  `Country` varchar(7) DEFAULT NULL,
  `Email` varchar(34) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Addresses`
--

LOCK TABLES `Addresses` WRITE;
/*!40000 ALTER TABLE `Addresses` DISABLE KEYS */;
INSERT INTO `Addresses` VALUES (1,'Auf der Graube',7,4057,'Basel','Schweiz','test@business-software-for-free.de'),(2,'In der Maur',88,5066,'Zug','Schweiz','maur@pichisdns.com'),(3,'Kannerstrasse',4,7056,'St Gallen','Schweiz','kanne@pichisdns.com'),(4,'Inner Weide',55,8088,'Wintherthur','Schweiz','weide@pichisdns.com'),(5,'Norton Ring',22,6022,'Solothurn','Schweiz','norton@pichisdns.com');
/*!40000 ALTER TABLE `Addresses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Addresstypes`
--

DROP TABLE IF EXISTS `Addresstypes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Addresstypes` (
  `ID` tinyint(4) DEFAULT NULL,
  `Addresstypename` varchar(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Addresstypes`
--

LOCK TABLES `Addresstypes` WRITE;
/*!40000 ALTER TABLE `Addresstypes` DISABLE KEYS */;
INSERT INTO `Addresstypes` VALUES (1,'Privat'),(2,'Business'),(3,'Bank');
/*!40000 ALTER TABLE `Addresstypes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Bankdata`
--

DROP TABLE IF EXISTS `Bankdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Bankdata` (
  `ID` tinyint(4) DEFAULT NULL,
  `IBAN` varchar(26) DEFAULT NULL,
  `Personid` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Bankdata`
--

LOCK TABLES `Bankdata` WRITE;
/*!40000 ALTER TABLE `Bankdata` DISABLE KEYS */;
INSERT INTO `Bankdata` VALUES (2,'CH44 3199 9123 0008 8901 2',1),(3,'CH44 3199 9123 0008 8901 3',2),(4,'CH44 3199 9123 0008 8901 4',3),(5,'CH44 3199 9123 0008 8901 5',4),(6,'CH44 3199 9123 0008 8901 6',5),(7,'CH44 3199 9123 0008 8901 7',6);
/*!40000 ALTER TABLE `Bankdata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Dueto`
--

DROP TABLE IF EXISTS `Dueto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Dueto` (
  `ID` tinyint(4) DEFAULT NULL,
  `Duedate` varchar(10) DEFAULT NULL,
  `Amount` smallint(6) DEFAULT NULL,
  `Personid` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Dueto`
--

LOCK TABLES `Dueto` WRITE;
/*!40000 ALTER TABLE `Dueto` DISABLE KEYS */;
INSERT INTO `Dueto` VALUES (5,'02.03.2023',700,5),(1,'test',700,1),(3,'21.03.2023',700,3),(4,'22.03.2023',700,4);
/*!40000 ALTER TABLE `Dueto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `People`
--

DROP TABLE IF EXISTS `People`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `People` (
  `ID` tinyint(4) DEFAULT NULL,
  `Firstname` varchar(7) DEFAULT NULL,
  `Lastname` varchar(6) DEFAULT NULL,
  `Birthdate` varchar(19) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `People`
--

LOCK TABLES `People` WRITE;
/*!40000 ALTER TABLE `People` DISABLE KEYS */;
INSERT INTO `People` VALUES (1,'Egon','Olsen','1965-07-30 00:00:00'),(2,'Maria','Vorsen','2002-12-12 00:00:00'),(3,'Gunner','Mat','1999-03-02 00:00:00'),(4,'Walther','Kuru','2003-06-05 00:00:00'),(5,'Wika','Nika','2001-05-07 00:00:00'),(6,'Herbert','Wirt','1988-02-15 00:00:00');
/*!40000 ALTER TABLE `People` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Person_Address_Match`
--

DROP TABLE IF EXISTS `Person_Address_Match`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Person_Address_Match` (
  `ID` tinyint(4) DEFAULT NULL,
  `Personid` tinyint(4) DEFAULT NULL,
  `Addressid` tinyint(4) DEFAULT NULL,
  `Addresstypeid` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Person_Address_Match`
--

LOCK TABLES `Person_Address_Match` WRITE;
/*!40000 ALTER TABLE `Person_Address_Match` DISABLE KEYS */;
INSERT INTO `Person_Address_Match` VALUES (1,1,1,3),(2,2,2,3),(3,3,2,3),(4,4,4,3),(5,5,5,3);
/*!40000 ALTER TABLE `Person_Address_Match` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_emailaddress`
--

DROP TABLE IF EXISTS `account_emailaddress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_emailaddress` (
  `id` varchar(0) DEFAULT NULL,
  `verified` varchar(0) DEFAULT NULL,
  `primary` varchar(0) DEFAULT NULL,
  `user_id` varchar(0) DEFAULT NULL,
  `email` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_emailaddress`
--

LOCK TABLES `account_emailaddress` WRITE;
/*!40000 ALTER TABLE `account_emailaddress` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_emailaddress` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account_emailconfirmation`
--

DROP TABLE IF EXISTS `account_emailconfirmation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_emailconfirmation` (
  `id` varchar(0) DEFAULT NULL,
  `created` varchar(0) DEFAULT NULL,
  `sent` varchar(0) DEFAULT NULL,
  `key` varchar(0) DEFAULT NULL,
  `email_address_id` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_emailconfirmation`
--

LOCK TABLES `account_emailconfirmation` WRITE;
/*!40000 ALTER TABLE `account_emailconfirmation` DISABLE KEYS */;
/*!40000 ALTER TABLE `account_emailconfirmation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` varchar(0) DEFAULT NULL,
  `name` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
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
  `id` varchar(0) DEFAULT NULL,
  `group_id` varchar(0) DEFAULT NULL,
  `permission_id` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
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
  `id` tinyint(4) DEFAULT NULL,
  `content_type_id` tinyint(4) DEFAULT NULL,
  `codename` varchar(24) DEFAULT NULL,
  `name` varchar(29) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,1,'add_logentry','Can add log entry'),(2,1,'change_logentry','Can change log entry'),(3,1,'delete_logentry','Can delete log entry'),(4,1,'view_logentry','Can view log entry'),(5,2,'add_permission','Can add permission'),(6,2,'change_permission','Can change permission'),(7,2,'delete_permission','Can delete permission'),(8,2,'view_permission','Can view permission'),(9,3,'add_group','Can add group'),(10,3,'change_group','Can change group'),(11,3,'delete_group','Can delete group'),(12,3,'view_group','Can view group'),(13,4,'add_user','Can add user'),(14,4,'change_user','Can change user'),(15,4,'delete_user','Can delete user'),(16,4,'view_user','Can view user'),(17,5,'add_contenttype','Can add content type'),(18,5,'change_contenttype','Can change content type'),(19,5,'delete_contenttype','Can delete content type'),(20,5,'view_contenttype','Can view content type'),(21,6,'add_session','Can add session'),(22,6,'change_session','Can change session'),(23,6,'delete_session','Can delete session'),(24,6,'view_session','Can view session'),(25,7,'add_course','Can add course'),(26,7,'change_course','Can change course'),(27,7,'delete_course','Can delete course'),(28,7,'view_course','Can view course'),(29,8,'add_student','Can add student'),(30,8,'change_student','Can change student'),(31,8,'delete_student','Can delete student'),(32,8,'view_student','Can view student'),(33,9,'add_teacher','Can add teacher'),(34,9,'change_teacher','Can change teacher'),(35,9,'delete_teacher','Can delete teacher'),(36,9,'view_teacher','Can view teacher'),(37,10,'add_courseschedule','Can add course schedule'),(38,10,'change_courseschedule','Can change course schedule'),(39,10,'delete_courseschedule','Can delete course schedule'),(40,10,'view_courseschedule','Can view course schedule'),(41,11,'add_belt','Can add belt'),(42,11,'change_belt','Can change belt'),(43,11,'delete_belt','Can delete belt'),(44,11,'view_belt','Can view belt'),(45,12,'add_emailaddress','Can add email address'),(46,12,'change_emailaddress','Can change email address'),(47,12,'delete_emailaddress','Can delete email address'),(48,12,'view_emailaddress','Can view email address'),(49,13,'add_emailconfirmation','Can add email confirmation'),(50,13,'change_emailconfirmation','Can change email confirmation'),(51,13,'delete_emailconfirmation','Can delete email confirmation'),(52,13,'view_emailconfirmation','Can view email confirmation');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` tinyint(4) DEFAULT NULL,
  `password` varchar(88) DEFAULT NULL,
  `last_login` varchar(10) DEFAULT NULL,
  `is_superuser` tinyint(4) DEFAULT NULL,
  `username` varchar(3) DEFAULT NULL,
  `first_name` varchar(0) DEFAULT NULL,
  `last_name` varchar(0) DEFAULT NULL,
  `is_staff` tinyint(4) DEFAULT NULL,
  `is_active` tinyint(4) DEFAULT NULL,
  `date_joined` varchar(10) DEFAULT NULL,
  `email` varchar(7) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$390000$yuUErMxitIrRWkCZuiyL1y$BiJuJha3AspLhdkla2WEilLVSsZYC/FgWoaMQtQm4iY=','2023-04-07',1,'dev','','',1,1,'2023-04-07','1@1.com');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` varchar(0) DEFAULT NULL,
  `user_id` varchar(0) DEFAULT NULL,
  `group_id` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
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
  `id` varchar(0) DEFAULT NULL,
  `user_id` varchar(0) DEFAULT NULL,
  `permission_id` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
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
  `id` tinyint(4) DEFAULT NULL,
  `object_id` tinyint(4) DEFAULT NULL,
  `object_repr` varchar(20) DEFAULT NULL,
  `action_flag` tinyint(4) DEFAULT NULL,
  `change_message` varchar(15) DEFAULT NULL,
  `content_type_id` tinyint(4) DEFAULT NULL,
  `user_id` tinyint(4) DEFAULT NULL,
  `action_time` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,1,'Name \'create_student',1,'[{\"added\": {}}]',8,1,'2023-04-07');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` tinyint(4) DEFAULT NULL,
  `app_label` varchar(12) DEFAULT NULL,
  `model` varchar(17) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (12,'account','emailaddress'),(13,'account','emailconfirmation'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(11,'main','belt'),(7,'main','course'),(10,'main','courseschedule'),(8,'main','student'),(9,'main','teacher'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` tinyint(4) DEFAULT NULL,
  `app` varchar(12) DEFAULT NULL,
  `name` varchar(66) DEFAULT NULL,
  `applied` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-04-07'),(2,'auth','0001_initial','2023-04-07'),(3,'account','0001_initial','2023-04-07'),(4,'account','0002_email_max_length','2023-04-07'),(5,'admin','0001_initial','2023-04-07'),(6,'admin','0002_logentry_remove_auto_add','2023-04-07'),(7,'admin','0003_logentry_add_action_flag_choices','2023-04-07'),(8,'contenttypes','0002_remove_content_type_name','2023-04-07'),(9,'auth','0002_alter_permission_name_max_length','2023-04-07'),(10,'auth','0003_alter_user_email_max_length','2023-04-07'),(11,'auth','0004_alter_user_username_opts','2023-04-07'),(12,'auth','0005_alter_user_last_login_null','2023-04-07'),(13,'auth','0006_require_contenttypes_0002','2023-04-07'),(14,'auth','0007_alter_validators_add_error_messages','2023-04-07'),(15,'auth','0008_alter_user_username_max_length','2023-04-07'),(16,'auth','0009_alter_user_last_name_max_length','2023-04-07'),(17,'auth','0010_alter_group_name_max_length','2023-04-07'),(18,'auth','0011_update_proxy_permissions','2023-04-07'),(19,'auth','0012_alter_user_first_name_max_length','2023-04-07'),(20,'auth','0013_alter_user_email','2023-04-07'),(21,'auth','0014_alter_user_email','2023-04-07'),(22,'auth','0015_alter_user_email','2023-04-07'),(23,'auth','0016_alter_user_email','2023-04-07'),(24,'auth','0017_alter_user_email','2023-04-07'),(25,'auth','0018_alter_user_email','2023-04-07'),(26,'auth','0019_alter_user_email','2023-04-07'),(27,'auth','0020_alter_user_email','2023-04-07'),(28,'main','0001_initial','2023-04-07'),(29,'main','0002_alter_student_birthdate_alter_teacher_birthdate','2023-04-07'),(30,'main','0003_student_grade','2023-04-07'),(31,'sessions','0001_initial','2023-04-07'),(32,'main','0004_course_day_of_week_course_end_time_course_start_time_and_more','2023-04-07'),(33,'main','0005_alter_course_end_time_alter_course_start_time','2023-04-07'),(34,'main','0006_alter_course_end_time_alter_course_start_time','2023-04-07');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(32) DEFAULT NULL,
  `session_data` varchar(246) DEFAULT NULL,
  `expire_date` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('ouo9sg5vplxhqm3sl3mwwgd5bkx1htx4','.eJxVjDsOwjAQBe_iGlkbx79NSc8ZLH82xIBsFCcSCHF3iJQC2jfz5sWcX5fJrY1mlxMbWMcOv1vw8UplA-niy7nyWMsy58A3he-08VNNdDvu7l9g8m36vscUQtRGmAggJCivtUKlxh4kkoEOAyYLiCQCoDWKrNLagjAiph6C3KKNWsu1OHrc8_xkA7w_UQU90A:1pkjPm:KIkPEU7GUpBF7nSf0AdIBb7f-AJOEDe7-n9AIHxVsLA','2023-04-21');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_belt`
--

DROP TABLE IF EXISTS `main_belt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_belt` (
  `id` varchar(0) DEFAULT NULL,
  `name` varchar(0) DEFAULT NULL,
  `description` varchar(0) DEFAULT NULL,
  `user_id` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_belt`
--

LOCK TABLES `main_belt` WRITE;
/*!40000 ALTER TABLE `main_belt` DISABLE KEYS */;
/*!40000 ALTER TABLE `main_belt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_course`
--

DROP TABLE IF EXISTS `main_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_course` (
  `id` tinyint(4) DEFAULT NULL,
  `course_name` varchar(7) DEFAULT NULL,
  `duration` tinyint(4) DEFAULT NULL,
  `instructor_id` tinyint(4) DEFAULT NULL,
  `day_of_week` varchar(9) DEFAULT NULL,
  `end_time` varchar(8) DEFAULT NULL,
  `start_time` varchar(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_course`
--

LOCK TABLES `main_course` WRITE;
/*!40000 ALTER TABLE `main_course` DISABLE KEYS */;
INSERT INTO `main_course` VALUES (1,'Yoga',2,1,'Wednesday','21:00:00','20:00:00'),(2,'Kung Fu',2,1,'Wednesday','22:00:00','20:00:00'),(3,'test',12,1,'Tuesday','12:00:00','20:00:00');
/*!40000 ALTER TABLE `main_course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_courseschedule`
--

DROP TABLE IF EXISTS `main_courseschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_courseschedule` (
  `id` varchar(0) DEFAULT NULL,
  `day_of_week` varchar(0) DEFAULT NULL,
  `start_time` varchar(0) DEFAULT NULL,
  `end_time` varchar(0) DEFAULT NULL,
  `course_id` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_courseschedule`
--

LOCK TABLES `main_courseschedule` WRITE;
/*!40000 ALTER TABLE `main_courseschedule` DISABLE KEYS */;
/*!40000 ALTER TABLE `main_courseschedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_student`
--

DROP TABLE IF EXISTS `main_student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_student` (
  `id` tinyint(4) DEFAULT NULL,
  `name` varchar(4) DEFAULT NULL,
  `surname` varchar(15) DEFAULT NULL,
  `street_nr` tinyint(4) DEFAULT NULL,
  `birthdate` varchar(0) DEFAULT NULL,
  `grade` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_student`
--

LOCK TABLES `main_student` WRITE;
/*!40000 ALTER TABLE `main_student` DISABLE KEYS */;
INSERT INTO `main_student` VALUES (1,'Name','\'create_student',2,'',2);
/*!40000 ALTER TABLE `main_student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_teacher`
--

DROP TABLE IF EXISTS `main_teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_teacher` (
  `id` tinyint(4) DEFAULT NULL,
  `name` varchar(4) DEFAULT NULL,
  `surname` varchar(15) DEFAULT NULL,
  `street_nr` tinyint(4) DEFAULT NULL,
  `birthdate` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_teacher`
--

LOCK TABLES `main_teacher` WRITE;
/*!40000 ALTER TABLE `main_teacher` DISABLE KEYS */;
INSERT INTO `main_teacher` VALUES (1,'sd','\'create_student',3,''),(2,'Mika','abs',2,'');
/*!40000 ALTER TABLE `main_teacher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sqlite_sequence`
--

DROP TABLE IF EXISTS `sqlite_sequence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sqlite_sequence` (
  `name` varchar(20) DEFAULT NULL,
  `seq` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sqlite_sequence`
--

LOCK TABLES `sqlite_sequence` WRITE;
/*!40000 ALTER TABLE `sqlite_sequence` DISABLE KEYS */;
INSERT INTO `sqlite_sequence` VALUES ('django_migrations',34),('account_emailaddress',0),('django_admin_log',1),('django_content_type',13),('auth_permission',52),('auth_group',0),('auth_user',1),('main_student',1),('main_teacher',2),('main_course',3);
/*!40000 ALTER TABLE `sqlite_sequence` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-11 17:15:59
