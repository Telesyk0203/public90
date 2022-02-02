create table `laptop` 
(`id`int(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
`manufacturer` varchar(32) , 
`CPU speed(GHz)` decimal(15,5) not null, 
`release_date` varchar(16) null,
`broken(y/n)` enum('yes', 'no') not null,
`owner(name and surname)` varchar(64));