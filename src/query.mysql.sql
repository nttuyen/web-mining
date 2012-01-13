CREATE TABLE `url_queue` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `url` varchar(255) NOT NULL,
  `refer` varchar(500) DEFAULT NULL,
  `crawled` tinyint(1) DEFAULT '0',
  `data` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `url-unique` (`url`) USING HASH
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8;

