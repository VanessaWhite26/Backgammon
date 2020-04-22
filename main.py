import kivy

kivy.require('1.9.0')


from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.base import runTouchApp
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label

import kivy
from kivy.clock import Clock
from kivy.config import Config
from kivy.core.window import Window
##----------------------------------------------------------------------------------------------------------------------
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '750')
Window.size = (1000, 750)
##----------------------------------------------------------------------------------------------------------------------
# You can create your kv code in the Python file
root = Builder.load_string("""

# 
# Background: 
#     id: background
#     canvas.before:
#         Rectangle:
#             size: self.size
#             pos: self.pos
#             source: "backgroundMenu.png"
#         Rectangle:
#             size: self.width, 138
#             pos: self.pos[0], self.pos[1] + self.height -138
#             texture: self.dice_texture
#         Rectangle:
#             size: self.width, 500
#             pos: self.pos[0], self.pos[1]
#             texture: self.points_texture


<Button>:
    font_name: 'Arial'
    font_size: 25
    bold: True
    color: 0, 1, 0, 1
    size_hint: 0.3,0.2
    background_normal: 'leather.png'
    background_down: 'downleather.png'
    



<ScreenMenu>:
    
    FloatLayout:
        BoxLayout:
            orientation: "vertical"
            BoxLayout:
                Button:
                    pos_hint:{"top": 1,"left": 1}
                    text: "Need Help?"
                    
                    on_press:
                        # You can define the duration of the change
                        # and the direction of the slide
                        root.manager.transition.direction = 'right'
                        root.manager.transition.duration = 1
                        root.manager.current = 'screen_help'
                        
                
     
                Button:
                    pos_hint:{"top": 1,"right": 1}
                    text: "Play Backgammon?"
                    
                    on_press:
                        # You can define the duration of the change
                        # and the direction of the slide
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 1
                        root.manager.current = 'screen_game'
                    
                Button:
                    pos_hint:{"top": 1,"right": 2}
                    text: "Scores"
                    
                    on_press:
                        # You can define the duration of the change
                        # and the direction of the slide
                        root.manager.transition.direction = 'up'
                        root.manager.transition.duration = 1
                        root.manager.current = 'screen_scores'
                
                Button:
                    pos_hint:{"top": 1,"left": 2}
                    text: "QUIT?"
                    
                    on_press:
                        exit()
        

<ScreenGame>:
    BoxLayout:
        Button:
            text: "Main Menu"
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'screen_menu'
        Button:
            text: "Quit"
            on_press:
                exit()
                
<ScreenHelp>:                          
                 
    ScrollView:
        Label:        
            size_hint: None, None
            size: self.texture_size
            text: ' Game Instructions: \\n Every roll presents the opportunity to move towards pieces to the end of the board \\n Each player must roll two dice:' * 50    
                # 'If the dice is not a 'doubles' then only two moves are allowed one for each number on the dice '
                # If the dice roll is a 'doubles' meaning both of the dice have the same number then four moves of that number on the dice is allowed  
                # *No player is allowed to 'pass' or not use their moves (there must be a move made every turn if possible)"
    
    BoxLayout:
        Button:
            text: "Main Menu"
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'screen_menu'            
                
                
<ScreenScores>:
    BoxLayout:
        Button:
            text: "Main Menu"
            on_press:
                root.manager.transition.direction = 'down'
                root.manager.current = 'screen_menu'             
""")

##----------------------------------------------------------------------------------------------------------------------
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

##----------------------------------------------------------------------------------------------------------------------
# Create a class for all screens in which you can include
# helpful methods specific to that screen
class ScreenMenu(Screen):
    pass

class ScreenGame(Screen):
    pass

class ScreenHelp(Screen):
    pass

class ScreenScores(Screen):
    pass

##----------------------------------------------------------------------------------------------------------------------
# The ScreenManager controls moving between screens
screen_manager = ScreenManager()

# Add the screens to the manager and then supply a name
# that is used to switch screens
screen_manager.add_widget(ScreenMenu(name="screen_menu"))
screen_manager.add_widget(ScreenGame(name="screen_game"))
screen_manager.add_widget(ScreenHelp(name="screen_help"))
screen_manager.add_widget(ScreenScores(name="screen_scores"))

##----------------------------------------------------------------------------------------------------------------------

class Backgammon(App):
    # def on_start(self):
    #     Clock.schedule_interval(self.root.ids.background.scroll_textures, 1 / 500.)

    def build(self):
        return screen_manager


app = Backgammon()
app.run()