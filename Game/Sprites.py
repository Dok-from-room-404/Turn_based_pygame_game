import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, board, x, y, image):
        self.groups = board.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.board = board
        self.image = self.board.dic_image_from_level[image]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def moving(self, x=0, y=0):
        if not self.collide_with_walls(x, y):
            self.x += x
            self.y += y

    def collide_with_walls(self, x=0, y=0):
        for wall in self.board.walls:
            if wall.x == self.x + x and wall.y == self.y + y:
                return True
        return False

    def update(self):
        self.rect.x = self.x * self.board.block_size
        self.rect.y = self.y * self.board.block_size


class Wall(pygame.sprite.Sprite):
    def __init__(self, board, x, y, image):
        self.groups = board.all_sprites, board.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.board = board
        self.image = self.board.dic_image_from_level[image]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * self.board.block_size
        self.rect.y = y * self.board.block_size


class Tile(pygame.sprite.Sprite):
    def __init__(self, board, x, y, image='.'):
        self.groups = board.empty_tiles
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.board = board
        self.image = self.board.dic_image_from_level[image]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * self.board.block_size
        self.rect.y = y * self.board.block_size
