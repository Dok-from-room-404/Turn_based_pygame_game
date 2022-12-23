



import pygame
from pygame.locals import *
import sys




# Основной класс для взаимодействия с игрой
class Game:
    # def __init__(self, image:dict, size:list= (1280, 720), fps:int=30) -> None:
    #     '''Инициализирует класс.\n
    #     image – словарь с текстурами для игры
    #     size - список указывающий размеры окна игры
    #     fps - обозначает частоту обновления экрана [кадр/сек]'''
    
    def __init__(self, image:dict, sp_save:list=[]) -> None:
        '''Инициализирует класс.\n
        image – словарь с текстурами для игры
        sp_save - cписок с сохранениями'''
        self.image = image
        self.sp_save = sp_save
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
        
        
    def show_menu(self, screen, clock_fps) -> None:
        """Отображает меню, пока пользователь не нажмет клавишу"""
        
        #titleRect = self.dic_image['title'].get_rect()
        screen.fill((17, 189, 234))
        #screen.blit(self.dic_image['title'], titleRect)

        font = pygame.font.Font('freesansbold.ttf', 18)
        instSurf = font.render("Для начала игры нужно нажать Enter", 1, (0, 0, 0))
        
        instRect = instSurf.get_rect()
        instRect.top = 50
        instRect.centerx = 175
        
        screen.blit(instSurf, instRect)
        pygame.display.flip()
        
        while True: # Основной цикл для стартового экрана.
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit()
                    if event.key == K_RETURN:
                        return # пользователь нажал клавишу, поэтому вернитесь.
            pygame.display.update()
            clock_fps.tick()