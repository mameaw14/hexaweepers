import arcade
from enum import Enum
import random

class State(Enum):
    hidden = 1
    flagged = 2
    marked = 3

class World(object):
    """world class"""
    def __init__(self):
        self.x = 9
    def animate(self, delta):
        self.x

class Map(object):
    """create map"""
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.hexa_list = [[0] * col for i in range(row)]
        for i in range(0, row):
            for j in range(0, col):
                hexa = Hexa(30 + j * 38 + (i % 2 == 0) * 19, 50 + i * 35)
                self.hexa_list[i][j] = hexa

    def draw(self):
        for row in self.hexa_list:
            for i in row:
                i.draw()
    
    def onclick(self, x , y):
        for row in self.hexa_list:
            for i in row:
                if(i.check_onclick(x, y)):
                    i.click()

class Hexa(object):
    """hexagon blocks"""
    def __init__(self, x, y):
        self.is_mine = random.random() < 0.1
        self.state = State.hidden
        self.point_list = ((x + 0, y - 20),
                           (x - 17, y - 10),
                           (x - 17, y + 10),
                           (x + 0, y + 20),
                           (x + 17, y + 10),
                           (x + 17, y - 10))
        if self.is_mine:
            self.color = arcade.color.SPANISH_RED
        else:
            self.color = arcade.color.SPANISH_VIOLET

    def draw(self):
        if self.state == State.flagged:
            return
        arcade.draw_polygon_filled(self.point_list, self.color)

    def check_onclick(self, x, y):
        return arcade.are_polygons_intersecting(self.point_list, ((x, y), (x - 1, y), (x, y + 1)))
    
    def click(self):
        self.state = State.flagged
