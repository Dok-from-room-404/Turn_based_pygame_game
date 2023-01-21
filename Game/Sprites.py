import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, board, x, y, image, hp=100, dmg=10):
        self.groups = board.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.board = board
        self.image = self.board.dic_image_from_level[image]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.turn = 0
        self.hp = hp
        self.dmg = dmg


    def moving(self, x=0, y=0):
        if self.collide_with_walls(x, y):
            self.board.moving_map[self.y][self.x] = 0
            self.x += x
            self.y += y
            self.board.moving_map[self.y][self.x] = 1
            return True

    def collide_with_walls(self, x=0, y=0):
        if self.board.moving_map[self.y + y][self.x + x] == 0:
            return True
        return False

    def attack(self):
        for enemy in self.board.enemies:
            if abs(enemy.x - self.x) + abs(enemy.y - self.y) == 1:
                enemy.hp -= self.dmg

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


class Enemy(pygame.sprite.Sprite):
    """начальный класс противников"""
    def __init__(self, board, x, y, image, hp=100, dmg=10):
        self.groups = board.all_sprites, board.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.board = board
        self.image = self.board.dic_image_from_level[image]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * self.board.block_size
        self.rect.y = y * self.board.block_size
        self.hp = hp
        self.dmg = dmg

    def action(self):
        '''атака, перемещение монстра (пока только перемещение)'''
        ways = self.bfs()
        p_cor = (self.board.player.x, self.board.player.y)
        if abs(self.board.player.x - self.x) + abs(self.board.player.y - self.y) != 1 and p_cor in ways:
            self.make_move(ways)

    def make_move(self, ways):
        cur_move = (self.board.player.x, self.board.player.y)
        way = []
        while cur_move != (self.x, self.y):
            cur_move = ways[cur_move]
            way.append(cur_move)
        self.board.moving_map[self.y][self.x] = 0
        self.x = way[-2][0]
        self.y = way[-2][1]
        self.board.moving_map[self.y][self.x] = 1

    def update(self):
        self.rect.x = self.x * self.board.block_size
        self.rect.y = self.y * self.board.block_size
        if self.hp <= 0:
            self.kill()
            self.board.moving_map[self.y][self.x] = 0

    def create_graf(self):
        graf = {}
        for y, row in enumerate(self.board.moving_map):
            for x, col in enumerate(row):
                if not col or y == self.y and x == self.x or y == self.board.player.y and x == self.board.player.x:
                    graf[(x, y)] = graf.get((x, y), []) + self.get_neighbors(x, y)
        return graf

    def check_neighbors(self, x, y):
        return True if 0 <= x < len(self.board.moving_map[0]) \
                                               and 0 <= y < len(self.board.moving_map) \
                                               and not self.board.moving_map[y][x]\
                       or y == self.board.player.y and x == self.board.player.x else False

    def get_neighbors(self, x, y):
        ways = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        return [(x + dx, y + dy) for dx, dy in ways if self.check_neighbors(x + dx, y + dy)]

    def bfs(self):
        """алгоритм поиска в  ширину"""
        graf = self.create_graf()
        queue = [(self.x, self.y)]
        visited = {(self.x, self.y): None}
        while queue:
            cur_move = queue.pop(0)
            if cur_move == (self.board.player.x, self.board.player.y):
                break
            next_moves = graf[cur_move]
            for next_move in next_moves:
                if next_move not in visited:
                    queue.append(next_move)
                    visited[next_move] = cur_move

        return visited


