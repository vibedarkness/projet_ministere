-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : lun. 21 nov. 2022 à 20:33
-- Version du serveur : 8.0.27
-- Version de PHP : 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `facturation`
--

-- --------------------------------------------------------

--
-- Structure de la table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Structure de la table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Structure de la table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_bin NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;

--
-- Déchargement des données de la table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add client', 6, 'add_client'),
(22, 'Can change client', 6, 'change_client'),
(23, 'Can delete client', 6, 'delete_client'),
(24, 'Can view client', 6, 'view_client'),
(25, 'Can add user', 7, 'add_customuser'),
(26, 'Can change user', 7, 'change_customuser'),
(27, 'Can delete user', 7, 'delete_customuser'),
(28, 'Can view user', 7, 'view_customuser'),
(29, 'Can add staffs', 8, 'add_staffs'),
(30, 'Can change staffs', 8, 'change_staffs'),
(31, 'Can delete staffs', 8, 'delete_staffs'),
(32, 'Can view staffs', 8, 'view_staffs'),
(33, 'Can add facture', 9, 'add_facture'),
(34, 'Can change facture', 9, 'change_facture'),
(35, 'Can delete facture', 9, 'delete_facture'),
(36, 'Can view facture', 9, 'view_facture'),
(37, 'Can add attestation', 10, 'add_attestation'),
(38, 'Can change attestation', 10, 'change_attestation'),
(39, 'Can delete attestation', 10, 'delete_attestation'),
(40, 'Can view attestation', 10, 'view_attestation'),
(41, 'Can add admin', 11, 'add_admin'),
(42, 'Can change admin', 11, 'change_admin'),
(43, 'Can delete admin', 11, 'delete_admin'),
(44, 'Can view admin', 11, 'view_admin');

-- --------------------------------------------------------

--
-- Structure de la table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8_bin,
  `object_repr` varchar(200) COLLATE utf8_bin NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext COLLATE utf8_bin NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ;

-- --------------------------------------------------------

--
-- Structure de la table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8_bin NOT NULL,
  `model` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;

--
-- Déchargement des données de la table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session'),
(6, 'Main', 'client'),
(7, 'Main', 'customuser'),
(8, 'Main', 'staffs'),
(9, 'Main', 'facture'),
(10, 'Main', 'attestation'),
(11, 'Main', 'admin');

-- --------------------------------------------------------

--
-- Structure de la table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8_bin NOT NULL,
  `name` varchar(255) COLLATE utf8_bin NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;

