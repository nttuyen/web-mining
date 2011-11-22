CREATE TABLE `url_queue` (
`id`  bigint NOT NULL ,
`url`  varchar(250) NOT NULL ,
`refer`  varchar(255) NULL ,
`crawled`  tinyint NULL DEFAULT 0 ,
PRIMARY KEY (`id`),
UNIQUE INDEX `url-unique` (`url`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8
;