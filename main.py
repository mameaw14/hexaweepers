import arcade
from world import World, Tile, Map

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME = 0
GAME_OVER = 1
class HexSweepersGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        self.current_state = GAME
        self.world = World()
        arcade.set_background_color(arcade.color.WHITE)
        # Note:
        # You can change how often the animate() method is called by using the
        # set_update_rate() method in the parent class.
        # The default is once every 1/80 of a second.
        # self.set_update_rate(1/80)
    
    def draw_game(self):
        self.world.draw()
    
    def draw_game_over(self):
        output = "Game Over"
        arcade.draw_text(output, 400, 300, arcade.color.BLACK, 54, align="center",
                         anchor_x="center", anchor_y="center")

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()
        if self.current_state == GAME:
            self.draw_game()
        
        elif self.current_state == GAME_OVER:
            self.draw_game()
            self.draw_game_over()

    def animate(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        """
        if self.world.is_game_over == True:
            self.current_state = GAME_OVER

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://pythonhosted.org/arcade/arcade.key.html
        """

        # See if the user hit Shift-Space
        # (Key modifiers are in powers of two, so you can detect multiple
        # modifiers by using a bit-wise 'and'.)
        if key == arcade.key.SPACE and key_modifiers == arcade.key.MOD_SHIFT:
            print("You pressed shift-space")

        # See if the user just hit space.
        elif key == arcade.key.SPACE:
            print("You pressed the space bar.")

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.SPACE:
            print("You stopped pressing the space bar.")

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        if button == 1:
            self.world.onclick_left(x, y)
        
        if button == 4:
            self.world.onclick_right(x, y)

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass

def main():
    window = HexSweepersGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()