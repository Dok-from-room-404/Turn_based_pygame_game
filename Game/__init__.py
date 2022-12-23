



import pygame
from pygame.locals import *
import sys




# Основной класс для взаимодействия с игрой
class Game:
    def __init__(self, image:dict) -> None:
        '''Инициализирует класс.\n
        image – словарь с текстурами для игры'''
        self.image = image
        
    