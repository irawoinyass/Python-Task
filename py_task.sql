-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 19, 2023 at 02:54 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `py_task`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts_user`
--

CREATE TABLE `accounts_user` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `email` varchar(254) NOT NULL,
  `username` varchar(150) NOT NULL,
  `name` varchar(200) NOT NULL,
  `start_date` datetime(6) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `accounts_user`
--

INSERT INTO `accounts_user` (`id`, `password`, `last_login`, `is_superuser`, `email`, `username`, `name`, `start_date`, `is_staff`, `is_active`) VALUES
(1, 'pbkdf2_sha256$320000$F2zNIw8vtTu92jWqxO6MYb$OfFh5lM8WRSxba4MvC6NGEOnIMXX2de06Xyd59v048s=', '2023-04-12 15:19:48.026365', 1, 'lasisisaheed10@gmail.com', 'Irawo Inyass', 'Saheed Lasisi', '2023-04-11 16:51:22.928053', 1, 1),
(4, 'pbkdf2_sha256$320000$DyXa1RaykazajEomnD7LXq$iT4AP+aH8MrDIUy+mfoJ7jS3R7ktEa5UluFAaYYW8uk=', NULL, 0, 'adminuserone@gmail.com', 'AdminUserOne', 'Admin User One', '2023-04-12 16:52:25.570959', 1, 1),
(11, 'pbkdf2_sha256$320000$fmxcLtrxJwvyOVJXOmk6Te$qQeVYldqAfKR/skmcwplLbAPtIyPT/wtKvrIuVhDfSA=', NULL, 0, 'user1@gmail.com', 'User1', 'User One', '2023-04-13 15:18:55.328401', 0, 1),
(12, 'pbkdf2_sha256$320000$klwyekKHEXZqkrv2yLJboX$ky3BvulrxYRHaVlvGh4DHxKkB0dhmM9m6At1lMO+PvI=', NULL, 0, 'user@gmail.com', 'User2', 'User Two', '2023-04-15 17:27:35.185435', 0, 1),
(13, 'pbkdf2_sha256$320000$6kzaDMNRePh9RVLtJmYkGe$Z7Jmrn0TTB65gSLIWb/SnpNdFcOpYvP3YwLuUVg9+Qs=', NULL, 0, 'adminuser2@gmail.com', 'AdminUser2', 'Admin User Two', '2023-04-16 19:22:39.020154', 1, 1),
(17, 'pbkdf2_sha256$320000$JpcrGumekxzkI75fC1GZrW$XFWCL1gT5EzJQoKEAjL9jsza6WENosvVQX4JjMQw61A=', NULL, 0, 'user3@gmail.com', 'User3', 'User Three', '2023-04-16 20:34:09.610329', 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `accounts_user_groups`
--

CREATE TABLE `accounts_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `accounts_user_user_permissions`
--

