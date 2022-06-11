# ImitationPatterns

1. Базовий шаблон `base.html` має в собі елементи які є на всіх сторінках сайту (`шапка,підвал,метаданні`)
   ```
      <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
    <header>
        <h1>Шапка сайту</h1>
        <h1>_____________________________________________________________</h1>
    </header>



    <footer>
        <h1>_____________________________________________________________</h1>
        <h1>Підвал сайту</h1>

    </footer>    
    </body>
    </html>``
   ```
2. Всі інші шаблони(шаблонні сторінки) розширяються  `base.html` необхідно прописати 
   ```
   {% extends 'base.html' %}
   ```
    
3. В `base.html` прописуєм блоки сторінок які виводимо. У сторінках що виводимо прописуєм початок і кінець блоку.
    ```
    {% block content %}
    {% endblock content %}
    ```
4. Можна перевизначати базові параметри з `base.html`, наприклад тайтл(Title)
  +  В `base.html`обгортаєм тег (Title) в таку конструкцію
  ```
  <title>{% block title %}Текст шаблонного тайтлу{% endblock title %}</title>
  ```
  + В `index.html` вписуєм після `{% extends 'base.html' %}`  таку конструкцію
  ```
  {% block title %} Текст сторінки {% endblock title %}
  ```
5. Максимально розбиваємо шаблонну сторінку на блоки, для зручної роботи з кодом `HTML`
6. Вставляєм розділені блоки коду у шаблонну сторінку над якою працюємо (`index.html`) конструкцією `include`
   ```
   {% include 'index_old.html' %}
   ```
7. на виході `index.html` має таку шаблону конструцію
   ```
    {% extends 'base.html' %} # Розширення за допомогою основного файлу base.html
    {% block title %} Головна сторінка{% endblock title %} # Введення свого тайтлу замість шаблонного
    {% block content %}#Початок  введення Контену сторінки html код 
    <h2> Дані з файлу індексу(index.html) </h2>html код 
    {% include 'index_old.html' %}# Код іншої сторінки html в цю сторінку
    {% endblock content %}Кінець Контену
    
   ```