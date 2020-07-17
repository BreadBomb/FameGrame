import pygame
from pygame import draw, rect

class TetrominoPosition():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Tetromino():
    def __init__(self, _id, color, block):
        self.id = _id
        self.position = TetrominoPosition(0, 0)
        self.color = color
        self.block = block


class Tetris():
    def __init__(self):
        self.gamefield_x = 10
        self.gamefield_y = 6

        self.gamefield = []

        self.active_tetromino = None

        self.tetrominos = [
            Tetromino(
                "i",
                (0, 240, 239),
                [
                    [0, 0, 0, 0],
                    [1, 1, 1, 1]
                ]
            ),
            Tetromino(
                "j",
                (0, 0, 240),
                [
                    [1, 0, 0],
                    [1, 1, 1]
                ]
            ),
            Tetromino(
                "l",
                (241, 162, 0),
                [
                    [0, 0, 1],
                    [1, 1, 1]
                ]
            ),
            Tetromino(
                "o",
                (241, 240, 0),
                [
                    [1, 1],
                    [1, 1]
                ]
            ),
            Tetromino(
                "s",
                (0, 240, 0),
                [
                    [1, 1],
                    [1, 1]
                ]
            ),
            Tetromino(
                "t",
                (160, 0, 240),
                [
                    [0, 1, 0],
                    [1, 1, 1]
                ]
            ),
            Tetromino(
                "z",
                (240, 0, 0),
                [
                    [1, 1, 0],
                    [0, 1, 1]
                ]
            )
        ]

        self.init_gamefield()

        tetromino = self.get_tetromino("j")
        tetromino.position = TetrominoPosition(3, 0)

        self.add_tetromino_on_gamefield(tetromino)

        pass

    def init_gamefield(self):
        self.gamefield = [
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", ""],
        ]

    def get_tetromino(self, _id):
        for tetronimo in self.tetrominos:
            if tetronimo.id == _id:
                return tetronimo
        return None

    def add_tetromino_on_gamefield(self, tetromino):
        for y in range(len(tetromino.block)):
            for x in range(len(tetromino.block[y])):
                if tetromino.block[y][x] == 1:
                    self.gamefield[tetromino.position.y + y][tetromino.position.x + x] = tetromino.id

    def run(self, surface):
        draw.rect(surface, (255, 255, 255), (self.gamefield_x, self.gamefield_y, 12, 22), 1)

        self.draw_gamefrield(surface)

    def draw_gamefrield(self, surface):
        for y in range(len(self.gamefield)):
            for x in range(len(self.gamefield[y])):
                if self.gamefield[y][x] == "":
                    surface.set_at((self.gamefield_x + 1 + x, self.gamefield_y + 1 + y), (0, 0, 0))
                else:
                    tetromino = self.get_tetromino(self.gamefield[y][x])
                    surface.set_at((self.gamefield_x + 1 + x, self.gamefield_y + 1 + y), tetromino.color)
