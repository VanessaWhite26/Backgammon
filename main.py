from kivy.app import App
from kivy.core.text import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import (ScreenManager, Screen, NoTransition,
                                    SlideTransition, CardTransition, SwapTransition,
                                    FadeTransition, WipeTransition, FallOutTransition, RiseInTransition)

from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.lang import Builder
import kivy

kivy.require("1.9.1")


# ----------------------------------------------------------------------------------------------------------
# Background/ Menu class
class Background(Widget):
    dice_texture = ObjectProperty(None)
    points_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # create textures
        self.dice_texture = Image(source="pieces.png").texture
        self.dice_texture.wrap = 'repeat'
        self.dice_texture.uvsize = (Window.width / self.dice_texture.width, -1)

        self.points_texture = Image(source="points.png").texture
        self.points_texture.wrap = 'repeat'
        self.points_texture.uvsize = (Window.width / self.dice_texture.width, -1)

    def scroll_textures(self, time_passed):
        # update the uvpos
        self.dice_texture.uvpos = (
            (self.dice_texture.uvpos[0] + time_passed) % Window.width, self.dice_texture.uvpos[1])
        self.points_texture.uvpos = (
            (self.points_texture.uvpos[0] - time_passed) % Window.width, self.points_texture.uvpos[1])
        # Redraw the texture
        texture = self.property("dice_texture")
        texture.dispatch(self)

        texture = self.property("points_texture")
        texture.dispatch(self)

    pass


# ----------------------------------------------------------------------------------------------------------
# Button class

class ButtonApp(App):

    def build(self):
        # Create a widget to bold the buttons
        start = Widget()

        # Create the buttons
        startButton = Button(text="Start",
                             font_size="20sp",
                             background_color=(1, 1, 1, 1),
                             color=(1, 1, 1, 1),
                             size=(100, 75),
                             size_hint=(.2, .2),
                             pos=(Window.width / 2 - 50, Window.height / 2 + 50))

        helpButton = Button(text="Help",
                            font_size="20sp",
                            background_color=(1, 1, 1, 1),
                            color=(1, 1, 1, 1),
                            size=(100, 75),
                            size_hint=(.2, .2),
                            pos=(Window.width / 2 - 50, Window.height / 2 - 50))

        exitButton = Button(text="Exit",
                            font_size="20sp",
                            background_color=(1, 1, 1, 1),
                            color=(1, 1, 1, 1),
                            size=(100, 75),
                            size_hint=(.2, .2),
                            pos=(Window.width / 2 - 50, Window.height / 2 - 150))

        start.add_widget(startButton)
        start.add_widget(helpButton)
        start.add_widget(exitButton)

        # bind() use to bind the button to function callback
        startButton.bind(on_press=self.startGame)
        helpButton.bind(on_press=self.helpPage)
        exitButton.bind(on_press=self.exitGame)

        return start

    # Use startGame, helpPage, exitGame to give functionality to each of the buttons pressed
    def startGame(self, event):
        print("game started")
        MainApp().run().screenManager.current = "game"

    def helpPage(self, event):
        print("Heading to the help page")

    def exitGame(self, event):
        exit()


# ----------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------
class board(App):
    def build(self):
        return Label(text="Game Yes!!")


# ----------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------
class MainApp(App):
    def on_start(self):
        self.screenManager = ScreenManager()
        self.menu = Clock.schedule_interval(self.root.ids.background.scroll_textures, 1 / 500.)
        self.root = ButtonApp().run()
        screen = Screen(name="menu")
        screen2 = Screen(name="buttons")
        screen.add_widget(self.menu)
        screen.add_widget(self.root)
        self.screenManager.add_widget(screen)
        self.screenManager.add_widget(screen2)

        self.board = board()
        screen = Screen(name="game")
        screen.add_widget(self.board)
        self.screenManager.add_widget(screen)

        return self.screenManager


MainApp().run()
