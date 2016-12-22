import arcade
from world import World, Tile, Map

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME = 0
GAME_OVER = 1


class HexSweepersGame(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height, "Hexaweepers")

        self.current_state = GAME
        self.world = World()
        arcade.set_background_color(arcade.color.WHITE)

    def draw_game(self):
        self.world.draw()

    def draw_game_over(self):
        output = "Game Over"
        arcade.draw_text(output, 400, 300, arcade.color.BLACK, 54, align="center",
                         anchor_x="center", anchor_y="center")

    def on_draw(self):
        arcade.start_render()
        if self.current_state == GAME:
            self.draw_game()

        elif self.current_state == GAME_OVER:
            self.draw_game()
            self.draw_game_over()

    def animate(self, delta_time):
        if self.world.is_game_over == True:
            self.current_state = GAME_OVER

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        if button == 1:
            self.world.onclick_left(x, y)

        if button == 4:
            self.world.onclick_right(x, y)


def main():
    window = HexSweepersGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()
