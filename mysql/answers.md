# Assignment: Робота  з MySQL
1. How to install MySQL-client on OL8?
+ Set Percona repository
```
 yum install https://repo.percona.com/yum/percona-release-latest.noarch.rpm
```
+  Check allowed packages
```
sudo percona-release setup ps80
yum list | grep percona | grep server
```

+ Install MySQL
```
yum install percona-server-server
```
2. How to connect to MySQL through Unix-socket?
```
mysql -u root -p
mysql -u root -S /var/lib/mysql/mysql.sock -p
```

3. Is it possible to connect to MySQL via Unix-socket from another host? Why/How?

> Yes, it`s possible

4. What table defines users and their global privileges? What database contains this table?
```
mysql> select * from mysql.user  where user='root' \G;
*************************** 1. row ***************************
                    Host: localhost
                    User: root
             Select_priv: Y
             Insert_priv: Y
             Update_priv: Y
             Delete_priv: Y
             Create_priv: Y
               Drop_priv: Y
             Reload_priv: Y
           Shutdown_priv: Y
            Process_priv: Y
               File_priv: Y
              Grant_priv: Y
         References_priv: Y
              Index_priv: Y
              Alter_priv: Y
            Show_db_priv: Y
              Super_priv: Y
   Create_tmp_table_priv: Y
        Lock_tables_priv: Y
            Execute_priv: Y
         Repl_slave_priv: Y
        Repl_client_priv: Y
        Create_view_priv: Y
          Show_view_priv: Y
     Create_routine_priv: Y
      Alter_routine_priv: Y
        Create_user_priv: Y
              Event_priv: Y
            Trigger_priv: Y
  Create_tablespace_priv: Y
                ssl_type: 
              ssl_cipher: 0x
             x509_issuer: 0x
            x509_subject: 0x
           max_questions: 0
             max_updates: 0
         max_connections: 0
    max_user_connections: 0
                  plugin: auth_socket
   authentication_string: 
        password_expired: N
   password_last_changed: 2022-01-12 08:20:27
       password_lifetime: NULL
          account_locked: N
        Create_role_priv: Y
          Drop_role_priv: Y
  Password_reuse_history: NULL
     Password_reuse_time: NULL
Password_require_current: NULL
         User_attributes: NULL
1 row in set (0,00 sec)

ERROR: 
No query specified
```

5. Write all necessary commands to create a user 'test_user' which will have SELECT and UPDATE privileges to database 'test_db' from 192.168.0.100 with password 'my_pass'.
```
mysql> CREATE USER 'test'@'192.168.0.100' identified by 'my_pass';
```
```
GRANT SELECT, UPDATE ON test_db.* TO 'test'@'192.168.0.100';
```

Describe as many variants as possible.

6. At PortaSwitch server:
```
mysql> show tables from porta-billing;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '-billing' at line 1
```
+ Why this query doesn't work?
> Because right query is : 
```
mysql> use porta-billing; show tables;
```
7. What's wrong with the query?
```
mysql> SET PASSWORD FOR ''@'localhost' = ('newpwd');
```
```
mysql> SET PASSWORD FOR 'test'@'127.0.0.1' = '123test';
Query OK, 0 rows affected (0,01 sec)
```
> `'newpwd' have to be without () parentheses`

8. How to connect to a remote MySQL-server 192.168.0.1, where mysqld listens to the port 3308, with user 'test_user' and password 'test_password'?
```
mysql -u test_user -h 192.168.0.1 -P 3308 -p'test_password'   
```

9. How to find out location of mysql socket file?
```
 ss  -xap | grep mysql
