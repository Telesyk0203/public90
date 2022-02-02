# Установка і базові налаштування Percona Mysql server

1. Встановити Percona repository 
   
   ```
   # yum install https://repo.percona.com/yum/percona-release-latest.noarch.rpm
   ```
2. Перевірка доступності пакету
```
sudo percona-release setup ps80
* Disabling all Percona Repositories
* Enabling the Percona Server 8.0 repository
* Enabling the Percona Tools repository
<*> All done!
```
```
yum list | grep percona | grep server
percona-server-client.x86_64                8.0.26-16.1.el7            @ps-80-release-x86_64
percona-server-server.x86_64                8.0.26-16.1.el7            @ps-80-release-x86_64
percona-server-shared.x86_64                8.0.26-16.1.el7            @ps-80-release-x86_64
percona-server-shared-compat.x86_64         8.0.26-16.1.el7            @ps-80-release-x86_64
percona-server-debuginfo.x86_64             8.0.26-16.1.el7            ps-80-release-x86_64
percona-server-devel.x86_64                 8.0.26-16.1.el7            ps-80-release-x86_64
percona-server-rocksdb.x86_64               8.0.26-16.1.el7            ps-80-release-x86_64
percona-server-test.x86_64                  8.0.26-16.1.el7            ps-80-release-x86_64
percona-server-tokudb.x86_64                8.0.26-16.1.el7            ps-80-release-x86_64
```
3. Встановити MySQL 
```
yum install percona-server-server
```
4. `Ознайомлення з основними параметрами файлу конфігурації MYSQL (і всіма підключеними файлами)`
```
vim /etc/my.cnf
```
```
# Percona Server template configuration
#
# For advice on how to change settings please see
# http://dev.mysql.com/doc/refman/8.0/en/server-configuration-defaults.html

[mysqld]
#
# Remove leading # and set to the amount of RAM for the most important data
# cache in MySQL. Start at 70% of total RAM for dedicated server, else 10%.
# innodb_buffer_pool_size = 128M
#
# Remove the leading "# " to disable binary logging
# Binary logging captures changes between backups and is enabled by
# default. It's default setting is log_bin=binlog
# disable_log_bin
#
# Remove leading # to set options mainly useful for reporting servers.
# The server defaults are faster for transactions and fast SELECTs.
# Adjust sizes as needed, experiment to find the optimal values.
# join_buffer_size = 128M
# sort_buffer_size = 2M
# read_rnd_buffer_size = 2M
#
# Remove leading # to revert to previous value for default_authentication_plugin,
# this will increase compatibility with older clients. For background, see:
# https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_default_authentication_plugin
# default-authentication-plugin=mysql_native_password

datadir=/var/lib/mysql
socket=/var/lib/mysql/mysql.sock

log-error=/var/log/mysqld.log
pid-file=/var/run/mysqld/mysqld.pid
```
5. Налаштування автоматичного запуску сервісу systemctl
```
systemctl enable mysqld
```
6. Запуск MySQL  systemctl
```
systemctl start mysqld
```
7. Перевірка статусу сервісу та логи MYSQL
```
systemctl  status mysqld
```
```
Loaded: loaded (/usr/lib/systemd/system/mysqld.service; enabled; vendor preset: disabled)
   Active: active (running) since вт 2021-12-21 03:20:49 EST; 2 weeks 5 days ago
     Docs: man:mysqld(8)
           http://dev.mysql.com/doc/refman/en/using-systemd.html
 Main PID: 1009 (mysqld)
   Status: "Server is operational"
   CGroup: /system.slice/mysqld.service
           └─1009 /usr/sbin/mysqld
```
+ Перевірка логів
  
