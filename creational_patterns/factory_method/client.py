from creational_patterns.factory_method.creator import AbstractCreator
from creational_patterns.factory_method.tetris_figure import Color


class Client:
    def __init__(self, creator: AbstractCreator = AbstractCreator()):
        self.creator = creator

    def get_red(self):
        return self.creator.factory_method(color=Color.RED)

    def get_green(self):
        return self.creator.factory_method(color=Color.GREEN)

    def get_black(self):
        return self.creator.factory_method(color=Color.BLACK)

    def get_blue(self):
        return self.creator.factory_method(color=Color.BLUE)

    def get_brown(self):
        return self.creator.factory_method(color=Color.BROWN)

    def get_yellow(self):
        return self.creator.factory_method(color=Color.YELLOW)

    def get_orange(self):
        return self.creator.factory_method(color=Color.ORANGE)

    def get_purple(self):
        return self.creator.factory_method(color=Color.PURPLE)