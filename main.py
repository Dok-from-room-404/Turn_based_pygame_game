



# Импорт модулей
import pygame
from pygame.locals import *
import sys
from Game import *
from launcher import *






# Данный класс необходим для совмещения лаунчера и игры 
# Основной класс 
class Main:
    def launcher(self) -> None:
        '''Необходима для запуска и получения инфы из лаунчера'''
        self.class_launcher = Launcher()
        self.class_launcher.connect(self.get_launcher, 30)
        self.class_launcher.show()

    def get_launcher(self) -> None:
        '''Данная функция необходима для получения информации с лаунчера'''
        size, block_scaling, FPS, checkBox = self.class_launcher.get_inform()
        
        self.class_launcher.made_write_options()

        self.class_launcher.destroy()
        if checkBox:
            del self.class_launcher
        else:
            self.command_last_game = self.class_launcher.show()
        # Выбираем блоки по масштабу и загружаем игру
        self.game(size, FPS, self.load_image(block_scaling))
        
    def load_image(self, block_scaling:int=100) -> int:
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
        return name
        
    def command_last_game(self) -> None: '''Необходима для запуска лаунчера после игры'''

        
        
    def game(self, size:list=[1280, 720], fps:int=30, block_size:int=50) -> None:
        '''Необходима для взаимодействия с игрой\n
        size - список указывающий размеры окна игры\n
        fps - обозначает частоту обновления экрана [кадр/сек]\n
        block_size - размер блока'''
        
        pygame.init()
        pygame.display.set_caption('Игра')
        
        clock_fps = pygame.time.Clock()
        
        screen = pygame.display.set_mode(size)
        
        game = Game(self.image, size, block_size)
        game.show_test_level()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()  
                    
                elif event.type == KEYDOWN:
                    if event.key == K_UP or event.key == K_w:
                        print("k_UP")
                        game.board.player.moving(y=-1)
                    if event.key == K_DOWN or event.key == K_s:
                        print("k_DOWN")
                        game.board.player.moving(y=1)
                    if event.key == K_RIGHT or event.key == K_d:
                        print("k_RIGHT")
                        game.board.player.moving(x=1)
                    if event.key == K_LEFT or event.key == K_a:
                        print("k_LEFT")
                        game.board.player.moving(x=-1)
            game.run(screen)
            clock_fps.tick(fps)
            # смена (отрисовка) кадра:
            pygame.display.flip()


# Основная функция для работы с программой
def main():
    program_main = Main()
    program_main.launcher()
    
    
if __name__ == "__main__":
    main()
    
    
    
    











# Данный класс необходим для совмещения лаунчера и игры 
# Основной класс 
class Main:
    def launcher(self) -> None:
        '''Необходима для запуска и получения инфы из лаунчера'''
        self.class_launcher = Launcher()
        self.class_launcher.connect(self.get_launcher, 30)
        self.class_launcher.show()

    def get_launcher(self) -> None:
        '''Данная функция необходима для получения информации с лаунчера'''
        size, block_scaling, FPS, checkBox = self.class_launcher.get_inform()
        # Выбираем блоки по масштабу 
        self.load_image(block_scaling)
        
        self.class_launcher.made_write_options()

        self.class_launcher.destroy()
        if checkBox:
            del self.class_launcher
        else:
            self.command_last_game = self.class_launcher.show()
        
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
        
        
    def command_last_game(self) -> None: '''Необходима для запуска лаунчера после игры'''


    
    
    



# Основная функция для работы с программой
def main():
    program_main = Main()
    program_main.launcher()
    
    try:
        program_main.command_last_game()
    except: ...


    
    
if __name__ == "__main__":
    main()