



# Импорт модулей
import pygame
from pygame.locals import *
from Game import *
# from launcher import *
from PIL import Image





# Данный класс необходим для совмещения лаунчера и игры 
# Основной класс ё
class Main:
    def launcher(self) -> None:
        '''Необходима для запуска и получения инфы из лаунчера'''
        # Тестовые значения
        size : list = [1280, 720]
        block_scaling : int = 100
        fps : int = 30
        block_size : int = self.load_image(size, block_scaling)
        self.game(size, fps, block_size)

        
    def load_image(self, size:int, block_scaling:int=100) -> int:
        '''Необходима для выбора текстур по параметрам из лаунчера '''
        
        if block_scaling == 50:
            name = 25
        elif block_scaling == 100:
            name = 50
        elif block_scaling == 150:
            name = 75
        elif block_scaling == 200:
            name = 100
        
        image = Image.open("images\\Menu_fon\\fon.jpg")
        new_image = image.resize(size)
        new_image.save('images\\fon_cash.jpg')

        self.image = {
            "floor_grass": pygame.image.load("images\\floor\\grass\\{name}.png".format(name = name)),
            "floor_stone": pygame.image.load("images\\floor\\stone\\{name}.png".format(name = name)),
            "floor_tree": pygame.image.load("images\\floor\\tree\\{name}.png".format(name = name)),
            
            "obstacles_stone": pygame.image.load("images\\obstacles\\stone\\{name}.png".format(name = name)),
            "obstacles_tree": pygame.image.load("images\\obstacles\\tree\\{name}.png".format(name = name)),
            
            "wall_stone": pygame.image.load("images\\wall\\stone\\{name}.png".format(name = name)),
            "wall_tree": pygame.image.load("images\\wall\\tree\\{name}.png".format(name = name)),
            
            "actor": pygame.image.load("images\\hero\\{name}.png".format(name = name)),
            
            "fon": pygame.image.load("images\\fon_cash.jpg"),
            
            "save_point": pygame.image.load("images\\save_point\\{name}.png".format(name = name)),
            
            "opponent": pygame.image.load("images\\opponent\\{name}.png".format(name = name)),
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
        res = game.show_menu(screen, clock_fps)
        #print(res)
        
        
        game_process = True
        while game_process:
            # Если в меню выбрали закрыть меню
            if res == "break":
                #print("break")
                break 
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_process = False
                    break
                
                if event.type == KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        #print("K_ESCAPE")
                        res = game.show_menu(screen, clock_fps)
                        
                    elif event.key == K_UP or event.key == K_w:
                        #print("k_UP")
                        if game.board.player.moving(y=-1):
                            game.board.player.turn += 1
                            
                    elif event.key == K_DOWN or event.key == K_s:
                        #print("k_DOWN")
                        if game.board.player.moving(y=1):
                            game.board.player.turn += 1
                            
                    elif event.key == K_RIGHT or event.key == K_d:
                        #print("k_RIGHT")
                        if game.board.player.moving(x=1):
                            game.board.player.turn += 1
                            
                    elif event.key == K_LEFT or event.key == K_a:
                        #print("k_LEFT")
                        if game.board.player.moving(x=-1):
                            game.board.player.turn += 1
                    elif event.key == K_SPACE:
                        game.board.player.attack()
                        game.board.player.turn += 1
         
            if res == "break":
                #print("break")
                break 
            game.run(screen)
            clock_fps.tick(fps)
            # смена (отрисовка) кадра:
            pygame.display.flip()
        # Убираем экран игры
        pygame.quit()
        


# Основная функция для работы с программой
def main():
    program_main = Main()
    program_main.launcher()
    
    try:
        program_main.command_last_game()
    except: ...


    
    
if __name__ == "__main__":
    main()