CREATE TABLE `accounts_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
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
(21, 'Can add auth token', 6, 'add_authtoken'),
(22, 'Can change auth token', 6, 'change_authtoken'),
(23, 'Can delete auth token', 6, 'delete_authtoken'),
(24, 'Can view auth token', 6, 'view_authtoken'),
(25, 'Can add user', 7, 'add_user'),
(26, 'Can change user', 7, 'change_user'),
(27, 'Can delete user', 7, 'delete_user'),
(28, 'Can view user', 7, 'view_user'),
(29, 'Can add cagetory', 8, 'add_cagetory'),
(30, 'Can change cagetory', 8, 'change_cagetory'),
(31, 'Can delete cagetory', 8, 'delete_cagetory'),
(32, 'Can view cagetory', 8, 'view_cagetory'),
(33, 'Can add category', 8, 'add_category'),
(34, 'Can change category', 8, 'change_category'),
(35, 'Can delete category', 8, 'delete_category'),
(36, 'Can view category', 8, 'view_category'),
(37, 'Can add activation model', 9, 'add_activationmodel'),
(38, 'Can change activation model', 9, 'change_activationmodel'),
(39, 'Can delete activation model', 9, 'delete_activationmodel'),
(40, 'Can view activation model', 9, 'view_activationmodel'),
(41, 'Can add password token model', 10, 'add_passwordtokenmodel'),
(42, 'Can change password token model', 10, 'change_passwordtokenmodel'),
(43, 'Can delete password token model', 10, 'delete_passwordtokenmodel'),
(44, 'Can view password token model', 10, 'view_passwordtokenmodel'),
(45, 'Can add post', 11, 'add_post'),
(46, 'Can change post', 11, 'change_post'),
(47, 'Can delete post', 11, 'delete_post'),
(48, 'Can view post', 11, 'view_post'),
(49, 'Can add comment', 12, 'add_comment'),
(50, 'Can change comment', 12, 'change_comment'),
(51, 'Can delete comment', 12, 'delete_comment'),
(52, 'Can view comment', 12, 'view_comment'),
(53, 'Can add nested comment', 13, 'add_nestedcomment'),
(54, 'Can change nested comment', 13, 'change_nestedcomment'),
(55, 'Can delete nested comment', 13, 'delete_nestedcomment'),
(56, 'Can view nested comment', 13, 'view_nestedcomment');

-- --------------------------------------------------------

--
-- Table structure for table `categories_category`
--

CREATE TABLE `categories_category` (
  `id` bigint(20) NOT NULL,
  `category_name` varchar(120) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `categories_category`
--

INSERT INTO `categories_category` (`id`, `category_name`, `created_at`, `updated_at`) VALUES
(1, 'Sporting', '2023-04-12 23:36:16.529273', '2023-04-15 19:34:09.719661'),
(2, 'Scoccer', '2023-04-12 23:36:41.744275', '2023-04-15 19:34:33.373083'),
(3, 'Racing', '2023-04-12 23:37:19.033969', '2023-04-12 23:37:19.033969'),
(5, 'Music', '2023-04-16 19:12:02.411326', '2023-04-16 19:12:02.411326'),
(6, 'Film Production', '2023-04-16 19:13:30.756608', '2023-04-16 19:13:30.756608'),
(7, 'Software Development', '2023-04-16 19:13:40.610888', '2023-04-16 19:13:40.610888');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2023-04-11 18:13:44.448079', '2', 'staff@gmail.com', 1, '[{\"added\": {}}]', 7, 1),
(2, '2023-04-12 14:50:17.476537', '1', 'lasisisaheed10@gmail.com', 2, '[{\"changed\": {\"fields\": [\"Is staff\"]}}]', 7, 1),
(3, '2023-04-13 12:30:48.871869', '5', 'customer2@gmail.com', 3, '', 7, 1),
(4, '2023-04-13 14:58:00.006221', '6', 'user1@gmail.com', 3, '', 7, 1),
(5, '2023-04-13 14:59:19.876219', '7', 'user1@gmail.com', 3, '', 7, 1),
(6, '2023-04-13 15:15:06.861300', '8', 'user1@gmail.com', 3, '', 7, 1),
(7, '2023-04-13 15:16:11.641583', '9', 'user1@gmail.com', 3, '', 7, 1),
(8, '2023-04-13 15:17:34.736848', '10', 'user1@gmail.com', 3, '', 7, 1),
(9, '2023-04-13 15:20:51.349565', '11', 'user1@gmail.com', 2, '[{\"changed\": {\"fields\": [\"Is active\"]}}]', 7, 1),
(10, '2023-04-13 15:21:48.579061', '11', 'user1@gmail.com', 2, '[{\"changed\": {\"fields\": [\"Is active\"]}}]', 7, 1),
(11, '2023-04-13 21:06:01.199657', '1', 'PasswordTokenModel object (1)', 1, '[{\"added\": {}}]', 10, 1),
(12, '2023-04-14 23:56:48.099463', '11', 'user1@gmail.com', 2, '[{\"changed\": {\"fields\": [\"Is staff\"]}}]', 7, 1),
(13, '2023-04-14 23:57:28.237014', '11', 'user1@gmail.com', 2, '[{\"changed\": {\"fields\": [\"Is staff\"]}}]', 7, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(7, 'accounts', 'user'),
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(8, 'categories', 'category'),
(4, 'contenttypes', 'contenttype'),
(6, 'knox', 'authtoken'),
(12, 'posts', 'comment'),
(13, 'posts', 'nestedcomment'),
(11, 'posts', 'post'),
(5, 'sessions', 'session'),
(9, 'users', 'activationmodel'),
(10, 'users', 'passwordtokenmodel');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-04-11 16:40:00.914600'),
(2, 'contenttypes', '0002_remove_content_type_name', '2023-04-11 16:40:01.874479'),
(3, 'auth', '0001_initial', '2023-04-11 16:40:06.722662'),
(4, 'auth', '0002_alter_permission_name_max_length', '2023-04-11 16:40:09.131079'),
(5, 'auth', '0003_alter_user_email_max_length', '2023-04-11 16:40:09.241392'),
(6, 'auth', '0004_alter_user_username_opts', '2023-04-11 16:40:09.336612'),
(7, 'auth', '0005_alter_user_last_login_null', '2023-04-11 16:40:09.680831'),
(8, 'auth', '0006_require_contenttypes_0002', '2023-04-11 16:40:09.906180'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2023-04-11 16:40:10.334145'),
(10, 'auth', '0008_alter_user_username_max_length', '2023-04-11 16:40:10.647311'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2023-04-11 16:40:11.035721'),
(12, 'auth', '0010_alter_group_name_max_length', '2023-04-11 16:40:11.282909'),
(13, 'auth', '0011_update_proxy_permissions', '2023-04-11 16:40:11.389636'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2023-04-11 16:40:11.516553'),
(15, 'accounts', '0001_initial', '2023-04-11 16:40:25.259589'),
(16, 'admin', '0001_initial', '2023-04-11 16:40:31.902913'),
(17, 'admin', '0002_logentry_remove_auto_add', '2023-04-11 16:40:32.014010'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2023-04-11 16:40:32.079968'),
(19, 'knox', '0001_initial', '2023-04-11 16:40:36.034252'),
(20, 'knox', '0002_auto_20150916_1425', '2023-04-11 16:40:40.894428'),
(21, 'knox', '0003_auto_20150916_1526', '2023-04-11 16:40:41.258574'),
(22, 'knox', '0004_authtoken_expires', '2023-04-11 16:40:41.714396'),
(23, 'knox', '0005_authtoken_token_key', '2023-04-11 16:40:42.944155'),
(24, 'knox', '0006_auto_20160818_0932', '2023-04-11 16:40:45.674426'),
(25, 'knox', '0007_auto_20190111_0542', '2023-04-11 16:40:46.436843'),
(26, 'knox', '0008_remove_authtoken_salt', '2023-04-11 16:40:47.588199'),
(27, 'sessions', '0001_initial', '2023-04-11 16:40:49.129403'),
(28, 'accounts', '0002_rename_is_adminuser_user_is_staff', '2023-04-11 17:05:05.134002'),
(29, 'categories', '0001_initial', '2023-04-12 23:26:55.354393'),
(30, 'categories', '0002_rename_cagetory_category', '2023-04-12 23:28:48.954667'),
(31, 'users', '0001_initial', '2023-04-13 14:52:36.518515'),
(32, 'users', '0002_rename_address_activationmodel_token', '2023-04-13 14:54:45.646642'),
(33, 'users', '0003_passwordtokenmodel', '2023-04-13 20:50:07.334280'),
(34, 'posts', '0001_initial', '2023-04-14 22:03:57.506288'),
(35, 'posts', '0002_post_category_id_alter_post_posted_at', '2023-04-15 00:32:34.110383'),
(36, 'posts', '0003_alter_post_category_id', '2023-04-15 00:40:30.412826'),
(37, 'posts', '0004_alter_post_category_id', '2023-04-15 00:42:47.555846'),
(38, 'posts', '0005_alter_post_category_id', '2023-04-15 00:53:52.877165'),
(39, 'posts', '0006_alter_post_category_id', '2023-04-15 00:59:50.266913'),
(40, 'posts', '0007_comment', '2023-04-15 19:55:14.229540'),
(41, 'posts', '0008_remove_comment_updated_at_comment_cat_id_and_more', '2023-04-15 20:14:06.615983'),
(42, 'posts', '0009_alter_comment_created_at', '2023-04-15 20:17:34.995527'),
(43, 'posts', '0010_alter_comment_created_at', '2023-04-15 20:18:06.145670'),
(44, 'posts', '0011_nestedcomment', '2023-04-15 21:44:05.539948');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('n57tzp8eflk333yyoi1yxktjcc4qce1e', '.eJxVjDkOwjAURO_iGlne_U1JnzNY3xsOIFuKkwpxdxIpBXSjeW_mTTxua_XbyIufE7kSTi6_XcD4zO0A6YHt3mnsbV3mQA-FnnTQqaf8up3u30HFUfc1c9rZkKSWYIFjgOKki4m7YACkMUVoVSIU3KMCyUzRwbAshMWYs1Hk8wXGDjdt:1pmcGC:vlJPtFzT6QgJgG1hFQfiQZYcQme9c3VYl4WUdqKLYkc', '2023-04-26 15:19:48.074353');

-- --------------------------------------------------------

--
-- Table structure for table `knox_authtoken`
--

CREATE TABLE `knox_authtoken` (
  `digest` varchar(128) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `expiry` datetime(6) DEFAULT NULL,
  `token_key` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `knox_authtoken`
--

INSERT INTO `knox_authtoken` (`digest`, `created`, `user_id`, `expiry`, `token_key`) VALUES
('0586677ec9d81352bf998e32d133f38d9e823a733c408ad20d7d7d900c860159fba5c0db9b82e3171d12ff7ee38436ea8399ac448a8ad3e6ed7231efbd8dc24c', '2023-04-16 18:51:27.311348', 1, NULL, '3c0a1b08'),
('05e3bab021d734da13455abeedb3e6492faa0ebace00c48f2af0a407b48e984fbaf23c0517a3af75a7606a3b60af3948adaeb470e6d7e540d4feeaacc6951807', '2023-04-16 20:46:10.051848', 17, NULL, 'a1af6aa1'),
('169b5497eb2a1c2785d9462cd19ef4b81002c35f62b64f01fa779caccf90fa0adeaa2d8948bad704ee14d4318546a05eb09e0a16fec2207357ab035e16e33c19', '2023-04-15 17:20:36.858318', 11, '2023-04-16 03:20:36.858318', '31f1b2c4'),
('1ff4a67c5473ce427c84867c3e8a9d9ff637d976d13a4926c0835c8afa46e0bb8e2f5232133685c71ce0f3aa9353c83f2ab72f32dbff558aefbf62973257ebe5', '2023-04-16 19:20:52.519875', 1, NULL, '3bab6863'),
('71fce63ad8cfd61ec7cca400765b7ae820fd5e1fd698add90609f72463f33549cf7d3726738e31f3acfc078a9c98199563f3c57d5951c61751100f746843ebee', '2023-04-19 00:33:44.612474', 1, NULL, 'c8dbffcc'),
('9a02fd7f1ffe64303a5aa0e6f3104f76d3f6ef06415df92978dd468d13fd3d769c81246cbff0cc1d4c0ac9f5dd40f5d56e8f37739390f8ba44406a3ea2a0f7e5', '2023-04-16 14:51:17.798222', 12, '2023-04-17 00:51:17.797223', '833b767b'),
('e6d6df583958b2632f06874685464a7060050e5727f613af1375b7371815ce34794350f31806067358cb97950f76c486059c28fade8ba9864fa6538491dd51c8', '2023-04-16 18:46:44.119749', 1, NULL, '0bb2a5b4'),
('fd52c3aa8509df5de9925cafe429f6f0f4b129eb8317c5e35201a216c76b4c30927852254b2183a7c465bca28b770976235096c688f0557e8100a3f2a3745070', '2023-04-16 20:34:10.187113', 17, NULL, 'b7efde27');

-- --------------------------------------------------------

--
-- Table structure for table `posts_comment`
--

CREATE TABLE `posts_comment` (
  `id` bigint(20) NOT NULL,
  `comment` varchar(250) NOT NULL,
  `created_at` date NOT NULL,
  `post_id_id` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `cat_id_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts_comment`
--

INSERT INTO `posts_comment` (`id`, `comment`, `created_at`, `post_id_id`, `user_id`, `cat_id_id`) VALUES
(1, 'Wow !!', '2023-04-15', 4, 12, 1),
(2, 'This could change all our livies', '2023-04-16', 4, 12, 1),
(3, 'nice one', '2023-04-16', 8, 17, 5);

-- --------------------------------------------------------

--
-- Table structure for table `posts_nestedcomment`
--

CREATE TABLE `posts_nestedcomment` (
  `id` bigint(20) NOT NULL,
  `comment` varchar(250) NOT NULL,
  `created_at` date NOT NULL,
  `comment_id_id` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts_nestedcomment`
