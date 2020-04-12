from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.button import Button
import kivy
kivy.require("1.9.1")


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


class ButtonApp(App):

    def build(self):
        # use a (r, g, b, a) tuple
        btn = Button(text="Push Me !",
                     font_size="20sp",
                     background_color=(1, 1, 1, 1),
                     color=(1, 1, 1, 1),
                     size=(32, 32),
                     size_hint=(.2, .2),
                     pos=(300, 250))


        # bind() use to bind the button to function callback
        btn.bind(on_press=self.callback)
        return btn

    # callback function tells when button pressed
    def callback(self, event):
        print("button pressed")
        print('Yoooo !!!!!!!!!!!')



class MainApp(App):
    def on_start(self):
        Clock.schedule_interval(self.root.ids.background.scroll_textures, 1/500.)
        root = ButtonApp()
        root.run()
    pass


MainApp().run()