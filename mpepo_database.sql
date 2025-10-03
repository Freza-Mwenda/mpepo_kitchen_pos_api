-- MySQL dump 10.13  Distrib 9.4.0, for macos14.7 (x86_64)
--
-- Host: localhost    Database: prod_mpepo_db
-- ------------------------------------------------------
-- Server version	9.2.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `invoice_logs`
--

DROP TABLE IF EXISTS `invoice_logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `invoice_logs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `order_id` varchar(50) NOT NULL,
  `invoice_data` json NOT NULL,
  `submission_status` varchar(20) DEFAULT NULL,
  `tax_authority_response` json DEFAULT NULL,
  `submitted_at` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_invoice_logs_order_id` (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invoice_logs`
--

LOCK TABLES `invoice_logs` WRITE;
/*!40000 ALTER TABLE `invoice_logs` DISABLE KEYS */;
INSERT INTO `invoice_logs` VALUES (1,'50e0b660-daff-45c2-9f3e-3a8083a7faea','{\"items\": [{\"quantity\": 1, \"tax_code\": \"A\", \"tax_amount\": 0.9584, \"unit_price\": 5.99, \"description\": \"French Fries\", \"total_amount\": 5.99}, {\"quantity\": 1, \"tax_code\": \"A\", \"tax_amount\": 0.72, \"unit_price\": 4.5, \"description\": \"Lemonade\", \"total_amount\": 4.5}], \"summary\": {\"total\": 12.17, \"currency\": \"KES\", \"subtotal\": 10.49, \"tax_amount\": 1.68}, \"buyer_info\": {\"tin\": \"000000000\", \"name\": \"Retail Customer\", \"address\": \"Walk-in Customer\"}, \"issue_date\": \"2025-10-03T20:06:25\", \"seller_info\": {\"tin\": \"P051234567L\", \"name\": \"Mpepo Kitchen\", \"address\": \"Nairobi, Kenya\"}, \"tax_breakdown\": {\"vat_rate\": 0.16, \"vat_amount\": 1.68}, \"invoice_number\": \"MPEPO-50e0b660-daff-45c2-9f3e-3a8083a7faea\"}','pending',NULL,NULL,'2025-10-03 20:06:27');
/*!40000 ALTER TABLE `invoice_logs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `id` varchar(50) NOT NULL,
  `items` json NOT NULL,
  `subtotal` decimal(10,2) NOT NULL,
  `tax_amount` decimal(10,2) NOT NULL,
  `discount_amount` decimal(10,2) DEFAULT NULL,
  `total` decimal(10,2) NOT NULL,
  `status` varchar(20) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `tax_authority_ref` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_orders_id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES ('50e0b660-daff-45c2-9f3e-3a8083a7faea','[{\"product\": {\"id\": \"3\", \"name\": \"French Fries\", \"price\": 5.99, \"category\": \"Side Dish\", \"image_url\": \"https://becs-table.com.au/wp-content/uploads/2014/01/ice-cream-1.jpg\", \"description\": \"Crispy golden fries with seasoning\"}, \"quantity\": 1}, {\"product\": {\"id\": \"10\", \"name\": \"Lemonade\", \"price\": 4.5, \"category\": \"Beverage\", \"image_url\": \"https://becs-table.com.au/wp-content/uploads/2014/01/ice-cream-1.jpg\", \"description\": \"Freshly squeezed lemonade with mint\"}, \"quantity\": 1}]',10.49,1.68,0.00,12.17,'completed','2025-10-03 20:06:25','KRA-REF-FC649F07E2AC');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `id` varchar(50) NOT NULL,
  `name` varchar(100) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `category` varchar(50) NOT NULL,
  `description` text,
  `image_url` varchar(10000) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `is_active` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_products_id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES ('1','Grilled Chicken',18.99,'Main Course','Juicy grilled chicken with herbs and spices','https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQuBkZLiOpt0tSb3fhdk_lek5yXHWoNdKvwQDMnbtCEBNVbFIPyekMlFNeh0mdKbqWOYFQLuKBGMwLS9vmd9ceQWQUTdQT63IBha5L89w','2025-10-03 19:58:38',1),('10','Lemonade',4.50,'Beverage','Freshly squeezed lemonade with mint','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQcoXWLIiYs_u54dOx8J_1DpCZNKBKcQJe0A&s','2025-10-03 19:58:38',1),('2','Beef Burger',15.99,'Main Course','Classic beef burger with cheese and vegetables','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQcoXWLIiYs_u54dOx8J_1DpCZNKBKcQJe0A&s','2025-10-03 19:58:38',1),('2411433e-a2f4-4cd5-982b-c7b0a5cdd56d','Kapenta',75.00,'Food','Kapenta Na Nshima','https://www.gimmesomeoven.com/wp-content/uploads/2018/06/How-To-Cook-Whole-Fish-In-The-Oven-Baked-Roastted-Mahi-Mahi-Recipe-2.jpg','2025-10-03 20:17:21',1),('3','French Fries',5.99,'Side Dish','Crispy golden fries with seasoning','https://i0.wp.com/www.lubzonline.com/wp-content/uploads/2021/12/131980110_691132031599382_7883691975085799914_o-1024x804-1.jpg?fit=750%2C589&ssl=1','2025-10-03 19:58:38',1),('4','Greek Salad',12.99,'Salad','Fresh vegetables with feta cheese and olive oil','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQcoXWLIiYs_u54dOx8J_1DpCZNKBKcQJe0A&s','2025-10-03 19:58:38',1),('5','Coca Cola',3.99,'Beverage','Cold refreshing carbonated drink','https://i0.wp.com/www.lubzonline.com/wp-content/uploads/2021/12/131980110_691132031599382_7883691975085799914_o-1024x804-1.jpg?fit=750%2C589&ssl=1','2025-10-03 19:58:38',1),('6','Ice Cream',6.99,'Dessert','Vanilla ice cream with chocolate sauce','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQcoXWLIiYs_u54dOx8J_1DpCZNKBKcQJe0A&s','2025-10-03 19:58:38',1),('7','Chicken Wings',11.99,'Appetizer','Spicy chicken wings with dip sauce','https://i0.wp.com/www.lubzonline.com/wp-content/uploads/2021/12/131980110_691132031599382_7883691975085799914_o-1024x804-1.jpg?fit=750%2C589&ssl=1','2025-10-03 19:58:38',1),('8','Pasta Carbonara',14.99,'Main Course','Creamy pasta with bacon and parmesan','https://www.zimbokitchen.com/wp-content/uploads/2022/06/MINCE-PASTA-3-750x500.jpg','2025-10-03 19:58:38',1),('9','Chocolate Cake',7.99,'Dessert','Rich chocolate cake with ganache','https://i0.wp.com/www.lubzonline.com/wp-content/uploads/2021/12/131980110_691132031599382_7883691975085799914_o-1024x804-1.jpg?fit=750%2C589&ssl=1','2025-10-03 19:58:38',1),('e36f0b7f-8a6e-40eb-87a3-6416bb7b645d','Nshima',15.00,'Main Dish','Plain Nshima','https://miro.medium.com/1*LRUnVOaJ1mTidrBXUCFFkA.png','2025-10-03 20:04:47',0);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `full_name` varchar(100) NOT NULL,
  `role` varchar(20) DEFAULT NULL,
  `is_active` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `last_login` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `ix_users_username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'prod_mpepo_db'
--

--
-- Dumping routines for database 'prod_mpepo_db'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-03 23:19:12
