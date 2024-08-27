import random
from grid import Grid
from blocks import *
import pygame

class Game:
    def __init__(self, ):
        self.grid = Grid()
        self.cell_size = 30
        self.blocks = []
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        pygame.mixer.music.load('sounds\\background.mp3')
        pygame.mixer.music.play(-1)
        self.rotate_sound = pygame.mixer.Sound('sounds\\rotate.mp3')
        self.clear_sound = pygame.mixer.Sound('sounds\\clear_row.wav')

    def reset_blocks(self):
        self.blocks = [IBlock(self.cell_size), JBlock(self.cell_size), LBlock(self.cell_size), OBlock(self.cell_size), SBlock(self.cell_size), TBlock(self.cell_size), ZBlock(self.cell_size)]

    def update_score(self, row_cleared=0, move_down_points=0):
        if row_cleared == 1:
            self.score += 40
        elif row_cleared == 2:
            self.score += 100
        elif row_cleared == 3:
            self.score += 300
        elif row_cleared == 4:
            self.score += 1200
        self.score += move_down_points

    def get_random_block(self):
        if len(self.blocks) == 0: self.reset_blocks()
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        self.move_block_center(block)
        return block
    
    def move_block_center(self, block):
        if block.id == 4:
            block.move(0, 4)
        else: block.move(0, 3)

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)
        if self.next_block.id == 4: # O block
            offset_x, offset_y = 255, 275
        elif self.next_block.id == 3: # I block
            offset_x, offset_y = 255, 260
        else: offset_x, offset_y = 270, 275
        self.next_block.draw(screen, offset_x, offset_y)

    def reset(self):
        self.grid.reset()
        self.reset_blocks()
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0

    def move_left(self):
        self.current_block.move(0, -1)
        if not self.block_inside() or self.collision():
            self.current_block.move(0, 1)
        if self.collision():
            self.lock_block()

    def move_right(self):
        self.current_block.move(0, 1)
        if not self.block_inside() or self.collision():
            self.current_block.move(0, -1)
        if self.collision():
            self.lock_block()

    def move_down(self):
        self.current_block.move(1, 0)
        if not self.block_inside() or self.collision():
            self.current_block.move(-1, 0)
            self.lock_block()
             
    def rotate(self):
        self.current_block.rotate()
        if not self.block_inside() or self.collision():
            self.current_block.undo_rotate()
        else:
            self.rotate_sound.play()
        if self.collision():
            self.lock_block()


    def lock_block(self):
        tiles = self.current_block.get_position()
        for tile in tiles:
            self.grid.grid[tile.row][tile.col] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        cleared_row = self.grid.clear_full_row()
        if cleared_row > 0:
            self.clear_sound.play()
            self.update_score(row_cleared=cleared_row)

        if not self.block_inside() or self.collision():
            self.current_block.move(-1, 0)
            self.game_over = True

    def block_inside(self):
        tiles = self.current_block.get_position()
        for tile in tiles:
            if not self.grid.is_inside(tile):
                return False
        return True
    
    def collision(self):
        tiles = self.current_block.get_position()
        for tile in tiles:
            if not self.grid.is_empty(tile):
                return True
        return False
