import math
import time

import arcade



window = arcade.Window(title="2D Maze Runne",
    width=1280,
    height=720,
    resizable= True)

class MainMenu(arcade.View):

    def __init__(self):
        super().__init__()

        # Load sprites
        self.background = arcade.Sprite(
            "assets/menu/Background.png"
        )

        self.maincircle = arcade.Sprite(
            "assets/menu/MainCircle.png"
        )

        self.corners = arcade.Sprite(
            "assets/menu/Corners.png"
        )

        self.cross = arcade.Sprite(
            "assets/menu/Cross.png"
        )

        self.text = arcade.Sprite(
            "assets/menu/Text.png"
        )

        # Original Figma resolution
        self.design_width = 1920
        self.design_height = 1080

        # Sprite storage
        self.sprites = [
            self.background,
            self.maincircle,
            self.corners,
            self.cross,
            self.text
        ]

        self.menu_sprites = arcade.SpriteList()
        for sprite in self.sprites:
            self.menu_sprites.append(sprite)

        # Prevent resize recursion
        self.resizing = False

        # Initial scaling
        self.resize_sprites(
            self.window.width,
            self.window.height
        )

        # Transition variables
        self.transitioning = False
        self.transition_radius = 0
        self.transition_speed = 1000

    # Scale and position sprites
    def resize_sprites(self, width, height):
        self.scale = min(
            width / self.design_width,
            height / self.design_height
        )

        # Actual window centre
        screen_center_x = width / 2
        screen_center_y = height / 2

        for sprite in self.sprites:
            sprite.scale = self.scale
            sprite.center_x = screen_center_x
            sprite.center_y = screen_center_y

    # Window resize
    def on_resize(self, width, height):

        if self.resizing:
            return

        self.resizing = True
        # Keep 16:9 ratio
        aspect_ratio = 16 / 9
        correct_height = int(
            width / aspect_ratio
        )

        if correct_height != height:
            self.window.set_size(
                width,
                correct_height
            )
        self.resize_sprites(
            self.window.width,
            self.window.height
        )
        self.resizing = False

    # Draw
    def on_draw(self):
        self.clear()
        self.menu_sprites.draw()

        # Hyper-drive flash
        if self.transitioning:

            arcade.draw_circle_filled(
                center_x=self.window.width / 2,
                center_y=self.window.height / 2,
                radius=self.transition_radius,
                color=arcade.color.WHITE
            )

    # Update
    def on_update(self, delta_time):

        if self.transitioning:

            self.transition_radius += (
                self.transition_speed * delta_time
            )


            if self.transition_radius > max(
                self.window.width,
                self.window.height
            ) * 2:

                # Switch to game view here
                pass

    # Mouse input
    def on_mouse_press(
        self,
        x,
        y,
        button,
        modifiers
    ):

        if button == arcade.MOUSE_BUTTON_LEFT:

            self.transitioning = True

class PauseView(arcade.View):
    pass

class InGameView(arcade.View):
    pass

class WinView(arcade.View):
    pass

class LostView(arcade.View):
    pass


game = MainMenu()
window.show_view(game)

arcade.run()
