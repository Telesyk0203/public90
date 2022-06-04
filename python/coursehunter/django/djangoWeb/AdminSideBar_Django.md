# AdmiSideBar
+ Створюєм обліковий запис адміна : 
```
python manage.py createsuperuser
```

+ Реєструєм додаток в обліковаму записі адміна , імпортуючи і ат прописав його в файлі __admin.py__
```
from .model import Order #Order назва вашого класу 
admin.site.register(order)
```
+ Для зміни мови адмін панелі змінюємо локалізацію в файлі __settings.py__ з en_us на ru-Ru наприклад
```
# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
```
+ Прописуєм __verbose_name__ для полів, що перекладає назву полів на потрібну мову (значення)
```
class Order(models.Model):
    order_dt= models.DateTimeField(auto_now=True)
    order_name=models.CharField(max_length=200, verbose_name='Name')
    order_phone=models.CharField(max_length=200, verbose_name='Mobile phone')
```
+ Перетворюємо об'єкт в рядкове представлення "магічним методом" __str__ в _return_ який необхідно прописатив потрібне поле
```
def __str__(self) :
        return self.order_name
```
+ Додаєм суб клас __Meta__ для переіменування об'екта класу , додаєм __verbose_name__ і __verbose_name_plural для однини і множини .
```
class Meta:
        verbose_name= 'Замовлення'
        verbose_name_plural='Замовлень'
```