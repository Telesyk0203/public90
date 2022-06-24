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
    dict_obj= {'slider_list':slider_list,           
                'pc_1':pc_1,
                'pc_2': pc_2,
                'pc_3':pc_3,
                'pc_1_description':pc_1_description,
                'pc_2_description':pc_2_description,
                'pc_3_description':pc_3_description,
                'price_table':price_table}
    return render(request,'./index.html',dict_obj)

def thanks_page(request):
    name= request.POST['name']
    phone= request.POST['phone']
    # name= request.GET['name']
    # phone= request.GET['phone']
    element= Order(order_name = name, order_phone= phone)
    element.save()
    return render(request, './thanks_page.html', {'name':name, 'phone':phone})