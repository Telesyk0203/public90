'''
Dunder - Магічні методи __str__(srting) & __repr__(representation) використовуються для рядкового предсавлення об'єкту.

'''
from os import name


class New():
    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self) -> str: # Для більш інформації яка підходить в лог файл 
        return self.name

    def __str__(self) -> str:# Для того щоб виводити саме читаючий текст для людини 
        return self.name

name= New('Taras')

print(name)