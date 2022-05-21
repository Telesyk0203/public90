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

        