```
sudo less /var/log/mysqld.log
```
```
2021-12-06T11:59:29.878178Z 0 [System] [MY-013169] [Server] /usr/sbin/mysqld (mysqld 8.0.26-16) initializing of server in progress as process 1793
2021-12-06T11:59:29.888993Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
2021-12-06T11:59:31.175551Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
2021-12-06T11:59:32.297166Z 0 [Warning] [MY-013746] [Server] A deprecated TLS version TLSv1 is enabled for channel mysql_main
2021-12-06T11:59:32.297476Z 0 [Warning] [MY-013746] [Server] A deprecated TLS version TLSv1.1 is enabled for channel mysql_main
2021-12-06T11:59:32.311747Z 6 [Note] [MY-010454] [Server] A temporary password is generated for root@localhost: m+o<Gim+p5HY
2021-12-06T11:59:35.402565Z 0 [System] [MY-010116] [Server] /usr/sbin/mysqld (mysqld 8.0.26-16) starting as process 1838
2021-12-06T11:59:35.414389Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
2021-12-06T11:59:36.074864Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
2021-12-06T11:59:36.716390Z 0 [Warning] [MY-013746] [Server] A deprecated TLS version TLSv1 is enabled for channel mysql_main
2021-12-06T11:59:36.716673Z 0 [Warning] [MY-013746] [Server] A deprecated TLS version TLSv1.1 is enabled for channel mysql_main
2021-12-06T11:59:36.719819Z 0 [Warning] [MY-010068] [Server] CA certificate ca.pem is self signed.
2021-12-06T11:59:36.719965Z 0 [System] [MY-013602] [Server] Channel mysql_main configured to support TLS. Encrypted connections are now supported 
for this channel.
2021-12-06T11:59:36.820847Z 0 [System] [MY-010931] [Server] /usr/sbin/mysqld: ready for connections. Version: '8.0.26-16'  socket: '/var/lib/mysql
/mysql.sock'  port: 3306  Percona Server (GPL), Release 16, Revision 3d64165.
2021-12-06T11:59:36.820916Z 0 [System] [MY-011323] [Server] X Plugin ready for connections. Bind-address: '::' port: 33060, socket: /var/lib/mysql
/mysqlx.sock
2021-12-06T12:00:15.138258Z 0 [System] [MY-013172] [Server] Received SHUTDOWN from user <via user signal>. Shutting down mysqld (Version: 8.0.26-1
6).
2021-12-06T12:00:16.152056Z 0 [System] [MY-010910] [Server] /usr/sbin/mysqld: Shutdown complete (mysqld 8.0.26-16)  Percona Server (GPL), Release 
16, Revision 3d64165.
2021-12-06T12:00:28.082915Z 0 [System] [MY-010116] [Server] /usr/sbin/mysqld (mysqld 8.0.26-16) starting as process 1959
2021-12-06T12:00:28.096206Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
2021-12-06T12:00:28.754670Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
2021-12-06T12:00:29.182255Z 0 [Warning] [MY-013746] [Server] A deprecated TLS version TLSv1 is enabled for channel mysql_main
2021-12-06T12:00:29.182367Z 0 [Warning] [MY-013746] [Server] A deprecated TLS version TLSv1.1 is enabled for channel mysql_main
2021-12-06T12:00:29.187371Z 0 [Warning] [MY-010068] [Server] CA certificate ca.pem is self signed.
```
8. Знайти в лог-файлі тимчасовий парольі перевірити можливість підключення до Mysql (підключ клієнтом) 
Підключаємось до сервісу mysql подивитись стан unix і мережевих сокетів(в окремому терміналі screen, паралельно). Нижче наведені параметри для підключення.
```
# mysql -u root -p
# mysql -u root -h 127.0.0.1 -p
# mysql -u root -S /var/lib/mysql/mysql.sock -p
# mysql -u root -h 127.0.0.1 -P 3306 -p
```
+ Перегляд наявності підключення через файл-сокет 
```
ss -xap | grep mysql
```
```
u_str  LISTEN     0      70     /var/lib/mysql/mysqlx.sock 17020         
         * 0                                                             
u_str  LISTEN     0      128    /var/lib/mysql/mysql.sock 17023          
        * 0                                                              
u_str  ESTAB      0      0      /var/lib/mysql/mysql.sock 19478          
        * 19477                                                          
u_str  ESTAB      0      0       * 19477                 * 19478         
 users:(("mysql",pid=2175fd=3))
 ```
