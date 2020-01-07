import pygame


class GameObject: # класс наследник для всех обьектов
    def init(self, modules): # функция для инициализации класса
        self.modules = modules # переменная хранящая в себе все модули игры (по сути это Singlton)

    def render(self, events): # метод обновления кадра
        pass
