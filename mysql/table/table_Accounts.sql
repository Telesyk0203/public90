create table `Accounts` 
(`id_account`int(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
`id` varchar (32) not null, 
`password` varchar(16) null,
`balance` decimal(15,5) not null default (0.00000),
`billing_model` tinyint not null default(0),
`id_customer` int(6) UNSIGNED not null default(0));