+ Перегляд наявності підключення п мережі 
```
ss -na | grep 3306 
```
```
tcp    LISTEN     0      128    [::]:3306               [::]:*           
                                                                         
tcp    LISTEN     0      70     [::]:33060              [::]:* 
```
9. Задати пароль можна для root (не забудь його) такими способами:
```
# mysqladmin -u root -p -S /var/lib/mysql/mysql.sock password '<new-password>'
# mysqladmin -u root -p -h `hostname` -P 3306 password '<new-password>'
# mysqladmin -u root -p -h <IP-ADDRESS> -P 3306 password '<new-password>'
```
___
## Робота з таблицями та базами даних
+  mysql> CREATE DATABASE `Users`;- створення бази даних ;
  ```
  mysql> CREATE DATABASE `Users`;
Query OK, 1 row affected (0.02 sec)
```
  
  + створення таблиці Accounts;
  ```
  create table `Accounts` 
(`id_account`int(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
`id` varchar (32) not null, 
`password` varchar(16) null,
`balance` decimal(15,5) not null default (0.00000),
`billing_model` tinyint not null default(0),
`id_customer` int(6) UNSIGNED not null default(0));
```
+ створення файлу для наповнення таблиці Accounts;
```
Insert into `Accounts`(`id`,`password`,`balance`, `id_customer`, `billing_model`)
values 
('000999123','123test',default, 1, 1),
('000999456', '123test',default, 1, 1),
('380441112233', 'ylxlab8',default, 2, 1),
('999610934091', null, 10.00000, 2, -1),
('998942226765', '1oyhptao', 10.00000, 2, -1),
('997127472771', '123test', default, 3, 1),
('000999123', 'plt0wf', default, 3, 1),
('000999456', 'xgmfy0', 10.00000, 2, 1 ),
('998819317344', null, 10.00000, 1, -1 );
```
+ __mysql> SHOW DATABASES;__ - вивести список баз даних;
```
mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| User               |
| Users              |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
6 rows in set (0.00 sec)
```
+ __mysql> DROP DATABASE `Users`;__ - видалити базу даних;
```
mysql> DROP DATABASE `Users`;
Query OK, 0 rows affected (0.02 sec)

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| User               |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)
```

## Файли конфігурацій MySQL сервера
+ __mysql --help | grep -A1 'Default options'__ -приклад  для пошуку файлів конфігурування

```mysql --help | grep -A1 'Default options'
Default options are read from the following files in the given order:
/etc/my.cnf /etc/mysql/my.cnf /usr/etc/my.cnf ~/.my.cnf 
```
/etc/my.cnf - файл глобальної конфігурації БД
```
 Percona Server template configuration
#
# For advice on how to change settings please see
# http://dev.mysql.com/doc/refman/8.0/en/server-configuration-defaults.html

[mysqld]
#
# Remove leading # and set to the amount of RAM for the most important data
# cache in MySQL. Start at 70% of total RAM for dedicated server, else 10%.
# innodb_buffer_pool_size = 128M
#
# Remove the leading "# " to disable binary logging
# Binary logging captures changes between backups and is enabled by
# default. It's default setting is log_bin=binlog
# disable_log_bin
#
# Remove leading # to set options mainly useful for reporting servers.
# The server defaults are faster for transactions and fast SELECTs.
# Adjust sizes as needed, experiment to find the optimal values.
# join_buffer_size = 128M
# sort_buffer_size = 2M
# read_rnd_buffer_size = 2M
#
# Remove leading # to revert to previous value for default_authentication_plugin,
# this will increase compatibility with older clients. For background, see:
# https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_default_authentication_plugin
# default-authentication-plugin=mysql_native_password

datadir=/var/lib/mysql
socket=/var/lib/mysql/mysql.sock

log-error=/var/log/mysqld.log
pid-file=/var/run/mysqld/mysqld.pid
[server]
validate_password.policy='LOW'
```

___
## Виконання запитів
 + Вивести всі облікові записи з порожніми паролями
  