--
-- Déchargement des données de la table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-11-21 20:19:38.490240'),
(2, 'contenttypes', '0002_remove_content_type_name', '2022-11-21 20:19:39.552808'),
(3, 'auth', '0001_initial', '2022-11-21 20:19:42.422425'),
(4, 'auth', '0002_alter_permission_name_max_length', '2022-11-21 20:19:42.687021'),
(5, 'auth', '0003_alter_user_email_max_length', '2022-11-21 20:19:42.723525'),
(6, 'auth', '0004_alter_user_username_opts', '2022-11-21 20:19:42.851496'),
(7, 'auth', '0005_alter_user_last_login_null', '2022-11-21 20:19:42.883499'),
(8, 'auth', '0006_require_contenttypes_0002', '2022-11-21 20:19:42.899494'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2022-11-21 20:19:42.931486'),
(10, 'auth', '0008_alter_user_username_max_length', '2022-11-21 20:19:42.947489'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2022-11-21 20:19:42.971483'),
(12, 'auth', '0010_alter_group_name_max_length', '2022-11-21 20:19:43.321830'),
(13, 'auth', '0011_update_proxy_permissions', '2022-11-21 20:19:43.353827'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2022-11-21 20:19:43.385827'),
(15, 'Main', '0001_initial', '2022-11-21 20:19:51.115471'),
(16, 'admin', '0001_initial', '2022-11-21 20:19:52.910761'),
(17, 'admin', '0002_logentry_remove_auto_add', '2022-11-21 20:19:52.940997'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2022-11-21 20:19:52.956993'),
(19, 'sessions', '0001_initial', '2022-11-21 20:19:53.805144');

-- --------------------------------------------------------

--
-- Structure de la table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) COLLATE utf8_bin NOT NULL,
  `session_data` longtext COLLATE utf8_bin NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Structure de la table `main_admin`
--

DROP TABLE IF EXISTS `main_admin`;
CREATE TABLE IF NOT EXISTS `main_admin` (
  `id` int NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `admin_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_id` (`admin_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Structure de la table `main_attestation`
--

DROP TABLE IF EXISTS `main_attestation`;
CREATE TABLE IF NOT EXISTS `main_attestation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `client_id` bigint NOT NULL,
  `facture_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Main_attestation_client_id_57be7b61` (`client_id`),
  KEY `Main_attestation_facture_id_aa2fc173` (`facture_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Structure de la table `main_client`
--

DROP TABLE IF EXISTS `main_client`;
CREATE TABLE IF NOT EXISTS `main_client` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nom` varchar(200) COLLATE utf8_bin NOT NULL,
  `prenom` varchar(200) COLLATE utf8_bin NOT NULL,
  `adresse` varchar(200) COLLATE utf8_bin NOT NULL,
  `telephone` varchar(200) COLLATE utf8_bin NOT NULL,
  `email` varchar(200) COLLATE utf8_bin NOT NULL,
  `sexe` varchar(200) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Structure de la table `main_customuser`
--

DROP TABLE IF EXISTS `main_customuser`;
CREATE TABLE IF NOT EXISTS `main_customuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_bin NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8_bin NOT NULL,
  `first_name` varchar(150) COLLATE utf8_bin NOT NULL,
  `last_name` varchar(150) COLLATE utf8_bin NOT NULL,
  `email` varchar(254) COLLATE utf8_bin NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `user_type` varchar(20) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;

--
-- Déchargement des données de la table `main_customuser`
--

INSERT INTO `main_customuser` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `user_type`) VALUES
(1, 'pbkdf2_sha256$390000$mdv0fokd7RxhaZnaMfNiXs$Qj7S8xS8CJoLxB2XX0BiInfIZMB1JygvAX7eANMa/GY=', NULL, 1, 'ben', '', '', 'ben@gmail.com', 1, 1, '2022-11-21 20:25:56.538507', '1');

-- --------------------------------------------------------

--
-- Structure de la table `main_customuser_groups`
--

DROP TABLE IF EXISTS `main_customuser_groups`;
CREATE TABLE IF NOT EXISTS `main_customuser_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Main_customuser_groups_customuser_id_group_id_019d79ea_uniq` (`customuser_id`,`group_id`),
  KEY `Main_customuser_groups_customuser_id_57eeb364` (`customuser_id`),
  KEY `Main_customuser_groups_group_id_4234fd54` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Structure de la table `main_customuser_user_permissions`
--

DROP TABLE IF EXISTS `main_customuser_user_permissions`;
CREATE TABLE IF NOT EXISTS `main_customuser_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Main_customuser_user_per_customuser_id_permission_55ec7719_uniq` (`customuser_id`,`permission_id`),
  KEY `Main_customuser_user_permissions_customuser_id_5fc13329` (`customuser_id`),
  KEY `Main_customuser_user_permissions_permission_id_6f4d2b12` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Structure de la table `main_facture`
--

DROP TABLE IF EXISTS `main_facture`;
CREATE TABLE IF NOT EXISTS `main_facture` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `designation` varchar(200) COLLATE utf8_bin NOT NULL,
  `poids_en_grammes` int NOT NULL,
  `titre_en_caract` int NOT NULL,
  `prix_unitaire` int NOT NULL,
  `prix_total` int NOT NULL,
  `client_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Main_facture_client_id_10b8cf6a` (`client_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Structure de la table `main_staffs`
--

DROP TABLE IF EXISTS `main_staffs`;
CREATE TABLE IF NOT EXISTS `main_staffs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `address` longtext COLLATE utf8_bin NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `admin_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_id` (`admin_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
