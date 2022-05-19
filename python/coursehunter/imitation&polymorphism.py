'''
Наслідування : клас який наслідує(нащадок) , батьківський клас той клас що передає свої властивості(методи) та атрибути

Перевизначаєм потрібні в наслідковому класі (нащадка)атрибути батьківського класа 
                def___init__(self,atr...):
                    super().__init__(atr...)
            Далі прописуємо атрибути нащадка(наслідкового класу)            

Можна перевизначати методи батьківського класу , просто переписав метод в нащадку під нові умови(необхідності)

Можна виносити логічно зв'язані атрибути в окремі класи і використовувати екземпляри даного класу як атрибути іншого класу  

'''
class CarsClass():# Батьківський клас
    '''Клас авто'''

    def __init__(self, brand, model, year, race):
        ''' Ініціалізація атрибутів'''
        self.brand= brand
        self.model = model
        self.year = year
        self.race= int(race)

    def showCar(self):
        ''' Показати інформацію про машину '''
        print(f'{self.brand}, {self.model} , {self.year} рік, {self.race} km' )
    def drowCar(self, km):
        '''Метод їзди автомобіля'''
        self.race= self.race + km

class Batterry():# Незалежний клас 
    '''Клас батареї'''
    def __init__(self, battery=80) :
        self.battery=int(battery)
    def description_batterry(self):
        print('Цей автомобіль має заряд батареї:  ' + str(self.battery)+ '%')

class ElectroCar(CarsClass):# Наслідуємий клас від батьківського
    ''' Клас електромашин'''
    def __init__(self, brand, model, year, race):
        super().__init__(brand, model, year, race)
        self.battery = Batterry() # Використання незалежного класу як атрибуту класа 

    def showCar(self):
        ''' Показати інформацію про машину '''
        print(f'{self.brand} , {self.year} рік, {self.race} km' )


s_car = CarsClass('Skoda', 'Fabia', '2020', '10')
s_car.showCar()
s_car.drowCar(250)
s_car.showCar()

tesla= ElectroCar ('Tesla', 'T', '2022', 100)
tesla.showCar()
#tesla.description_batterry()
tesla.drowCar(6500)
tesla.showCar()
tesla.battery.description_batterry()