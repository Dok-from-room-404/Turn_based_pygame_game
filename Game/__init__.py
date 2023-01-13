



# Импорт модулей
import pygame
from pygame.locals import *
from .Board import *
from .Menu.menu import *




# Основной класс для взаимодействия с игрой
class Game:
    def __init__(self, image:dict, size, block_size:int=50) -> None:
        '''Инициализирует класс.\n
        image – словарь с текстурами для игры\n
        block_size - размер блока
        size - список указывающий размеры окна игры\n'''
        self.size = size
        self.image = image
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
        # Класс отвечающий за меню
        self.menu = Menu(self.image["fon"])
        # Флаг загруженного уровня True - загружен, False - не загружен
        self.stete_load_level = False
        
        
        
    def show_menu(self, screen, clock_fps):
        """Отображает титульный экран, пока пользователь не нажмет клавишу\n
        1) Будем искать сохранения\n
        2) Будем продолжать игру\n
        3) Будем выходить из игры"""
        try:
            res = self.menu.show_menu(screen, clock_fps, self.stete_load_level)
            
            if res == "new_games":
                self.show_test_level()
            
            
        except BreakError:
            pygame.quit()
            return "break"
        
        
        
        
    def show_test_level(self) -> None:
        '''Загрузка уровня, переход на следующий и т.д. но пока просто показывает тестовый уровень'''
        self.stete_load_level = True
        self.level = Map(self)
        # камера
        self.camera = Camera(self, self.level.width, self.level.height)
        self.board.new(self.level.map, self.camera)

    def run(self, screen) -> None:
        '''Отрисовка'''
        self.board.update()
        self.board.draw(screen)