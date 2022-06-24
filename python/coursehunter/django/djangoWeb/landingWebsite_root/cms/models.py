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
    

