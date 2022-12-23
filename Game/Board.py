



# Импорт модулей
import pygame



# Класс отвечающий за прорисовку уровня
class Board:
    def __init__(self, block_size:int=50, dic_image_from_level:dict={}, sp_ctop_block:list=[], actor_image:str="@") -> None:
        '''Инициализирует класс.\n
        block_size – Размер каждого блока\n
        dic_image_from_level - словарь с текстурами для игры где каждая текстура привязана к символу (для уровня)\n
        sp_ctop_block - Список блоков препятствий\n
        actor_image - символ представляющий персонажа'''
        self.block_size = block_size
        self.dic_image_from_level = dic_image_from_level
        self.sp_ctop_block = sp_ctop_block
        self.actor_image = actor_image
        
    def render(self, screen, level:str, width:int, height:int, block_to_acter:str=".", bias_left:int=0, bias_top:int=0) -> None:
        '''Данная функция необходима для рендера уровня\n
        screen — холст, на котором нужно рисовать\n
        level - уровень\n
        width - длина уровня\n
        height - Высота уровня\n
        block_to_acter - чем заполнять после актера (символ из словаря для уровня)\n
        bias_left - Смещение влево (по оси x)\n
        bias_top - Смещение вниз (по оси y)'''
        # Блоки куда нельзя ходить
        self.not_go_board = []
        # Позиция актера
        self.actor_pos = []
        # чем заполнять после актера (символ из словаря для уровня)
        self.block_to_acter = block_to_acter

        wcolor = pygame.Color(255, 255, 255)
        for y in range(height):
            for x in range(width):
                n_x, n_y = bias_left + self.block_size * x, bias_top + self.block_size * y
                k_x =  k_y = self.block_size
                pygame.draw.rect(screen, wcolor, (n_x, n_y, k_x, k_y), 1)
                # Символ уровня
                level_res = level[y][x]
                
                if level_res == self.actor_image:
                    # Закрашиваем клетку под игроком
                    titleRect = self.dic_image_from_level[self.block_to_acter].get_rect()
                    titleRect.bottomleft = (n_x, n_y + self.block_size)
                    screen.blit(self.dic_image_from_level[self.block_to_acter], titleRect)
                    # Сохраняем позицию игрока
                    self.actor_pos = [n_x, n_y + self.block_size]
                    
                    
                if level_res in self.sp_ctop_block:
                    # Закрашиваем клетку под препятствием или стеной
                    titleRect = self.dic_image_from_level[self.block_to_acter].get_rect()
                    titleRect.bottomleft = (n_x, n_y + self.block_size)
                    screen.blit(self.dic_image_from_level[self.block_to_acter], titleRect)
                    # Сохраняем позицию препятствия или стены
                    self.not_go_board.append([n_x, n_y + self.block_size])
 
                titleRect = self.dic_image_from_level[level[y][x]].get_rect()
                titleRect.bottomleft = (n_x, n_y + self.block_size)
                
                screen.blit(self.dic_image_from_level[level[y][x]], titleRect)
                
    ##############################
    # Следующий блок кода отвечает за передвижение гг 

    def __chek(self, res:list) -> bool:
        '''Проверяет что гг может идти в заданном направлении\n
        res - положение гг с учетом хода'''
        return res not in self.not_go_board and (res[0] > 0 and res[1] > 0)
        
    def __last_pos_actor(self, screen) -> None: 
        '''Позволяет закрасить клетку где был гг до хода\n
        screen — холст, на котором нужно рисовать'''
        titleRect = self.dic_image_from_level["."].get_rect()
        titleRect.bottomleft = self.actor_pos
        screen.blit(self.dic_image_from_level["."], titleRect)
            
    def __go(self, screen, res:list) -> None:
        '''Данная функция осуществляет ход гг на полотне\n
        screen — холст, на котором нужно рисовать\n
        res - положение гг с учетом хода'''
        titleRect = self.dic_image_from_level["@"].get_rect()
        self.actor_pos = res
        titleRect.bottomleft = self.actor_pos
        screen.blit(self.dic_image_from_level["@"], titleRect)
                
                
    def go_left(self, screen): 
        '''Данный метод отвечает за возможность ходить в лево\n
        screen — холст, на котором нужно рисовать'''
        res = [self.actor_pos[0] - self.block_size, self.actor_pos[1]]
        if self.__chek(res):
            self.__last_pos_actor(screen)
            self.__go(screen, res)
        
    
    def go_right(self, screen): 
        '''Данный метод отвечает за возможность ходить в право\n
        screen — холст, на котором нужно рисовать'''
        res = [self.actor_pos[0] + self.block_size, self.actor_pos[1]]
        if self.__chek(res):
            self.__last_pos_actor(screen)
            self.__go(screen, res)

    def go_up(self, screen): 
        '''Данный метод отвечает за возможность ходить вперед\n
        screen — холст, на котором нужно рисовать'''
        res = [self.actor_pos[0], self.actor_pos[1] - self.block_size]
        if self.__chek(res):
            self.__last_pos_actor(screen)
            self.__go(screen, res)

    def go_down(self, screen): 
        '''Данный метод отвечает за возможность ходить назад\n
        screen — холст, на котором нужно рисовать'''
        res = [self.actor_pos[0], self.actor_pos[1] + self.block_size]
        if self.__chek(res):
            self.__last_pos_actor(screen)
            self.__go(screen, res)

 
    
 

