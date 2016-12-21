import arcade

def main():
    """main"""
    arcade.open_window("Drawing Example", 600, 600)
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()

    point_list = ((150, 250),
                  (107, 275),
                  (107, 325),
                  (150, 350),
                  (193, 325),
                  (193, 275))
    arcade.draw_polygon_filled(point_list, arcade.color.SPANISH_VIOLET)

    arcade.finish_render()
    arcade.run()

if __name__ == "__main__":
    main()
