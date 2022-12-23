



import pygame
from pygame.locals import *
import sys




# Основной класс для взаимодействия с игрой
class Game:
    def __init__(self, image:dict) -> None:
        '''Инициализирует класс.\n
        image – словарь с текстурами для игры'''
        self.image = image
        # Словарь где каждая текстура привязана к символу (для уровня)
        self.dic_image_from_level = {
            ".": self.image["floor_grass"], 
            ",": self.image["floor_stone"], 
            "/": self.image["floor_tree"], 
            
            "#": self.image["obstacles_stone"], 
            "$": self.image["obstacles_tree"], 
            
            ":": self.image["wall_stone"], 
            ";": self.image["wall_tree"], 
            
            
        }# "@":  self.dic_image["actor"],
    