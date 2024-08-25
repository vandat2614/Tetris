import random
from grid import Grid
from blocks import *

class Game:
    def __init__(self, num_rows, num_cols, cell_size):
        self.grid = Grid(num_rows, num_cols, cell_size)
        self.cell_size = cell_size
        self.blocks = []
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()

    def reset_blocks(self):
        self.blocks = [IBlock(self.cell_size), JBlock(self.cell_size), LBlock(self.cell_size), OBlock(self.cell_size), SBlock(self.cell_size), TBlock(self.cell_size), ZBlock(self.cell_size)]

    def get_random_block(self):
        if len(self.blocks) == 0: self.reset_blocks()
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)

    def move_left(self):
        self.current_block.move(0, -1)
        if not self.block_inside():
            self.current_block.move(0, 1)

    def move_right(self):
        self.current_block.move(0, 1)
        if not self.block_inside():
            self.current_block.move(0, -1)

    def move_down(self):
        self.current_block.move(1, 0)
        if not self.block_inside():
            self.current_block.move(-1, 0)

    def rotate(self):
        self.current_block.rotate()
        if not self.block_inside():
            self.current_block.undo_rotate()

    def block_inside(self):
        tiles = self.current_block.get_position()
        for tile in tiles:
            if not self.grid.is_inside(tile):
                return False
        return True
