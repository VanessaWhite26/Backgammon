from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.button import Button

class Background(Widget):
    dice_texture = ObjectProperty(None)
    points_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #create textures
        self.dice_texture = Image(source="pieces.png").texture
        self.dice_texture.wrap = 'repeat'
        self.dice_texture.uvsize = (Window.width / self.dice_texture.width, -1)

        self.points_texture = Image(source="points.png").texture
        self.points_texture.wrap = 'repeat'
        self.points_texture.uvsize = (Window.width / self.dice_texture.width, -1)


    def callback(self):
        self.hello = Button(text = "hello")
        # create a button
        # btn1 = Button(text="Start")
        # btn1.bind(on_press = callback)
        # btn2 = Button (text = "Help")
        # btn2.bind(on_press = callback)
        # btn3 = Button(text = "Exit")
        # btn3.bind(on_press = callback)
    pass


    def scroll_textures(self, time_passed):
        #update the uvpos
        self.dice_texture.uvpos = ((self.dice_texture.uvpos[0] + time_passed)%Window.width, self.dice_texture.uvpos[1])
        self.points_texture.uvpos = ((self.points_texture.uvpos[0] - time_passed) % Window.width, self.points_texture.uvpos[1])
        #Redraw the texture
        texture = self.property("dice_texture")
        texture.dispatch(self)

        texture = self.property("points_texture")
        texture.dispatch(self)
    pass

from kivy.clock import Clock


class MainApp(App):
    def on_start(self):
        Clock.schedule_interval(self.root.ids.background.scroll_textures, 1/500.)
    pass


MainApp().run()