--

INSERT INTO `posts_nestedcomment` (`id`, `comment`, `created_at`, `comment_id_id`, `user_id`) VALUES
(1, 'I mean just too funny', '2023-04-16', 1, 12),
(2, 'ride on', '2023-04-16', 3, 17);

-- --------------------------------------------------------

--
-- Table structure for table `posts_post`
--

CREATE TABLE `posts_post` (
  `id` bigint(20) NOT NULL,
  `title` varchar(1000) NOT NULL,
  `body` longtext NOT NULL,
  `posted_at` date NOT NULL,
  `is_public` tinyint(1) NOT NULL,
  `author_id` bigint(20) DEFAULT NULL,
  `category_id_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts_post`
--

INSERT INTO `posts_post` (`id`, `title`, `body`, `posted_at`, `is_public`, `author_id`, `category_id_id`) VALUES
(1, 'Hakimi the master', 'a great footballer', '2023-04-15', 1, 11, 1),
(2, 'Man City 3-0 Leicester', '39: SHOT! Maddison clips a free kick into the middle. Soyuncu wins the first contact and it drops to Faes about 15 yards out. He hits one on the turn but it loops harmlessly over the crossbar.', '2023-04-15', 0, 11, 1),
(3, 'Grand National: Favourite Corach Rambler delivers for Derek Fox and Lucinda Russell in Aintree feature', 'Corach Rambler proved too strong in the finish for Derek Fox and Lucinda Russell; the pair combined for a second time after One For Arthur\'s win in 2017; Vanillier finished second, Gaillard Du Mesnil third, defending champion Noble Yeats fourth', '2023-04-15', 1, 11, 2),
(4, 'Hazardours', 'harzard is the first play to win winwin', '2023-04-15', 0, 12, 1),
(5, 'Neymar', 'neymar likes harzard', '2023-04-15', 0, 12, 1),
(7, 'dpoklaskf;ladksf;l', 'dkfl;dskf;lskdlfkal;', '2023-04-15', 0, 11, 2),
(8, 'Saheed Osupa is the king of Music', 'Indeed', '2023-04-16', 1, 17, 5),
(9, 'Pasoma likes osupa', 'i think so', '2023-04-16', 0, 17, 5);

-- --------------------------------------------------------

--
-- Table structure for table `users_activationmodel`
--

CREATE TABLE `users_activationmodel` (
  `id` bigint(20) NOT NULL,
  `token` varchar(1000) NOT NULL,
  `user_id_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users_activationmodel`
--

INSERT INTO `users_activationmodel` (`id`, `token`, `user_id_id`) VALUES
(3, 'bmlrzk-92017a6cae84104462e14fc60d2adc59', 11),
(4, 'bmpn9z-bb3ae23b8089bc30d6bf605f86076053', 12),
(5, 'bmrqky-60ee324792997ebcb2be8aadea436a12', 17);

-- --------------------------------------------------------

--
-- Table structure for table `users_passwordtokenmodel`
--

CREATE TABLE `users_passwordtokenmodel` (
  `id` bigint(20) NOT NULL,
  `token` varchar(1000) NOT NULL,
  `user_id_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts_user`
--
ALTER TABLE `accounts_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `accounts_user_groups`
--
ALTER TABLE `accounts_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `accounts_user_groups_user_id_group_id_59c0b32f_uniq` (`user_id`,`group_id`),
  ADD KEY `accounts_user_groups_group_id_bd11a704_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `accounts_user_user_permissions`
--
ALTER TABLE `accounts_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `accounts_user_user_permi_user_id_permission_id_2ab516c2_uniq` (`user_id`,`permission_id`),
  ADD KEY `accounts_user_user_p_permission_id_113bb443_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `categories_category`
--
ALTER TABLE `categories_category`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `category_name` (`category_name`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_accounts_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `knox_authtoken`
--
ALTER TABLE `knox_authtoken`
  ADD PRIMARY KEY (`digest`),
  ADD KEY `knox_authtoken_user_id_e5a5d899_fk_accounts_user_id` (`user_id`),
  ADD KEY `knox_authtoken_token_key_8f4f7d47` (`token_key`);

--
-- Indexes for table `posts_comment`
--
ALTER TABLE `posts_comment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `posts_comment_post_id_id_c1a6fcb3_fk_posts_post_id` (`post_id_id`),
  ADD KEY `posts_comment_user_id_ad949c47_fk_accounts_user_id` (`user_id`),
  ADD KEY `posts_comment_cat_id_id_b6e57740_fk_categories_category_id` (`cat_id_id`);

--
-- Indexes for table `posts_nestedcomment`
--
ALTER TABLE `posts_nestedcomment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `posts_nestedcomment_comment_id_id_31af1317_fk_posts_comment_id` (`comment_id_id`),
  ADD KEY `posts_nestedcomment_user_id_a9eef9fe_fk_accounts_user_id` (`user_id`);

--
-- Indexes for table `posts_post`
--
ALTER TABLE `posts_post`
  ADD PRIMARY KEY (`id`),
  ADD KEY `posts_post_author_id_fe5487bf_fk_accounts_user_id` (`author_id`),
  ADD KEY `posts_post_category_id_id_f292a438` (`category_id_id`);

--
-- Indexes for table `users_activationmodel`
--
ALTER TABLE `users_activationmodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `users_activationmodel_user_id_id_9fcc4374_fk_accounts_user_id` (`user_id_id`);

--
-- Indexes for table `users_passwordtokenmodel`
--
ALTER TABLE `users_passwordtokenmodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `users_passwordtokenmodel_user_id_id_3eac01f9_fk_accounts_user_id` (`user_id_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounts_user`
--
ALTER TABLE `accounts_user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `accounts_user_groups`
--
ALTER TABLE `accounts_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `accounts_user_user_permissions`
--
ALTER TABLE `accounts_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- AUTO_INCREMENT for table `categories_category`
--
ALTER TABLE `categories_category`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `posts_comment`
--
ALTER TABLE `posts_comment`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `posts_nestedcomment`
--
ALTER TABLE `posts_nestedcomment`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `posts_post`
--
ALTER TABLE `posts_post`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `users_activationmodel`
--
ALTER TABLE `users_activationmodel`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `users_passwordtokenmodel`
--
ALTER TABLE `users_passwordtokenmodel`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `accounts_user_groups`
--
ALTER TABLE `accounts_user_groups`
  ADD CONSTRAINT `accounts_user_groups_group_id_bd11a704_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `accounts_user_groups_user_id_52b62117_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`);

--
-- Constraints for table `accounts_user_user_permissions`
--
ALTER TABLE `accounts_user_user_permissions`
  ADD CONSTRAINT `accounts_user_user_p_permission_id_113bb443_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `accounts_user_user_p_user_id_e4f0a161_fk_accounts_` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`);

--
-- Constraints for table `knox_authtoken`
--
ALTER TABLE `knox_authtoken`
  ADD CONSTRAINT `knox_authtoken_user_id_e5a5d899_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`);

--
-- Constraints for table `posts_comment`
--
ALTER TABLE `posts_comment`
  ADD CONSTRAINT `posts_comment_cat_id_id_b6e57740_fk_categories_category_id` FOREIGN KEY (`cat_id_id`) REFERENCES `categories_category` (`id`),
  ADD CONSTRAINT `posts_comment_post_id_id_c1a6fcb3_fk_posts_post_id` FOREIGN KEY (`post_id_id`) REFERENCES `posts_post` (`id`),
  ADD CONSTRAINT `posts_comment_user_id_ad949c47_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`);

--
-- Constraints for table `posts_nestedcomment`
--
ALTER TABLE `posts_nestedcomment`
  ADD CONSTRAINT `posts_nestedcomment_comment_id_id_31af1317_fk_posts_comment_id` FOREIGN KEY (`comment_id_id`) REFERENCES `posts_comment` (`id`),
  ADD CONSTRAINT `posts_nestedcomment_user_id_a9eef9fe_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`);

--
-- Constraints for table `posts_post`
--
ALTER TABLE `posts_post`
  ADD CONSTRAINT `posts_post_author_id_fe5487bf_fk_accounts_user_id` FOREIGN KEY (`author_id`) REFERENCES `accounts_user` (`id`),
  ADD CONSTRAINT `posts_post_category_id_id_f292a438_fk_categories_category_id` FOREIGN KEY (`category_id_id`) REFERENCES `categories_category` (`id`);

--
-- Constraints for table `users_activationmodel`
--
ALTER TABLE `users_activationmodel`
  ADD CONSTRAINT `users_activationmodel_user_id_id_9fcc4374_fk_accounts_user_id` FOREIGN KEY (`user_id_id`) REFERENCES `accounts_user` (`id`);

--
-- Constraints for table `users_passwordtokenmodel`
--
ALTER TABLE `users_passwordtokenmodel`
  ADD CONSTRAINT `users_passwordtokenmodel_user_id_id_3eac01f9_fk_accounts_user_id` FOREIGN KEY (`user_id_id`) REFERENCES `accounts_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
