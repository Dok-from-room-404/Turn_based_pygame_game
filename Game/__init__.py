



# Импорт модулей
import pygame
from pygame.locals import *
import sys
from .Board import *




# Основной класс для взаимодействия с игрой
class Game:
    def __init__(self, image:dict, sp_save:list=[], block_size:int=50) -> None:
        '''Инициализирует класс.\n
        image – словарь с текстурами для игры\n
        sp_save - cписок с сохранениями\n
        block_size - размер блока'''
        self.image = image
        self.sp_save = sp_save
        self.block_size = block_size
        # Словарь где каждая текстура привязана к символу (для уровня)
        self.dic_image_from_level = {
            ".": self.image["floor_grass"], 
            ",": self.image["floor_stone"], 
            "/": self.image["floor_tree"], 
            
            "#": self.image["obstacles_stone"], 
            "$": self.image["obstacles_tree"], 
            
            ":": self.image["wall_stone"], 
            ";": self.image["wall_tree"], 
            
            "@":  self.image["actor"]}
        
        # Список блоков препятствий
        self.sp_ctop_block = ["#", "$", ":", ";"]
        # символ представляющий персонажа
        self.actor_image = "@"
        # Класс отвечающий за прорисовку уровня
        self.board = Board(self.block_size, self.dic_image_from_level, self.sp_ctop_block, self.actor_image)
        
        
        
        
    def show_test_level(self, screen):
        # уровень
        level = [['.', '.', '.', '#', '#', '#', '.', '.', '.', '.', '.'], 
                 ['.', '.', '#', '#', '.', '#', '.', '#', '#', '#', '#'], 
                 ['.', '#', '#', '.', '.', '#', '#', '#', '.', '.', '#'], 
                 ['#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '#'], 
                 ['#', '.', '.', '.', '@', '.', '.', '#', '.', '.', '#'], 
                 ['#', '#', '#', '.', '.', '#', '#', '#', '.', '.', '#'], 
                 ['.', '.', '#', '.', '.', '#', '.', '.', '.', '.', '#'], 
                 ['.', '#', '#', '.', '#', '#', '.', '#', '.', '#', '#'], 
                 ['.', '#', '.', '.', '.', '.', '.', '.', '#', '#', '.'], 
                 ['.', '#', '.', '.', '.', '.', '.', '#', '#', '.', '.'], 
                 ['.', '#', '#', '#', '#', '#', '#', '#', '.', '.', '.']]
        # Заливаем окно в цвет
        screen.fill((17, 189, 234))
        # Выводим длину и высоту уровня
        print(len(level[0]), len(level))
        
        #self.board = Board(len(level[0]), len(level), self.block_size, self.dic_image_from_level)
        self.board.render(screen, level, len(level[0]), len(level), '.', 20)