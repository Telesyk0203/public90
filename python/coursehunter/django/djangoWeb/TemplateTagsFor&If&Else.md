# Templates Tag __for__ , __if__ & __else__

1. Шаблонний тег __for__ працює з такою самою логікою що і цикл _for_ в python 
Виводить об'єкти із списку всіх об'єктів . 
#### Конструкція
```
{%for obj in object_list%}
    {{obj.art}}
{%endfor%}
```
####
__Приклад__
```
{%for obj in object_list%}
        <tr>
            <th>{{obj.id}}</th>
            <th>{{obj.order_dt}}</th>
            <th>{{obj.order_name}}</th>
            <th>{{obj.order_phone}}</th>
        </tr>
{%endfor%}    
```
__!!!НЕ ЗАБУВАЄМ__ про __{%endfor%}__

2. Вносимо об'єкти в теги __html__ , для зміни стилів , приклад з таблицею
   ``` <table border="1">
        <tr>
            <th>ID</th>
            <th>Дата</th>
            <th>Ім'я</th>
            <th>Телефон</th>
        </tr>
    {%for obj in object_list%}
        <tr>
            <th>{{obj.id}}</th>
            <th>{{obj.order_dt}}</th>
            <th>{{obj.order_name}}</th>
            <th>{{obj.order_phone}}</th>
        </tr>
    {%endfor%}    
    </table>
   ```
3. Конструкція __if else endif__ працює з такою самою логікою що в python , перевіряєм наявність об'єктів за допомогою __if__:
  ```
  {%if object_list%}# якщо об'єкт існує в базі то ... вивід об'єктів
  {%else%}# якщо об'єктів в БД немає 
  # html код виводить інформацію що немає даних
  {%endif%}

  ```
  #### Приклад
  ```
  {% if  object_list%}
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Дата</th>
            <th>Ім'я</th>
            <th>Телефон</th>
        </tr>
    {%for obj in object_list%}
        <tr>
            <th>{{obj.id}}</th>
            <th>{{obj.order_dt}}</th>
            <th>{{obj.order_name}}</th>
            <th>{{obj.order_phone}}</th>
        </tr>
    {%endfor%}   
    </table>
    {% else %}
    <h3>Немає  даних</h3>
    {% endif %}
```

