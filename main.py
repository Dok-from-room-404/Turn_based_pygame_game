



# Импорт модулей
import pygame
from pygame.locals import *
import sys
from Game import *






# Данный класс необходим для совмещения лаунчера и игры 
# Основной класс 
class Main:
    def launcher(self) -> None:
        '''Необходима для запуска и получения инфы из лаунчера'''
        # Список с сохранениями
        sp_save = []
        # Количество обновлений экрана
        FPS = 30
        # Размер окна игры
        size = width, height = [1280, 720]
        # Маштабирование блоков(Размер блока)
        block_scaling = 100
        # Выбираем блоки по масштабу 
        self.load_image(block_scaling)
        self.game(size, FPS, sp_save)
        
        
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
        
    def game(self, size:list= [1280, 720], fps:int=30, sp_save:list=[]) -> None: 
        '''Необходима для взаимодействия с игрой\n
        size - список указывающий размеры окна игры\n
        fps - обозначает частоту обновления экрана [кадр/сек]\n
        sp_save - cписок с сохранениями'''
        
        pygame.init()
        pygame.display.set_caption('Игра')
        
        clock_fps = pygame.time.Clock()
        
        screen = pygame.display.set_mode(size)
        
        game = Game(self.image, sp_save)
        game.show_test_level(screen)
        #game.show_menu(screen, clock_fps)
        
        
        print("show")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()  
    
            clock_fps.tick(fps)
            # смена (отрисовка) кадра:
            pygame.display.flip()

            
    
    
    



# Основная функция для работы с программой
def main():
    program_main = Main()
    program_main.launcher()
    
    
if __name__ == "__main__":
    main()