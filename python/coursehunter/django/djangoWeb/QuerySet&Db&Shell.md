# QuerySet
+ Запускаєм віртуальне серодровище 
  __cd venv\Scripts__

```
activate python.exe
```
+ Вхід інтерактивної консолі _\djangoWeb\landingWebsite_root>_
 ```
python manage.py shell
 ```

 ```
 Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> 

 ```

+ Імпорт класу Order 
```
from crm.models import Order 
```
+ Створення екземпляру класа Order
```
n = Order (order_name= 'Оксана' , order_phone = '+38066799416')
```
+ Збереження екземляра __n__ в БД 
```
n.save()
```
+  Імпортування модуля __connection__ для перегляду в командному рядку даних екземпляру
```
from django.db import connection
```
+ Створення запити до бази даних 
 ```
 connection.queries
 ```
+ Створення екземпляра моделі разом зі збереженням 
```
  n3= Order.objects.create(order_name= 'Ірина', order_phone = '+38073200259') 
  ```
+ Створення запиту список всіх елементів БД
```
Order.objects.all()
```
```
QuerySet [<Order: Order object (1)>, <Order: Order object (2)>, <Order: Order object (4)>]>
```
+ Фільтрування елементів БД по значенню __id__
```
 Order.objects.order_by('id')
```
```
<QuerySet [<Order: Order object (1)>, <Order: Order object (2)>, <Order: Order object (4)>]>
```
+ Фільтрування елементів БД по значенню __id__  _у зворотньому порядку_
```
 Order.objects.order_by('-id')
```
```
<QuerySet [<Order: Order object (4)>, <Order: Order object (2)>, <Order: Order object (1)>]>
```
+ Виборка одного елемнту даних по приватному ключу (pk)
```
>>> Order.objects.get(pk=4)
<Order: Order object (4)>
```
+ Робота з елементами бази даних 
    + Створення змінної для роботи з елеметом БД з приватним ключем 1 
        ```
        order1= Order.objects.get(pk=1)
        ```
    + Прочитати дані в полі __order_phone__
        ```
        order1.order_phone
        '+38066799416'
        ```
    + Зміна даних в полі __order_phone__
      ```
        order1.order_phone='+380997773366'
        order1.save() 
      ```