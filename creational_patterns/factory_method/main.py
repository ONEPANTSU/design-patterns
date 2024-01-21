import random

from creational_patterns.factory_method.client import Client
from creational_patterns.factory_method.creator import RightAngleCreator, LeftAngleCreator, SquareCreator, LineCreator, \
    RightZigzagCreator, LeftZigzagCreator

for _ in range(10):
    shape = random.randint(1, 6)

    match shape:
        case 1: client = Client(RightAngleCreator())
        case 2: client = Client(LeftAngleCreator())
        case 3: client = Client(SquareCreator())
        case 4: client = Client(LineCreator())
        case 5: client = Client(RightZigzagCreator())
        case 6: client = Client(LeftZigzagCreator())
        case _: client = Client()

    color = random.randint(1, 8)

    match color:
        case 1: figure = client.get_red()
        case 2: figure = client.get_blue()
        case 3: figure = client.get_black()
        case 4: figure = client.get_brown()
        case 5: figure = client.get_green()
        case 6: figure = client.get_orange()
        case 7: figure = client.get_purple()
        case 8: figure = client.get_yellow()
        case _: figure = client.get_black()

    print(str(figure))