u_str              LISTEN              0                    70                                                                      /var/run/mysqld/mysqlx.sock 643098                                                * 0                                                                                                       
u_str              LISTEN              0                    151                                                                     /var/run/mysqld/mysqld.sock 643100                                                * 0          
```

10. What will you do if:
```
[root@localhost shandr]# mysql -u root
ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/lib/mysql/mysql.sock' (2)
```
> Restart mysql.sevice 
```
systemctl restart mysql.service 
```
and after 
```
# mysql 
```

11. How to find a port that MySQL-server listens to?
```
ss -na | grep 3306
nl                UNCONN                 0                   0                                                                                               15:-1497913306                                   *                                 
nl                UNCONN                 0                   0                                                                                               15:-1497913306                                   *                                 
tcp               LISTEN                 0                   70                                                                                       127.0.0.1:33060                                  0.0.0.0:*                                
tcp               LISTEN                 0                   151                                                                                      127.0.0.1:3306                *  
```


12. What '\c' statement is used for?
 > '\c' statement is used for reject query that you want stdin

13. How to get an information about 'grant' usage?
```
mysql> show grants for 'test'@'127.0.0.1' \G;
*************************** 1. row ***************************
Grants for test@127.0.0.1: GRANT USAGE ON *.* TO `test`@`127.0.0.1`
```
```
mysql> select * from mysql.user where User='test' \G;
*************************** 1. row ***************************
                    Host: 127.0.0.1
                    User: test
             Select_priv: N
             Insert_priv: N
             Update_priv: N
             Delete_priv: N
             Create_priv: N
               Drop_priv: N
             Reload_priv: N
           Shutdown_priv: N
            Process_priv: N
               File_priv: N
              Grant_priv: N
         References_priv: N
              Index_priv: N
              Alter_priv: N
            Show_db_priv: N
              Super_priv: N
   Create_tmp_table_priv: N
        Lock_tables_priv: N
            Execute_priv: N
         Repl_slave_priv: N
        Repl_client_priv: N
        Create_view_priv: N
          Show_view_priv: N
     Create_routine_priv: N
      Alter_routine_priv: N
        Create_user_priv: N
              Event_priv: N
            Trigger_priv: N
  Create_tablespace_priv: N
                ssl_type: 
              ssl_cipher: 0x
             x509_issuer: 0x
            x509_subject: 0x
           max_questions: 0
             max_updates: 0
         max_connections: 0
    max_user_connections: 0
                  plugin: caching_sha2_password
   authentication_string: $A$005$mb7I\&nW'}XOGl5fw97/Ncnh0gqWatUiKgd2c8W6ZS/9VChTkNCt86C
        password_expired: N
   password_last_changed: 2022-02-02 12:35:37
       password_lifetime: NULL
          account_locked: N
        Create_role_priv: N
          Drop_role_priv: N
  Password_reuse_history: NULL
     Password_reuse_time: NULL
Password_require_current: NULL
         User_attributes: NULL
1 row in set (0,00 sec)

ERROR: 
No query specified
```

14. Specify a data type for "12345”.
> "12345" - CHAR,  because it's not digits it's statement 

15. What is the best data type for column which will store string data with length from 10 to 100 characters?
> VARCHAR 

16. How to set utf8 character set for clients?
> add the following to my.cnf/my.ini
```
[client]
default-character-set=utf8mb4
```
17.  Create table with "laptop" with such columns:

manufacturer
CPU speed(GHz)
release_date
broken(y/n)
owner(name and surname)
```
create table `Accounts` 
(`id_account`int(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
`id` varchar (32) not null, 
`password` varchar(16) null,
`balance` decimal(15,5) not null default (0.00000),
`billing_model` tinyint not null default(0),
`id_customer` int(6) UNSIGNED not null default(0));
```
```
mysql> desc laptop;
+-------------------------+------------------+------+-----+---------+----------------+
| Field                   | Type             | Null | Key | Default | Extra          |
+-------------------------+------------------+------+-----+---------+----------------+
| id                      | int unsigned     | NO   | PRI | NULL    | auto_increment |
| manufacturer            | varchar(32)      | YES  |     | NULL    |                |
| CPU speed(GHz)          | decimal(15,5)    | NO   |     | NULL    |                |
| release_date            | varchar(16)      | YES  |     | NULL    |                |
| broken(y/n)             | enum('yes','no') | NO   |     | NULL    |                |
| owner(name and surname) | varchar(64)      | YES  |     | NULL    |                |
+-------------------------+------------------+------+-----+---------+----------------+
6 rows in set (0,00 sec)

```

18. Load some data to created above table with help of INSERT, LOAD DATA, and source commands.
```
mysql> select * from laptop;
+----+--------------+----------------+--------------+-------------+-------------------------+
| id | manufacturer | CPU speed(GHz) | release_date | broken(y/n) | owner(name and surname) |
+----+--------------+----------------+--------------+-------------+-------------------------+
|  1 | HP           |        5.20000 | 20.03.2020   | no          |  Dead Pool              |
+----+--------------+----------------+--------------+-------------+-------------------------+
1 row in set (0,00 sec)
```
```
Insert into `laptop`(`manufacturer`,`CPU speed(GHz)`, `release_date`, `broken(y/n)`, `owner(name and surname)`)
values  
('HP', 5.200, '20.03.2020', 'no',' Dead Pool');
```

19. What command should be used to dump porta-billing database to porta.sql file?
> mysqldump -p porta-billing > porta.sql

20. How to create the same table as porta-billing.Customers?
> mysqldump -p --databases porta-billing --tables Customers > porta.sql
21. How to check ENGINE of some table?
```
mysql> SELECT ENGINE FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'Rating' AND TABLE_NAME = 'Rating';
+--------+
| ENGINE |
+--------+
| InnoDB |
+--------+
1 row in set (0,00 sec)
```
22. Choose amount of RAM for innodb_buffer_pool_size parameter if server has 20G RAM and it is dedicated DB server.
    
> With this output, you would set the following in /etc/my.cnf
```
[mysqld]
innodb_buffer_pool_size=8G
```