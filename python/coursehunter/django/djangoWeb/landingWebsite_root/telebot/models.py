from django.db import models
# Create your models here.
class TeleSettings(models.Model):
    tg_token=models.CharField(max_length=200, verbose_name='Токен_ID')
    tg_chat_id= models.CharField(max_length=200, verbose_name='Чат_ID')
    tg_text= models.TextField(verbose_name='Текст повідомлення')
    tg_time= models.DateTimeField(auto_now=True, verbose_name='Час відправки')

    def __str__(self) : # переведення в рядкове представлення
        return self.tg_chat_id

    class Meta:# переведення для укр мови
        verbose_name= 'Налаштування'
        verbose_name_plural='Налаштування'
