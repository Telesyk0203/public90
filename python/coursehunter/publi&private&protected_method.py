'''

Публічні атрибути та методи - доступні до читання та використання за межами класу

Захищені - заборонені для читання та зміненню , але тільки на рівні домовленості між програмістами 

Приватні - заборонені для читання та конфігурування на рівні мови 
'''


class InstagrammAccountInWebsite():
    ''' Ваш акаунт в Instagramm , на сайті Інстаграм'''

    def __init__(self, name, login_id, password) :
        self.name= name # Публічний атрибут
        self._login_id= login_id # Захищений атрибут
        self.__password=password # Приватний атрибут 
    
    def publicLoginInstagramm(self):#  Створення публічного методу із приватного 
        self.__loginInstagramm()

    
    def __loginInstagramm(self):# Приватний метод
        if self._login_id== 'Taras' and self.__password== '!QAZ2wsx': 
            print('Вітаємо тебе ' + self.name)
        else:
            print('НЕвірний логін або пароль!!!')
        return   True 

insta_account= InstagrammAccountInWebsite('Tarik', 'Taras', '!QAZ2wsx')
# insta_account.loginInstagramm()

insta_account.name='Zandalar'
print(insta_account.name)
insta_account._login_id="Amani"
print(insta_account._login_id)
# print(insta_account.__password)
# insta_account.loginInstagramm()
insta_account.publicLoginInstagramm()