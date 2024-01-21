from abc import ABC
from enum import Enum


class Color(Enum):
    WHITE = "⬜"
    BLACK = "⬛"
    BLUE = "🟦"
    GREEN = "🟩"
    RED = "🟥"
    YELLOW = "🟨"
    ORANGE = "🟧"
    PURPLE = "🟪"
    BROWN = "🟫"


class TetrisFigure(ABC):
    figure: list[list[int]]

    def __init__(self, color: Color = Color.BLACK):
        self.color = color

    def get_colorful(self) -> str:
        colorful = ""
        for line in self.figure:
            for num in line:
                if num == 0:
                    colorful += Color.WHITE.value
                else:
                    colorful += self.color.value
            colorful += "\n"
        return colorful

    def __str__(self):
        return self.get_colorful()


class RightAngle(TetrisFigure):
    figure = [[1, 1],
              [1, 0],
              [1, 0]]


class LeftAngle(TetrisFigure):
    figure = [[1, 1],
              [0, 1],
              [0, 1]]


class Square(TetrisFigure):
    figure = [[1, 1],
              [1, 1]]


class Line(TetrisFigure):
    figure = [[1],
              [1],
              [1],
              [1]]


class RightZigzag(TetrisFigure):
    figure = [[0, 1, 1],
              [1, 1, 0]]


class LeftZigzag(TetrisFigure):
    figure = [[1, 1, 0],
              [0, 1, 1]]
