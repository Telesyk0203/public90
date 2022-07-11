from pyexpat import model
from statistics import mode
from tabnanny import verbose
from django.db import models

# Create your models here.
class StatusCrm(models.Model):
    status_name=models.CharField(max_length=200, verbose_name='Назва статуса')
    def __str__(self) :
        return self.status_name
    class Meta:
        verbose_name= 'Статус'
        verbose_name_plural='Статуси'
    
class Order(models.Model):
    order_dt= models.DateTimeField(auto_now=True)
    order_name=models.CharField(max_length=200, verbose_name='Name')
    order_phone=models.CharField(max_length=200, verbose_name='Mobile phone')
    order_status=models.ForeignKey(StatusCrm, verbose_name='Статус', on_delete=models.PROTECT, null=True, blank=True)
    def __str__(self) :
        return self.order_name
    class Meta:
        verbose_name= 'Замовлення'
        verbose_name_plural='Замовлення'
    
class CommentCrm(models.Model):
    comment_binding= models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заявка' )
    coment_text = models.TextField(verbose_name='Текст коментря!!!')
    comment_dt = models.DateTimeField(auto_now=True, verbose_name='Час створення')
    def __str__(self) :
        return self.coment_text
    class Meta:
        verbose_name= 'Коментар'
        verbose_name_plural='Коментарі'