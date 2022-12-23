



# Импорт модулей
import pygame
from pygame.locals import *
import sys






# Данный класс необходим для совмещения лаунчера и игры 
# Основной класс 
class Main:
    def launcher(self) -> None:
        '''Необходима для запуска и получения инфы из лаунчера'''
        # Количество обновлений экрана
        FPS = 30
        # Размер окна игры
        size = width, height = 1_600, 900
        # Маштабирование блоков(Размер блока)
        block_scaling = 100
        # Выбираем блоки по масштабу 
        self.load_image(block_scaling)
        
        
    def load_image(self, block_scaling:int=100) -> None:
        '''Необходима для выбора текстур по параметрам из лаунчера '''
        if block_scaling == 50:
            self.image = {
                "floor_grass": pygame.image.load("images\\floor\\grass\\25.png"),
                "floor_stone": pygame.image.load("images\\floor\\stone\\25.png"),
                "floor_tree": pygame.image.load("images\\floor\\tree\\25.png"),

                "obstacles_stone": pygame.image.load("images\\obstacles\\stone\\25.png"),
                "obstacles_tree": pygame.image.load("images\\obstacles\\tree\\25.png"),
                
                "wall_stone": pygame.image.load("images\\wall\\stone\\25.png"),
                "wall_tree": pygame.image.load("images\\wall\\tree\\25.png")
            }

        elif block_scaling == 100:
            self.image = {
                "floor_grass": pygame.image.load("images\\floor\\grass\\50.png"),
                "floor_stone": pygame.image.load("images\\floor\\stone\\50.png"),
                "floor_tree": pygame.image.load("images\\floor\\tree\\50.png"),

                "obstacles_stone": pygame.image.load("images\\obstacles\\stone\\50.png"),
                "obstacles_tree": pygame.image.load("images\\obstacles\\tree\\50.png"),

                "wall_stone": pygame.image.load("images\\wall\\stone\\50.png"),
                "wall_tree": pygame.image.load("images\\wall\\tree\\50.png")
            }
            
        elif block_scaling == 150:
            self.image = {
                "floor_grass": pygame.image.load("images\\floor\\grass\\75.png"),
                "floor_stone": pygame.image.load("images\\floor\\stone\\75.png"),
                "floor_tree": pygame.image.load("images\\floor\\tree\\75.png"),

                "obstacles_stone": pygame.image.load("images\\obstacles\\stone\\75.png"),
                "obstacles_tree": pygame.image.load("images\\obstacles\\tree\\75.png"),

                "wall_stone": pygame.image.load("images\\wall\\stone\\75.png"),
                "wall_tree": pygame.image.load("images\\wall\\tree\\75.png")
            }
            
        elif block_scaling == 200:
            self.image = {
                "floor_grass": pygame.image.load("images\\floor\\grass\\100.png"),
                "floor_stone": pygame.image.load("images\\floor\\stone\\100.png"),
                "floor_tree": pygame.image.load("images\\floor\\tree\\100.png"),

                "obstacles_stone": pygame.image.load("images\\obstacles\\stone\\100.png"),
                "obstacles_tree": pygame.image.load("images\\obstacles\\tree\\100.png"),

                "wall_stone": pygame.image.load("images\\wall\\stone\\100.png"),
                "wall_tree": pygame.image.load("images\\wall\\tree\\100.png")
            }
            
    
    
    



# Основная функция для работы с программой
def main():
    program_main = Main()
    program_main.launcher()
    
    
if __name__ == "__main__":
    main()