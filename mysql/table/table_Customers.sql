create table `Customers` 
(`id_customer`int(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
`name` varchar (41) null, 
`firstname` varchar(25) null,
`balance` decimal(15,5) not null default (0.00000);