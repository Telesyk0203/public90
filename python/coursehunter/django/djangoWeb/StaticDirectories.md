#  Static Directories
1. Переносимо додаткові файли проекту (`Css`, `images`, `JS`, скріпти та інші елементи верстки) в окрему папку. 
2. Вказуємо у файлі ` settings.py` де шукати дані файлу. 

   `STATICFILES_DIRS = [
    BASE_DIR / './landingWebsite/static/']`

  В `index.html` прописуєм доступ до стастчних файлів командою `{% load static %}` та вказуєм саме який файл берем , наприклад берем картинку `<img src="{% static 'img/1.jfif' %}" height="300">`

<br>  {% extends 'base.html' %}
<br>  {% block title %} Головна сторінка{% endblock title %}
<br> `{% load static %}`
<br>  {% block content %}
<br>`<img src="{% static 'img/1.jfif' %}" height="300">`
<br>  {% include 'index_old.html' %}
<br>  {% endblock content %}
 
Для того щоб задіяти стилі `CSS` треба в файлі `base.html` небхідно прописати також `{% load static %}` та дати посилання на ці стилі  `<link href="{% static 'style.css' %}" rel='stylesheet'>`

3. Прописуєм папку `static_root` у файлі ` settings.py`
 `  STATIC_ROOT = os.path.join(BASE_DIR, 'static')`
4. В шаблонах прописуєм кончтрукцію : 
   `{% load static%}` 
5. Виводимо статичні файли конструкцій: 
   Приклад: {%static 'external.css'%}
6. Переносимо зборку статичних файлів в папку `static_root` командою __pyton manage.py collectstatic__
7. Прописуєм дерикторії для `media` файлів в `settings.py`

   ` MEDIA_URL = '/media/'`
    `MEDIA_ROOT = os.path.join(BASE_DIR, 'media')`
    
    
    from django.conf.urls import static
    from django.conf import settings

     static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)