



# Импорт модулей
import pygame
from pygame.locals import *
import sys
from .Board import *




# Основной класс для взаимодействия с игрой
class Game:
    def __init__(self, image:dict, size, sp_save:list=[], block_size:int=50) -> None:
        '''Инициализирует класс.\n
        image – словарь с текстурами для игры\n
        sp_save - cписок с сохранениями\n
        block_size - размер блока
        size - size of screen'''
        self.size = size
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
    def show_test_level(self) -> None:
        '''Загрузка уровня, переход на следующий и т.д. но пока просто показывает тестовый уровень'''
        self.level = Map(self)
        # камера
        self.camera = Camera(self, self.level.width, self.level.height)
        self.board.new(self.level.map, self.camera)

    def run(self, screen) -> None:
        '''Отрисовка'''
        self.board.update()
        self.board.draw(screen)