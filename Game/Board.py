



# Импорт модулей
import pygame



# Класс отвечающий за прорисовку уровня
class Board:
    def __init__(self, block_size:int=50, dic_image_from_level:dict={}, sp_ctop_block:list=[]) -> None:
        '''Инициализирует класс.\n
        block_size – Размер каждого блока\n
        dic_image_from_level - словарь с текстурами для игры где каждая текстура привязана к символу (для уровня)\n
        sp_ctop_block - Список блоков препятствий'''
        self.block_size = block_size
        self.dic_image_from_level = dic_image_from_level
        self.sp_ctop_block = sp_ctop_block
        
    def render(self, screen, level, width:int, height:int, bias_):
        pass







class Board:
    def __init__(self, width:int, height:int, cell_size:int=50, dic_image_from_level:dict={}):
        # длина уровня
        self.width = width
        # Высота уровня
        self.height = height
        # Размер каждого блока
        self.cell_size = cell_size
        # Блоки куда нельзя ходить
        self.not_go_board = []
        # Позиция актера
        self.actor_pos = []
        # Смещение влево
        self.left = 0
        # Смещение вниз
        self.top = 0
        # словарь с текстурами для игры где каждая текстура привязана к символу (для уровня)
        self.dic_image_from_level = dic_image_from_level

 

 
    def render(self, screen, level):
        wcolor = pygame.Color(255, 255, 255)
        for y in range(self.height):
            for x in range(self.width):
                n_x, n_y = self.left + self.cell_size * x, self.top + self.cell_size * y
                k_x, k_y = self.cell_size, self.cell_size
                
                pygame.draw.rect(screen, wcolor, (n_x, n_y, k_x, k_y), 1)

                level_res = level[y][x]
                
                if level_res == "@":
                    titleRect = self.dic_image_from_level["."].get_rect()
                    titleRect.bottomleft = (n_x, n_y + self.cell_size)
                    self.actor_pos = [n_x, n_y + self.cell_size]
                    screen.blit(self.dic_image_from_level["."], titleRect)
                    
                    
                if level_res == "#":
                    self.not_go_board.append([n_x, n_y + self.cell_size])
 
                titleRect = self.dic_image_from_level[level[y][x]].get_rect()
                titleRect.bottomleft = (n_x, n_y + self.cell_size)
                
                screen.blit(self.dic_image_from_level[level[y][x]], titleRect)
        
        
    def chek(self, res):
        return res not in self.not_go_board and (res[0] > 0 and res[1] > 0)
        
        
        
    def last_pos_actor(self, screen): 
            titleRect = self.dic_image_from_level["."].get_rect()
            titleRect.bottomleft = self.actor_pos
            
            screen.blit(self.dic_image_from_level["."], titleRect)
            
    def go(self, screen, res):
            titleRect = self.dic_image_from_level["@"].get_rect()
            self.actor_pos = res
            titleRect.bottomleft = self.actor_pos
            screen.blit(self.dic_image_from_level["@"], titleRect)
                
                
    def go_left(self, screen): 
        res = [self.actor_pos[0] - self.cell_size, self.actor_pos[1]]
        if self.chek(res):
            self.last_pos_actor(screen)
            self.go(screen, res)
        
    
    def go_right(self, screen): 
        res = [self.actor_pos[0] + self.cell_size, self.actor_pos[1]]
        if self.chek(res):
            self.last_pos_actor(screen)
            self.go(screen, res)

        
        
        
    
    def go_up(self, screen): 
        res = [self.actor_pos[0], self.actor_pos[1] - self.cell_size]
        if self.chek(res):
            self.last_pos_actor(screen)
            self.go(screen, res)

    
    def go_down(self, screen): 
        res = [self.actor_pos[0], self.actor_pos[1] + self.cell_size]
        if self.chek(res):
            self.last_pos_actor(screen)
            self.go(screen, res)

 
    
 

