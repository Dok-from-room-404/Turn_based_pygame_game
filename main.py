



# Импорт модулей
import pygame
from pygame.locals import *
import sys
from launcher import *






# Данный класс необходим для совмещения лаунчера и игры 
# Основной класс 
class Main:
    def launcher(self) -> None:
        '''Необходима для запуска и получения инфы из лаунчера'''
        launcher = Launcher()
        launcher.show()
        # Количество обновлений экрана
        FPS = 30
        # Размер окна игры
        size = width, height = [1280, 720]
        # Маштабирование блоков(Размер блока)
        block_scaling = 100
        # Выбираем блоки по масштабу 
        self.load_image(block_scaling)
        
        
    def load_image(self, block_scaling:int=100) -> None:
        '''Необходима для выбора текстур по параметрам из лаунчера '''
        
        
        if block_scaling == 50:
            name = 25
        elif block_scaling == 100:
            name = 50
        elif block_scaling == 150:
            name = 75
        elif block_scaling == 200:
            name = 100

        self.image = {
            "floor_grass": pygame.image.load("images\\floor\\grass\\{name}.png".format(name = name)),
            "floor_stone": pygame.image.load("images\\floor\\stone\\{name}.png".format(name = name)),
            "floor_tree": pygame.image.load("images\\floor\\tree\\{name}.png".format(name = name)),
            
            "obstacles_stone": pygame.image.load("images\\obstacles\\stone\\{name}.png".format(name = name)),
            "obstacles_tree": pygame.image.load("images\\obstacles\\tree\\{name}.png".format(name = name)),
            
            "wall_stone": pygame.image.load("images\\wall\\stone\\{name}.png".format(name = name)),
            "wall_tree": pygame.image.load("images\\wall\\tree\\{name}.png".format(name = name)),
            
            "actor": pygame.image.load("images\\hero\\{name}.png".format(name = name)),
            
        }

            
    
    
    



# Основная функция для работы с программой
def main():
    program_main = Main()
    program_main.launcher()

    
    
if __name__ == "__main__":
    main()