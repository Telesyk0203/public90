# Створення Додатку Order(CRM)
1. Створюєм додаток в нашому фреймворці командою в терміналі :
   + `python manage.py startapp crm`
2. Прописуєм його в файлі `settings.py` 
   + `INSTALLED_APPS = [ 'crm.apps.CrmConfig' ` ...
3. Переходимо в файл `models.py` в додатку `crm`  та створюємо класи `StatusCrm`, `Order`, `CommentCrm` від `model.Models` :
 ```
# Create your models here.
class StatusCrm(models.Model):# Створення класу Статусу батьківський клас класу Order(Замовлення)
    status_name=models.CharField(max_length=200, verbose_name='Назва статуса')
    def __str__(self) :
        return self.status_name
    class Meta:
        verbose_name= 'Статус'
        verbose_name_plural='Статуси'
    
class Order(models.Model):# Створення класу Order(Замовлення) дочірній клас StatusCrm
    order_dt= models.DateTimeField(auto_now=True)
    order_name=models.CharField(max_length=200, verbose_name='Name')
    order_phone=models.CharField(max_length=200, verbose_name='Mobile phone')
    order_status=models.ForeignKey(StatusCrm, verbose_name='Статус', on_delete=models.PROTECT, null=True, blank=True)
    def __str__(self) :
        return self.order_name
    class Meta:
        verbose_name= 'Замовлення'
        verbose_name_plural='Замовлення'
    
class CommentCrm(models.Model):# Створення класу CommentCrm дочірній клас Order(Замовлення)
    comment_binding= models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заявка' )
    coment_text = models.TextField(verbose_name='Текст коментря!!!')
    comment_dt = models.DateTimeField(auto_now=True, verbose_name='Час створення')
    def __str__(self) :
        return self.coment_text
    class Meta:
        verbose_name= 'Коментар'
        verbose_name_plural='Коментарі'
```
4. Реєстрація додатку в адмінпанелі в файлі `admin.py` в дерикторії самого додатку `crm` :
```
        from django.contrib import admin
from .models import Order, StatusCrm, CommentCrm
# Register your models here.
admin.site.register(Order)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)
```
5. Міграція даних для того щоб нові дані водобразилися в БД в терміналі вводимо команду:
      + `python manage.py makemigrations`

      + `python manage.py migrate`  переміщення додатків 
6. Вивести зображення в шаблон: 
   +  Створюємо функцію в файлі `views.py` для слайдеру для відображення даних
```
   from unicodedata import name
from django.shortcuts import render
from .models import Order
from .forms import OrderForms
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable
# Create your views here.
def first_page(request):
    slider_list=CmsSlider.objects.all()# Визначємо (ренедерим) усі разом об'єкти додатку  CmsSlider
    pc_1=PriceCard.objects.get(pk=1) # Виводимо(ренедеримо) окреме значення по приватному ключу pk=1
    pc_1_description=pc_1.pc_description # Визначаємо окремий парметра значення як опис в додатку PriceCard
    pc_2=PriceCard.objects.get(pk=2)# # Виводимо окреме значення по приватному ключу pk=2
    pc_2_description=pc_2.pc_description# Визначаємо окремий парметра значення як опис в додатку PriceCard
    pc_3=PriceCard.objects.get(pk=4)# Виводимо окреме значення по приватному ключу pk=4
    pc_3_description=pc_3.pc_description# Визначаємо окремий парметра значення як опис в додатку PriceCard
    price_table=PriceTable.objects.all()# Визначємо (ренедерим) усі разом об'єкти додатку  PriceTable
    form= OrderForms()# Визначємо (ренедерим) усі разом об'єкти моделі  OrderForms
    dict_obj= {'slider_list':slider_list,           
                'pc_1':pc_1,
                'pc_2': pc_2,
                'pc_3':pc_3,
                'pc_1_description':pc_1_description,
                'pc_2_description':pc_2_description,
                'pc_3_description':pc_3_description,
                'form': form,
                'price_table':price_table}
    return render(request,'./index.html',dict_obj)

def thanks_page(request):
    name= request.POST['name']
    phone= request.POST['phone']
    # name= request.GET['name']
    # phone= request.GET['phone']
    element= Order(order_name = name, order_phone= phone)
    element.save()
    return render(request, './thanks.html', {'name':name})

```

+ Переходимо в налаштування файла `index.html` та записуємо таку конструкцію для роботи з даними 
```
    <section>
  		<div class="container class_form">
  			<h1 class="text-3">Залиште зайвку та отримайте послугу</h1>
  			<div class="row justify-content-center">
  			<form action="{% url 'thanks_page' %}" method="POST" style="width: 50%;"> # "{% url 'thanks_page' %}" url(адресу) сторінку переходу та метод 
				{% csrf_token %} # назначаєм csrf_token для методу POST
			  <div class="form-group row">
			    <label for="inputEmail3" class="col-sm-2 col-form-label">Ім'я</label><br>
			     {{ form.name }}# Із файлу forms.py застосовуєм клас OrderForms а саме name
			    <div class="">
			    </div>
			  </div>
			  <div class="form-group row">
			    <label for="inputEmail3" class="col-sm-2 col-form-label">Телефон</label><br>
			      {{ form.phone}}# Із файлу forms.py застосовуєм клас OrderForms а саме phone
			    <div class="">
			    </div>
			  </div>
			  <div style="float: right;" class="form-group row">
			      <button type="submit" class="btn btn-success">ЗАЛИШИТИ ЗАЯВКУ</button>
			  </div>
			</form>
			</div>
  		</div>
  	</section>
```