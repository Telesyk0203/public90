# Створення Додатку Price(Ціни)
1. Створюєм додаток в нашому фреймворці командою в терміналі :
   + `python manage.py startapp price`
2. Прописуєм його в файлі `settings.py` 
   + `INSTALLED_APPS = [ 'cms.apps.PriceConfig' ` ...
3. Переходимо в файл `models.py` в додатку `price`  та створюємо  дочірні класи `PriceCard` та від `PriceTable` `model.Models` :
   ```
   from django.db import models

    # Create your models here.
    class PriceCard(models.Model):
        pc_value= models.CharField(max_length=20, verbose_name='Ціна')
        pc_description= models.CharField(max_length=200, verbose_name='Опис')   
        def __str__(self) : # переведення в рядкове представлення
            return self.pc_value

        class Meta:# переведення для укр мови
            verbose_name= 'Ціна'
            verbose_name_plural='Ціни'



    class PriceTable(models.Model):
        pt_title= models.CharField(max_length=200, verbose_name='Послуга')
        pt_old_price=models.CharField(max_length=20, verbose_name='Стара ціна')
        pt_new_price= models.CharField(max_length=20, verbose_name='Нова ціна')

        def __str__(self) : # переведення в рядкове представлення
            return self.pt_old_price, self.pt_new_price, self.pt_title

        class Meta:# переведення для укр мови
            verbose_name= 'Послуга'
            verbose_name_plural='Послуги'
    ```

4. Реєстрація додатку в адмінпанелі в файлі `admin.py` в дерикторії самого додатку `price` :
```
from django.contrib import admin
from .models import PriceCard, PriceTable

# Register your models here.
admin.site.register(PriceCard)
admin.site.register(PriceTable)
```
5. Міграція даних для того щоб нові дані водобразилися в БД в терміналі вводимо команду:
    + `python manage.py makemigrations`
    
    + `python manage.py migrate`  переміщення додатків 
6. Вивести зображення в шаблон: 
   +  Доповнюємо функцію в файлі `views.py` для цін для відображення:
```
    from price.models import PriceCard, PriceTable
# Create your views here.
def first_page(request):
    slider_list=CmsSlider.objects.all()
    pc_1=PriceCard.objects.get(pk=1)
    pc_1_description=pc_1.pc_description
    pc_2=PriceCard.objects.get(pk=2)
    pc_2_description=pc_2.pc_description
    pc_3=PriceCard.objects.get(pk=4)
    pc_3_description=pc_3.pc_description
    price_table=PriceTable.objects.all()
    dict_obj= {'slider_list':slider_list,           
                'pc_1':pc_1,
                'pc_2': pc_2,
                'pc_3':pc_3,
                'pc_1_description':pc_1_description,
                'pc_2_description':pc_2_description,
                'pc_3_description':pc_3_description,
                'price_table':price_table}
    return render(request,'./index.html',dict_obj)
```
 + Переходимо в налаштування файла `price.html` та записуємо таку конструкцію для роботи з цінами 
   + Для додатку `PriceCard`
```
         <div class="row justify-content-center">
            <div class="card product_card" style="width: 18rem; background-color: #cd7f32;">
            <div class="card-body">
              <h5 class="card-title">BRONZE</h5>
              <p class="card-text">{{pc_1_description}}</p>
              <h3>{{pc_1}} грн.</h3>
            </div>
          </div>
          <div class="card product_card" style="width: 18rem; background-color: #c0c0c0;">
            <div class="card-body">
              <h5 class="card-title">SILVER</h5>
              <p class="card-text">{{pc_2_description}}</p>
              <h3>{{pc_2}} грн.</h3>
            </div>
          </div>
          <div class="card product_card" style="width: 18rem; background-color: #ffd700;">
            <div class="card-body">
              <h5 class="card-title">GOLD</h5>
              <p class="card-text">{{pc_3_description}}</p> 
              <h3>{{pc_3}} грн.</h3>
```

   
 + Ддя додатку `PriceTable` 
```
       <tbody>
          {% for obj in price_table %}
          <tr>
            <td> {{obj.pt_title}}</td>
            <td><del>{{obj.pt_old_price}}</del></td>
            <td>{{obj.pt_new_price}}</td>
          </tr>
          {% endfor %}
        </tbody>
``` 