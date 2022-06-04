# Forms .GET & .POST
1. Тег __form__  має два атрибути __action__ & __method__
   ```
   <form action="" method="">
        <label>Ім'я</lable>
        <input name="name">
        <label>Телефон</lable>
        <input name= "phone">
        <button type="submit">ВІДПРАВИТИ</button>
    </form>
   ```
2. __GET__ відкрита форма запиту , формується так : 
   + В файлі __urls.py__ пишемо шлях до певної сторінки на яку треба перейти, вказавши параметр __name__ 
  ```
   path('thanks/', views.thanks_page, name='thanks_page')
  ```
  + Потім в __index.html__ у тезі _form_ прописуєм шлях до сторінки такою конструкцією
  ```
  <form action="{% url 'thanks_page' %}" method="GET">
  ```
   + url/__?atr_1__=''&__art_2__=''&...
   
   + Додаєм до функції __thanks_page__ в файлі __views.py__
  ```
  def thanks_page(request):
    name= request.GET['name']
    phone= request.GET['phone']
    return render(request, './thanks_page.html', {'name':name, 'phone':phone})
  ``` 
  + В файлі __thanks_page.html__  прописуєм 
  ```
    <body>
    <h1>Величезне Вам дякую, {{name}} !!! Слава Україні!!!</h1>
    <h2>Ваш номер телефону :{{phone}} </h2>
    </body>
  ```
  + Створюєм конструкцію для створення запису та збереження даних в БД
    ```
    element= Order(order_name = name, order_phone= phone)
    element.save()
    ``` 
    виглядає так :
   ```
  def thanks_page(request):
    name= request.POST['name']
    phone= request.POST['phone']
    element= Order(order_name = name, order_phone= phone)
    element.save()
    return render(request, './thanks_page.html', {'name':name, 'phone':phone})
  ```      
3. __POST__ прихована форма запиту , і в DJANGO обов'язкова наявність __CSRF__ токену у формі (тег __form__)
  ```
       <form action="{% url 'thanks_page' %}" method="POST">
        {% csrf_token %}
        <label>Ім'я</lable>
        <input name="name">
        <label>Телефон</lable>
        <input name= "phone">
        <button type="submit">ВІДПРАВИТИ</button>
        </form>
  ``` 
    ```
    def thanks_page(request):
    name= request.POST['name']
    phone= request.POST['phone']
    element= Order(order_name = name, order_phone= phone)
    element.save()
    return render(request, './thanks_page.html', {'name':name, 'phone':phone})
    ```
4. В __action__ обов'язково прописуєм шлях __name__ а не прямий шлях ,   __name__ задається в файлі __url__ прияв'язок 
5. Опрацьовуєм запис за допомогою __QuerySet__ і менеджера __objects_ як з екземляром класу(зберігаєм , оновлюєм, створюєм)
6. Приймаєм значення __request.POST['atr']__ or  __request.GET['atr']__
   
