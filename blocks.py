from position import Position
from block import Block

class LBlock(Block):
    def __init__(self, cell_size):
        super().__init__(id=1, cell_size=cell_size)
        self.states = [
            [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],
            [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
            [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],
            [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)]
        ]

class JBlock(Block):
    def __init__(self, cell_size):
        super().__init__(id=2, cell_size=cell_size)
        self.states = [
            [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
            [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],
            [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],
            [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)]
        ]

class IBlock(Block):
    def __init__(self, cell_size):
        super().__init__(id=3, cell_size=cell_size)
        self.states = [
            [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
            [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
            [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
            [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)]
        ]

class OBlock(Block):
    def __init__(self, cell_size):
        super().__init__(id=4, cell_size=cell_size)
        self.states = [
            [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)],
            [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)],
            [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)],
            [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)]
        ]

class SBlock(Block):
    def __init__(self, cell_size):
        super().__init__(id=5, cell_size=cell_size)
        self.states = [
            [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
            [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
            [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],
            [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)]
        ]


class TBlock(Block):
    def __init__(self, cell_size):
        super().__init__(id=6, cell_size=cell_size)
        self.states = [
            [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
            [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],
            [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
            [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)]
        ]

class ZBlock(Block):
    def __init__(self, cell_size):
        super().__init__(id=7, cell_size=cell_size)
        self.states = [
            [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
            [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],
            [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],
            [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)]
        ]
