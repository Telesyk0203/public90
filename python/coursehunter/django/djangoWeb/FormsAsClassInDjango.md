# FormsAsClassInDjango
1. __Django__ може генерувати __форми як клас__, створюємо файл `forms.py`  

```
from django import forms

class OrderForms(forms.Form):
    name = forms.CharField(max_length=200)
    phone= forms.CharField(max_length=14)
```
та імпортуєм його в `views.py`
```
from .forms import OrderForms
```
2. __Атрибути__ класу форми - __поля__ форми.
   ```
   form=OrderForms()
   ```
3. Передаєм форму в __render__ у словнику.
   ```
   return render(request,'./index.html',{'object_list':object_list,'form': form})
   ```
   + Передаєм значення до `index.html` в тег форм значення {{form}}
  ```
    <form action="{% url 'thanks_page' %}" method="POST">
        {% csrf_token %}
        {{form}}
        <button type="submit">ВІДПРАВИТИ</button>
    </form>
  ```
4. На необов'язкові поля додаєм атрибут __required = false__
   ```
   from django import forms

    class OrderForms(forms.Form):
        name = forms.CharField(max_length=200, required=False)
        phone= forms.CharField(max_length=14)
   ```
5. Відмальовуєм форму або як __as_p__
   ```
    <form action="{% url 'thanks_page' %}" method="POST">
        {% csrf_token %}
        {{form.as_p}}
        <button type="submit">ВІДПРАВИТИ</button>
    </form>
   ``
    або створюєм свої класи та _id CSS_
    ```

        <style>
        .css_input{
        color:yellow;
        background-color: blue:}
        </style>
    ```

6. Класи _CSS_ задаються допоміжним атрибутом `віджетом` _widjet=forms.TextInput(attrs={"`class`":"`form-class`"})
    + файл `forms.py`
    ```
    from django import forms

    class OrderForms(forms.Form):
    name = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class':'css_input'}))
    phone= forms.CharField(max_length=14)
    ```