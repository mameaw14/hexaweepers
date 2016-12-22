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

    def __init__(self):
        self.map = Map(13, 20, self)
        self.numbers_of_mine = 0
        self.numbers_of_flagged = 0
        self.is_game_over = False

    def draw(self):
        self.map.draw()
        arcade.draw_text(str(self.numbers_of_mine), 20, 500, arcade.color.BLACK, 13,
                         width=40, align="center",
                         anchor_x="center", anchor_y="center")
        arcade.draw_text(str(self.numbers_of_flagged), 300, 500, arcade.color.BLACK, 13,
                         width=40, align="center",
                         anchor_x="center", anchor_y="center")

    def game_over(self):
        self.is_game_over = True
        self.map.reveal_all_tiles()

    def onclick_left(self, x, y):
        if self.map.onclick_left(x, y):
            self.game_over()

    def onclick_right(self, x, y):
        self.map.onclick_right(x, y)

class Map(object):
    """create map"""
    def __init__(self, row, col, world):
        self.row = row
        self.col = col
        self.world = world
        self.tiles_list = [[0] * col for i in range(row)]
        for i in range(0, row):
            for j in range(0, col):
                is_mine = random.random() < 0.2
                tile = Tile(30 + j * 38 + (i % 2 == 0) * 19, 50 + i * 35, is_mine,
                            self.get_neighbor_list(i, j))
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
                    if i.is_mine:
                        return 1
                    return 0

    def onclick_right(self, x, y):
        for row in self.tiles_list:
            for i in row:
                if i.check_onclick(x, y):
                    if i.state == State.hidden:
                        i.change_state(State.flagged)
                    elif i.state == State.flagged:
                        i.change_state(State.hidden)
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
            tile.change_state(State.clear)
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

    def reveal_all_tiles(self):
        for row in self.tiles_list:
            for i in row:
                i.change_state(State.clear)

class Tile(object):
    """hexagon blocks"""
    def __init__(self, x, y, is_mine, lis):
        self.x = x
        self.y = y
        self.neighbor_list = lis
        self.is_mine = is_mine
        self.state = State.hidden
        self.count_mine = 0
        self.point_list = ((x + 0, y - 20),
                           (x - 17, y - 10),
                           (x - 17, y + 10),
                           (x + 0, y + 20),
                           (x + 17, y + 10),
                           (x + 17, y - 10))
        if self.is_mine:
            self.color = arcade.color.SPANISH_VIOLET
        else:
            self.color = arcade.color.SPANISH_VIOLET

    def change_color(self, color):
        self.color = color

    def change_state(self, state):
        self.state = state
        if state == State.flagged:
            self.change_color(arcade.color.RUBY_RED)
            return
        if state == State.hidden:
            self.change_color(arcade.color.SPANISH_VIOLET)
        if state == State.clear:
            if self.is_mine:
                self.change_color(arcade.color.SALMON)
            else:
                self.change_color(arcade.color.LIGHT_PASTEL_PURPLE)

    def draw(self):
        if self.state == State.flagged:
            self.change_color(arcade.color.TANGELO)

        arcade.draw_polygon_filled(self.point_list, self.color)

        if self.state == State.clear and self.count_mine != 0 and not self.is_mine:
            arcade.draw_text(str(self.count_mine), self.x, self.y, arcade.color.WHITE, 10,
                             width=40, align="center",
                             anchor_x="center", anchor_y="center")

    def check_onclick(self, x, y):
        return arcade.are_polygons_intersecting(self.point_list, ((x, y), (x - 1, y), (x, y + 1)))
