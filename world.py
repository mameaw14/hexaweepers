import arcade
from enum import Enum
import random

class State(Enum):
    hidden = 1
    flagged = 2
    marked = 3
    clear = 4

class World(object):
    """world class"""
    numbers_of_mine = 0
    def __init__(self):
        self.x = 1

    def draw(self):
        arcade.draw_text(str(self.numbers_of_mine), 20, 500, arcade.color.BLACK, 13,
                         width=40, align="center",
                         anchor_x="center", anchor_y="center")

class Map(object):
    """create map"""
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.tiles_list = [[0] * col for i in range(row)]
        for i in range(0, row):
            for j in range(0, col):
                tile = Tile(30 + j * 38 + (i % 2 == 0) * 19, 50 + i * 35, self.get_neighbor_list(i, j))
                self.tiles_list[i][j] = tile

        self.calculate_status()

    def draw(self):
        for row in self.tiles_list:
            for i in row:
                i.draw()

    def onclick_left(self, x, y):
        for row in self.tiles_list:
            for i in row:
                if i.check_onclick(x, y):
                    self.update(self.tiles_list.index(row), row.index(i))
                    i.onclick_left()
                    return
    
    def onclick_right(self, x, y):
        for row in self.tiles_list:
            for i in row:
                if i.check_onclick(x, y):
                    i.onclick_right()
                    return

    def get_neighbor_list(self, i, j):
        lis = [(i, j - 1), (i, j + 1)]

        if i % 2 == 0:
            j += 1

        lis.append((i - 1, j - 1))
        lis.append((i - 1, j))
        lis.append((i + 1, j - 1))
        lis.append((i + 1, j))
        copy_list = list(lis)

        for i, j in copy_list:
            if i < 0 or i >= self.row or j < 0 or j >= self.col:
                lis.remove((i, j))

        return lis

    def update(self, i, j):
        tile = self.tiles_list[i][j]
        if tile.is_mine != True and tile.state != State.clear:
            tile.color = arcade.color.AFRICAN_VIOLET
            tile.state = State.clear
            if tile.count_mine != 0:
                return
        else:
            return

        neighbor_list = self.tiles_list[i][j].neighbor_list
        for x, y in neighbor_list:
            self.update(x, y)

    def calculate_status(self):
        for i in range(0, self.row):
            for j in range(0, self.col):
                if self.tiles_list[i][j].is_mine:
                    neighbor_list = self.tiles_list[i][j].neighbor_list
                    for x, y in neighbor_list:
                        self.tiles_list[x][y].count_mine += 1

class Tile(object):
    """hexagon blocks"""
    def __init__(self, x, y, lis):
        self.x = x
        self.y = y
        self.neighbor_list = lis
        self.is_mine = random.random() < 0.1
        self.state = State.hidden
        self.count_mine = 0
        self.point_list = ((x + 0, y - 20),
                           (x - 17, y - 10),
                           (x - 17, y + 10),
                           (x + 0, y + 20),
                           (x + 17, y + 10),
                           (x + 17, y - 10))
        if self.is_mine:
            self.color = arcade.color.SPANISH_RED
            World.numbers_of_mine += 1
        else:
            self.color = arcade.color.SPANISH_VIOLET

    def draw(self):
        if self.state == State.flagged:
            self.color = arcade.color.TANGELO
        
        arcade.draw_polygon_filled(self.point_list, self.color)
        arcade.draw_text(str(self.count_mine), self.x, self.y, arcade.color.WHITE, 10,
                         width=40, align="center",
                         anchor_x="center", anchor_y="center")

    def check_onclick(self, x, y):
        return arcade.are_polygons_intersecting(self.point_list, ((x, y), (x - 1, y), (x, y + 1)))

    def onclick_left(self):
        self.state = State.clear

    def onclick_right(self):
        if self.state != State.flagged:
            self.state = State.flagged
        else:
            self.state = State.hidden

