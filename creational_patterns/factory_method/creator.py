from abc import ABC

from creational_patterns.factory_method.tetris_figure import TetrisFigure, Color, RightAngle, LeftAngle, Square, Line, \
    RightZigzag, LeftZigzag


class AbstractCreator(ABC):
    figure: type[TetrisFigure]

    def factory_method(self, color: Color) -> TetrisFigure:
        return self.figure(color)


class RightAngleCreator(AbstractCreator):
    figure = RightAngle


class LeftAngleCreator(AbstractCreator):
    figure = LeftAngle


class SquareCreator(AbstractCreator):
    figure = Square


class LineCreator(AbstractCreator):
    figure = Line


class RightZigzagCreator(AbstractCreator):
    figure = RightZigzag


class LeftZigzagCreator(AbstractCreator):
    figure = LeftZigzag