```
mysql> select * from Accounts where password is null;
+------------+--------------+----------+----------+---------------+-------------+
| id_account | id           | password | balance  | billing_model | id_customer |
+------------+--------------+----------+----------+---------------+-------------+
|          4 | 999610934091 | NULL     | 10.00000 |            -1 |           2 |
|          9 | 998819317344 | NULL     | 10.00000 |            -1 |           1 |
+------------+--------------+----------+----------+---------------+-------------+
2 rows in set (0,00 sec)
```
+ Вивести всі акаунти id починається з 0
```
  mysql> select * from Accounts where id like '0%';
+------------+-----------+----------+----------+---------------+-------------+
| id_account | id        | password | balance  | billing_model | id_customer |
+------------+-----------+----------+----------+---------------+-------------+
|          1 | 000999123 | 123test  |  0.00000 |             1 |           1 |
|          2 | 000999456 | 123test  |  0.00000 |             1 |           1 |
|          7 | 000999123 | plt0wf   |  0.00000 |             1 |           3 |
|          8 | 000999456 | xgmfy0   | 10.00000 |             1 |           2 |
+------------+-----------+----------+----------+---------------+-------------+
4 rows in set (0,00 sec)
```
+ Вивести Customer які мають в імені "Test" як підрядок.
```
mysql> select * from Customers where name like '%Test%';
+-------------+-------------------------+-----------+---------+
| id_customer | name                    | firstname | balance |
+-------------+-------------------------+-----------+---------+
|           1 | zzzPortaTestCustomer    | NULL      | 0.00000 |
|           3 | zzzPortaTestCustomerZZZ | NULL      | 0.00000 |
+-------------+-------------------------+-----------+---------+
2 rows in set (0,00 sec)
```
+ * Вивести імена Customers у кого є акаунти з billing_model = -1 (потрібний підзапит)
```
mysql> select * from Customers where id_customer  in (select id_customer from Accounts where billing_model=-1);
+-------------+----------------------+-----------+---------+
| id_customer | name                 | firstname | balance |
+-------------+----------------------+-----------+---------+
|           1 | zzzPortaTestCustomer | NULL      | 0.00000 |
|           2 | John                 | John      | 0.00000 |
+-------------+----------------------+-----------+---------+
2 rows in set (0,00 sec)
```
+ Підрахувати число облікових записів для кожного Customer( ім'я, число облікових записів)* потрібно використовувати JOIN
```
mysql> select name, count(id_account) from Customers c join Accounts a on c.id_customer=a.id_customer group by c.name ;
+-------------------------+-------------------+
| name                    | count(id_account) |
+-------------------------+-------------------+
| zzzPortaTestCustomer    |                 3 |
| John                    |                 4 |
| zzzPortaTestCustomerZZZ |                 2 |
+-------------------------+-------------------+
3 rows in set (0,00 sec)

```
___
## Налаштування Mysql та реезервне копіювання (backup)
Налаштування MySQL
+ Знайдіть файли конфігурації MySQL у вашій системі.

+ Вивчіть їх структуру і знайдіть всі секції (деякі секції можуть бути в файлах, що підключаються).

+ Запустіть та підключіться до MySQL.

+ Знайдіть значення опції validate_password.policy


Як подивитися значення опції\змінної?

`mysql> SHOW VARIABLES LIKE 'validate_password.policy';`

+ Знайдіть значення всіх опцій, що стосуються validate_password.

Як переглянути значення групи змінних?

`mysql> SHOW VARIABLES LIKE 'validate_password.%';`

+ Встановіть значення опції validate_password.policy у значення LOW. Переконайтеся, що вона змінилася. 
```
mysql> set global validate_password.policy = LOW;
Query OK, 0 rows affected (0,00 sec)
```
```
mysql> SHOW VARIABLES LIKE 'validate_password.%';
+--------------------------------------+-------+
| Variable_name                        | Value |
+--------------------------------------+-------+
| validate_password.check_user_name    | ON    |
| validate_password.dictionary_file    |       |
| validate_password.length             | 8     |
| validate_password.mixed_case_count   | 1     |
| validate_password.number_count       | 1     |
| validate_password.policy             | LOW   |
| validate_password.special_char_count | 1     |
+--------------------------------------+-------+
7 rows in set (0,01 sec)
```

+ Перезапустіть сервіс, перевірте значення опції. Зробіть висновок.

+ Задайте політику validate_password.policy у конфігураційному файлі  `/etc/mysql/mysql.conf.d/mysqld.cnf 
` у відповідній секції.
```
[mysqld]
validate_password.policy=STRONG
```

+ Перевірте значення опції до та після перезавантаження сервісу. Зробіть висновок.

 + Додайте опцію, яка зменшить обов'язкову кількість символів у паролі до 5.
```
[mysqld]

validate_password.length=5
```

+ Запустіть сервер на нестандартному порту (3307). Спробуйте підключитися до сервера (із портом і без).
Змініть локальні установки клієнта в конфігураційному файлі користувача.
Спробуйте підключитися до сервера (із портом і без).
Поверніть стандартний порт.

___
## Створення резервної копії бази даних
+ Збережіть структуру БД (без даних) у файл Dump1.sql.
```
sudo mysqldump -p VoiCompany --no-data> Dump1.sql
```
 + Вивчіть вміст файлу. Проінспектуйте файл командою файлу. 

 + Збережіть вміст БД у файл Dump2.sql з опцією дропа бази даних.
```
sudo mysqldump -p --no-create-info --add-drop-database VoiCompany > Dump2.sql
```

+ Вивчіть вміст файлу. Проінспектуйте файл командою файлу.

+ Збережіть структуру БД + дані у файл конвеєром через gzip Dump3.sql.gz
```
sudo mysqldump -p --databases VoiCompany | gzip > Dump3.sql.gz
```
+ Вивчіть вміст файлу. Проінспектуйте файл командою файлу.


+ Спробуйте завантажити вміст файлу Dump1.sql
```
mysql < "name of dump file"
```
+ Завантажте вміст файлу Dump2.sql. Перегляньте вміст БД.
```
sudo mysql -p VoiCompany < Dump2.sql
```
+ Видаліть БД.
```
mysql> drop database VoiCompany;                                          
Query OK, 2 rows affected (0,04 sec) 
```

+ Завантажте вміст файлу Dump3.sql. Перегляньте вміст БД.
```
gunzip < Dump3.sql.gz | sudo mysql -p
```

+ Збережіть вміст таблиці Accounts. У файл повинні потрапити лише акаунти, у яких не встановлено пароль.
```
sudo mysqldump -p --databases VoiCompany --tables Accounts --where="password is null" > Dump6.sql
```
___
## Користувачі та привілеї MySQL
+ Завантажте дамп бази rating.sql на встановлений сервер MySQL.
```
sudo mysql -p VoiCompany < rating.sql
```
+ Створіть нового користувача з наступними параметрами:

ім'я користувача – test;
хост – 127.0.0.1;
пароль – "test123".
```
create user 'test'@'127.0.0.1' identified by 'test123';
Query OK, 0 rows affected (0,02 sec)

```
Підказка з password_policy

+ Запит на перегляд користувача

select * from mysql.user where User = 'test'\G

+ Дайте вашому користувачеві всі привілеї, зокрема. "grant option". Привілеї мають поширюватися лише на таблиці бази даних "rating".
```
mysql> GRANT ALL ON Rating.* TO 'test'@'127.0.0.1' WITH GRANT OPTION;
Query OK, 0 rows affected (0,07 sec)
```
+ Перевірте результат командою: show grants for <користувач>@<хост>
```
mysql> show grants for 'test'@'127.0.0.1';
+----------------------------------------------------------------------------+
| Grants for test@127.0.0.1                                                  |
+----------------------------------------------------------------------------+
| GRANT USAGE ON *.* TO `test`@`127.0.0.1`                                   |
| GRANT ALL PRIVILEGES ON `Rating`.* TO `test`@`127.0.0.1` WITH GRANT OPTION |
+----------------------------------------------------------------------------+
2 rows in set (0,00 sec)
```

+ sЗробіть запити до таблиць "db", "tables_priv" та "columns_priv" бази даних mysql.

+ Дайте вашому користувачеві привілеї на вибірку та внесення записів у таблицю "Rating".
```
mysql> GRANT SELECT, UPDATE ON mysql.db TO 'test'@'127.0.0.1';
Query OK, 0 rows affected (0,01 sec)

mysql> GRANT SELECT, UPDATE ON mysql.tables_priv TO 'test'@'127.0.0.1';
Query OK, 0 rows affected (0,01 sec)

mysql> GRANT SELECT, UPDATE ON mysql.columns_priv TO 'test'@'127.0.0.1';
Query OK, 0 rows affected (0,00 sec)
```

+ Зробіть запити до таблиць "db", "tables_priv" та "columns_priv" бази даних mysql.

`Вибірка має стосуватися лише користувача 'test'@'127.0.0.1'.`
```
mysql> select * from tables_priv where User='test' \G;
*************************** 1. row ***************************
       Host: 127.0.0.1
         Db: mysql
       User: test
 Table_name: columns_priv
    Grantor: root@localhost
  Timestamp: 0000-00-00 00:00:00
 Table_priv: Select,Update
Column_priv: 
*************************** 2. row ***************************
       Host: 127.0.0.1
         Db: mysql
       User: test
 Table_name: db
    Grantor: root@localhost
  Timestamp: 0000-00-00 00:00:00
 Table_priv: Select,Update
Column_priv: 
*************************** 3. row ***************************
       Host: 127.0.0.1
         Db: mysql
       User: test
 Table_name: tables_priv
    Grantor: root@localhost
  Timestamp: 0000-00-00 00:00:00
 Table_priv: Select,Update
Column_priv: 
3 rows in set (0,01 sec)

ERROR: 
No query specified
```
```
ysql> select * from db where User='test' \G;
*************************** 1. row ***************************
                 Host: 127.0.0.1
                   Db: Rating
                 User: test
          Select_priv: Y
          Insert_priv: Y
          Update_priv: Y
          Delete_priv: Y
          Create_priv: Y
            Drop_priv: Y
           Grant_priv: Y
      References_priv: Y
           Index_priv: Y
           Alter_priv: Y
Create_tmp_table_priv: Y
     Lock_tables_priv: Y
     Create_view_priv: Y
       Show_view_priv: Y
  Create_routine_priv: Y
   Alter_routine_priv: Y
         Execute_priv: Y
           Event_priv: Y
         Trigger_priv: Y
1 row in set (0,01 sec)

ERROR: 
No query specified
```


+ Підключіться до сервера MySQL з даними користувача test з локальної консолі на ім'я (localhost), по IP (127.0.0.1) та з віддаленого сервера.
```
sudo mysql -u test -h 127.0.0.1 -p 
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 10
Server version: 8.0.27-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 
```
+ Під користувачем test продивіться список баз даних на сервері, перегляньте список таблиць rating та mysql
```
show tables in mysql;
show tables in rating;
```
```
mysql> show tables in mysql;
+-----------------+
| Tables_in_mysql |
+-----------------+
| columns_priv    |
| db              |
| tables_priv     |
+-----------------+
3 rows in set (0,00 sec)

mysql> show tables in Rating;
+------------------+
| Tables_in_Rating |
+------------------+
| Movie            |
| Rating           |
| Reviewer         |
+------------------+
3 rows in set (0,00 sec)
```
+ Перезайдіть в БД від імені суперкористувача і спробуйте зняти з користувача "test" наступні привілеї:
```
sudo mysql -u root -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 12
Server version: 8.0.27-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 
```

### 1. drop на всі таблиці баз даних "rating"
```
mysql> REVOKE DROP ON Rating.* FROM 'test'@'127.0.0.1';
Query OK, 0 rows affected (0,01 sec)
```
+ Перейдіть на БД "mysql". Зробіть запити до таблиць "db", "tables_priv" та "columns_priv".Вибірка має стосуватися лише користувача 'test'@'127.0.0.1'.
`Перевірте результат командою: show grants for <користувач>@<хост>`
```
mysql> select * from db where User='test' \G;
*************************** 1. row ***************************
                 Host: 127.0.0.1
                   Db: Rating
                 User: test
          Select_priv: Y
          Insert_priv: Y
          Update_priv: Y
          Delete_priv: Y
          Create_priv: Y
            Drop_priv: N
           Grant_priv: Y
      References_priv: Y
           Index_priv: Y
           Alter_priv: Y
Create_tmp_table_priv: Y
     Lock_tables_priv: Y
     Create_view_priv: Y
       Show_view_priv: Y
  Create_routine_priv: Y
   Alter_routine_priv: Y
         Execute_priv: Y
           Event_priv: Y
         Trigger_priv: Y
1 row in set (0,00 sec)

ERROR: 
No query specified

mysql> 
```
```
mysql> show grants for 'test'@'127.0.0.1'\G;
*************************** 1. row ***************************
Grants for test@127.0.0.1: GRANT USAGE ON *.* TO `test`@`127.0.0.1`
*************************** 2. row ***************************
Grants for test@127.0.0.1: GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, REFERENCES, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, EVENT, TRIGGER ON `Rating`.* TO `test`@`127.0.0.1` WITH GRANT OPTION
*************************** 3. row ***************************
Grants for test@127.0.0.1: GRANT SELECT, UPDATE ON `mysql`.`columns_priv` TO `test`@`127.0.0.1`
*************************** 4. row ***************************
Grants for test@127.0.0.1: GRANT SELECT, UPDATE ON `mysql`.`db` TO `test`@`127.0.0.1`
*************************** 5. row ***************************
Grants for test@127.0.0.1: GRANT SELECT, UPDATE ON `mysql`.`tables_priv` TO `test`@`127.0.0.1`
5 rows in set (0,00 sec)
```


### 2.зміна структури таблиці "Rating"
+ Перейдіть на БД "mysql". Зробіть запити до таблиць "db", "tables_priv" та "columns_priv".Вибірка має стосуватися лише користувача 'test'@'127.0.0.1'.
`Перевірте результат командою: show grants for <користувач>@<хост> (зробіть висновок)`
```
mysql> REVOKE ALTER ON Rating.Rating FROM 'test'@'127.0.0.1';
Query OK, 0 rows affected (0,00 sec)
```

* Заборонити виведення колонки "mID" таблиці "Rating".
Перейдіть на БД "mysql". Зробіть запити до таблиць "db", "tables_priv" та "columns_priv".
Вибірка має стосуватися лише користувача 'test'@'127.0.0.1'.
Перевірте результат командою: show grants for <користувач>@<хост>
## LaB
+ Create a dump of the table 'city' and mention there only cities with population of more or equal than a million people.
Give it a name 'big.sql'.
```
sudo mysql new_world < big.sql
```
+ Create a table 'big_country' in the new DB based on the table 'country' from 'world' DB with mentioning only countries with population of more than 200 million people. Use only one SQL-query for this.
```
sudo mysqldump --databases world --tables country --where="Population >200000000" > big2.sql
```
```
nano big2.sql
```
```

Data Base: rating.sql

Exercises:

1. Find the titles of all movies directed by Steven Spielberg.
[Найдите названия всех фильмов режиссера Стивена Спилберга]

2. Find all years that have a movie that received a rating of 4 or 5, and sort them in increasing order.
[Найдите все года, в которых был выпущен фильм получивший оценку 4 или 5, и отсортируйте их в порядке возрастания]

3. Find the titles of all movies that have no ratings.
[Найдите названия всех фильмов, которые не получили никакую оценку]

4. Some reviewers didn't provide a date with their rating. Find the names of all reviewers who have ratings with a NULL value for the date.
[Некоторые критики не предоставили дату, когда была поставлена оценка. Найдите имена всех критиков, у которых есть оценки и значение даты NULL]

5. Write a query to return the ratings data in a more readable format: reviewer name, movie title, stars, and ratingDate. Also, sort the data, first by reviewer name, then by movie title, and lastly by number of stars.
[Напишите запрос, который возвращает данные об оценках в более читабельном формате: reviewer name, movie title, stars и ratingDate. Также, отсортируйте данные сперва по  имени критика, затем по названию фильма и в конце по рейтингу]

6. * For all cases where the same reviewer rated the same movie twice and gave it a higher rating the second time, return the reviewer's name and the title of the movie.
[Для всех случаев, когда один и тот же критик оценил один фильм дважды и дал ему во второй раз выше оценку чем в первый, выведите имя критика и название фильма]

7. For each movie that has at least one rating, find the highest number of stars that movie received. Return the movie title and number of stars. Sort by movie title.
[Для каждого фильма, у которого есть хотя бы одна оценка, найдите наибольшее количество звезд, которые фильм получил. Выведите название фильма и количество звезд. Отсортируйте их по названию фильма]

8. For each movie, return the title and the 'rating spread', that is, the difference between highest and lowest ratings given to that movie. Sort by rating spread from highest to lowest, then by movie title.
[Для каждого фильма выведите название и "разницу в оценке”, то есть разницу между наивысшей и наинизшей оценках, которые получал фильм. Отсортируйте по этой разнице от наивысшей до самой низкой, а потом по названию фильма]

9. ** Find the difference between the average rating of movies released before 1980 and the average rating of movies released after 1980. (Make sure to calculate the average rating for each movie, then the average of those averages for movies before 1980 and movies after. Don't just calculate the overall average rating before and after 1980.)
[Найдите разницу между средней оценкой фильмов, выпущенных до 1980 года и средней оценкой фильмов, выпущенных после 1980 года. (Убедитесь, что вы посчитали среднюю оценку для каждого фильма, потом среднее значение этих средних значений для фильмов, выпущенных до и после 1980 года. А не просто подсчитайте общую среднюю оценку до и после 1980 года)]


SQL Movie-Rating Modification Exercises

1. Add the reviewer Roger Ebert to your database, with an rID of 209.
[Добавьте критика Roger Ebert в Вашу базу данных с rID - 209]

2. Insert 5-star ratings by James Cameron for all movies in the database. Leave the review date as NULL.
[Вставьте оценку 5, выставленную James Cameron, для всех фильмов в базе данных. Оставьте дату выставления оценки NULL]

3. For all movies that have an average rating of 4 stars or higher, add 25 to the release year. (Update the existing tuples; don't insert new tuples.)
[Для всех фильмов, у которых средняя оценка 4 или выше, добавьте 25 к году выпуска. (Используйте update, а не insert)]

 