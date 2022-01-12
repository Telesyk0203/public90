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
4. Ознайомлення з основними параметрами файлу конфігурації MYSQL (і всіма підключеними файлами)
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
1. 