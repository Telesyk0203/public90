# Створення Додатку Slider(CMS)
1. Створюєм додаток в нашому фреймворці командою в терміналі :
   + `python manage.py startapp cms`
2. Прописуєм його в файлі `settings.py` 
   + `INSTALLED_APPS = [ 'cms.apps.CmsConfig' ` ...
3. Переходимо в файл `models.py` в додатку `cms`  та створюємо  дочірній клас `CmsSlider` від `model.Models` :
 ```
from distutils.command.upload import upload
from django.db import models

# Create your models here.
class CmsSlider(models.Model):
    cms_img= models.ImageField(upload_to ='sliderimg/') # Створення поля для зображень та завантаження їх в окрему дерикторію 'sliderimg'
    cms_title= models.CharField(max_length=200, verbose_name='Заголовок')  # Створення поля для тексту
    cms_text= models.CharField(max_length=200, verbose_name='Текст')# Створення поля для тексту
    cms_css= models.CharField(max_length=200, null=True, default='-' , verbose_name='CSS клас')# Створення поля для класу css


def __str__(self) : # переведення в рядкове представлення
        return self.cms_title
class Meta:# переведення для укр мови
        verbose_name= 'Слайд'
        verbose_name_plural='Слайди'
```
4. Реєстрація додатку в адмінпанелі в файлі `admin.py` в дерикторії самого додатку `cms` :
    ```
        from django.contrib import admin
        from .models import CmsSlider
        # Register your models here.
        admin.site.register(CmsSlider)
    ```
5. Міграція даних для того щоб нові дані водобразилися в БД в терміналі вводимо команду:
        + `python manage.py makemigrations`
    можливо необхідно буде встановити додаткову бібліотеку для роботи з зображеннями :
        `python -m pip install Pillow`

      + `python manage.py migrate`  переміщення додатків 
6. Вивести зображення в шаблон: 
   +  Створюємо функцію в файлі `views.py` для слайдеру для відображення 
    ```
    from cms.models import CmsSlider

    def first_page(request):
    slider_list=CmsSlider.objects.all()
    return render(request,'./index.html',{'slider_list':slider_list})

    ```
    + Переходимо в налаштування файла `carusel.html` та записуємо таку конструкцію для роботи з зображеннями 
    ```
    <div class="carousel-inner">
      {% for slide in slider_list  %} # Використання QuerySet 
      <div class="carousel-item {{slide.cms_css}}"> # Активація слайдеру
        <img src="{{ slide.cms_img.url }}" class="d-block w-100"  alt="..."># Вказання на посилання де брати зображення
        <div class="carousel-caption d-none d-md-block">
          <h5 class="slaider_h">{{slide.cms_title}}</h5> # Використання  тексту що пишиться в полі slide.cms_title
          <p class="slaider_p">{{ slide.cms_text }}</p># Використання  тексту що пишиться в полі slide.cms_text
        </div>
      </div>
      {% endfor %} # Закінчення використання  QuerySet
    </div> 
    ```

