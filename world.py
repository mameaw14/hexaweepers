import arcade
"""control object in game"""
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
        self.hexa_list = []
        for i in range(0, row):
            for j in range(0, col):
                hexa = Hexa(30 + j * 38 + (i % 2 == 0) * 19, 50 + i * 35)
                self.hexa_list.append(hexa)

    def draw(self):
        for i in self.hexa_list:
            i.draw()

class Hexa(object):
    """hexagon blocks"""
    def __init__(self, x, y):
        self.point_list = ((x + 0, y - 20),
                           (x - 17, y - 10),
                           (x - 17, y + 10),
                           (x + 0, y + 20),
                           (x + 17, y + 10),
                           (x + 17, y - 10))

    def draw(self):
        arcade.draw_polygon_filled(self.point_list, arcade.color.SPANISH_VIOLET)
