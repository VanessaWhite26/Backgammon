import kivy
from kivy.uix.stacklayout import StackLayout

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
Builder.load_string("""




         

<Button>:
    font_name: 'Arial'
    font_size: 45
    bold: True
    color: 0, 1, 0, 1
    size_hint: 0.3,0.2
    size: self.texture_size
    background_normal: 'leather.png'
    background_down: 'downleather.png'
    



<ScreenMenu>:
    FloatLayout:
        Background: 
            id: background
            canvas.before:
                
                Rectangle:
                    size: self.size
                    pos: self.pos
                    source: "menuBackground.png"
    
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
                        root.manager.transition.direction = 'down'
                        root.manager.transition.duration = 1
                        root.manager.current = 'screen_scores'
                
                Button:
                    pos_hint:{"top": 1,"left": 2}
                    text: "QUIT?"
                    
                    on_press:
                        exit()
        

<ScreenGame>:
    # FloatLayout:
    #     Background: 
    #         id: background
    #         canvas.before:
    #             Rectangle:
    #                 size: self.size
    #                 pos: self.pos
    #                 source: "backgroundMenu.png"
    #             Rectangle:
    #                 size: self.width, 138
    #                 pos: self.pos[0], self.pos[1] + self.height -1200
    #                 texture: self.dice_texture
    #             Rectangle:
    #                 size: self.width, 500
    #                 pos: self.pos[0], self.pos[1] + self.height -300
    #                 texture: self.points_texture
    
    Board: 
        id: board
        canvas.before:
            Rectangle:
                size: self.size
                pos: self.pos
                source: "points.png"
        
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
    FloatLayout:
        Background:    
            id: background
            canvas.before:
                Rectangle:
                    size: self.size
                    pos: self.pos
                    source: "backgroundMenu.png"     
                Rectangle:
                    size: self.width, 138
                    pos: self.pos[0], self.pos[1] + self.height -138
                    texture: self.dice_texture
               
                        
                
            
        
        
        ScrollView:
            do_scroll_x: False
            do_scroll_y: True
            Label: 
                halign: 'left'
                valign: 'bottom'       
                size_hint: 1, None
                size: self.texture_size
                text:
                    '\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n\\n'+\
                    'Game Instructions: \\n\\n' +\
                    'Every roll presents the opportunity to move towards pieces to the end of the board \\n' +\
                    'Each player must roll two dice:\\n' +\
                    'If the dice is not a "doubles" then only two moves are allowed one for each number on the dice\\n' +\ 
                    'If the dice roll is a "doubles" meaning both of the dice have the same number then four moves of that number on the dice is allowed\\n' +\
                    '*No player is allowed to "pass" or not use their moves (there must be a move made every turn if possible)\\n\\n'+\
                    'A point with two or more pieces of the same colour on it is safe - the opponent cannot land a piece on such a point\\n'+\
                    'A point hosting only one piece is called a "blot"; Such a piece is vulnerable \\n'+\
                    'If the opponent lands on this point the piece is captured and moved to the bar\\n'+\
                    'This means physically placed on the middle bar dividing the board\\n\\n'+\
                    'Captured pieces are re-entered on the furthest point from the players inner table:\\n'+\
                    'A throw of 1 allows the piece to move from the bar to point one of the opponents inner table\\n'+\
                    'A throw of 5 allows the piece to enter at point 5 of the opponents inner table\\n\\n'+\
                    'If a player has one or more pieces on the bar, no other pieces can be moved until all such pieces have re-entered play: \\n'+\
                    'So if the dice throw and position of enemy pieces prevents a player from re-entering a piece onto the board from the bar\\n'+\
                    'the player cannot move any other piece and play passes to the opponent\\n'+\
                    'A point hosting two or more of the opponents pieces is said to be "blocked"\\n'+\
                    'If six points in a row are blocked, the opponent is said to have formed a "prime"\\n'+\
                    'This is a highly advantageous achievement because a prime cannot be traversed by an opponent\\n\\n'+\
                    'Bearing off: \\n\\n' +\
                    'Once all pieces are present in a players inner table, that player can start "bearing off"\\n'+\
                    'A throw of 1 allows a player to bear off a piece from point 1 of his inner table \\n'+\
                    'A throw of 2 allows a player to bear off a piece from point 2 of his inner table and so on\\n'+\
                    'Pieces borne off are simply removed from the board\\n\\n'+\
                    'When a player rolls a number that is higher than the highest point of the inner table upon which that player has pieces\\n'+\
                    'The player is allowed to bear off the next highest piece. For example, with a roll of double 5\\n'+\
                    'If the player has a piece on point 5, two pieces on point 3, one piece on point 2 and one piece on point 1\\n'+\
                    'The player would bear off the four highest placed pieces and be left with just one piece on point 1\\n\\n'+\
                    'Winner rules: \\n\\n' +\
                    'The first player to bear off all pieces wins the game \\n' +\
                    'If the opponent has borne off at least one piece, a single game is won and the current stake is forfeited \\n' +\
                    'If the opponent has not borne off any pieces, this is a "gammon" and worth double the current stake \\n' +\
                    'If the opponent has a piece left on the bar or within the opponents inner table, this is a "backgammon" and worth triple the current stake\\n\\n'+\
                    'Keyboard Movements: \\n\\n'+\
                    '\\n'*10
                    
                   #Instructions from https://www.mastersofgames.com/rules/backgammon-rules.htm   
        
            
                                          
                    
        
     
   
    
    BoxLayout:
        Button:
            text: "Main Menu"
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'screen_menu'        

<ScreenScores>:
    
    FloatLayout:
        Background: 
            id: background
            canvas.before:
                
                Rectangle:
                    size: self.size
                    pos: self.pos
                    source: "roll.png"
    BoxLayout:
        Button:
            text: "Main Menu"
            on_press:
                root.manager.transition.direction = 'up'
                root.manager.current = 'screen_menu'             
""")

##----------------------------------------------------------------------------------------------------------------------
class Board(Widget):

    board = []

    def build(self):
        # Config.set('graphics', 'width', '600')
        # Config.set('graphics', 'height', '600')
        self.layout = StackLayout()
        for x in range(3):
            bt = Button(text='', font_size=200, width=200, height=200, size_hint=(None, None), id=str(x))
            bt.bind(on_release=self.btn_pressed)
            self.board.append(bt)
            self.layout.add_widget(bt)
        return self.layout




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
            (self.dice_texture.uvpos[0] + time_passed) % Window.width, self.dice_texture.uvpos[0])
        self.points_texture.uvpos = (
            (self.points_texture.uvpos[0] - time_passed) % Window.width, self.points_texture.uvpos[1])
        # Redraw the texture
        texture = self.property("dice_texture")
        texture.dispatch(self)

        texture = self.property("points_texture")
        texture.dispatch(self)

    def on_start(self):
        Clock.schedule_interval(self.root.ids.background.scroll_textures, 1 / 500.)

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

    def build(self):
        return screen_manager

    pass

app = Backgammon()
app.run()