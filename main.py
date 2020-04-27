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
from kivy.uix.textinput import TextInput
from kivy.graphics import *

import kivy
from kivy.clock import Clock
from kivy.config import Config
from kivy.core.window import Window


from random import randint
import time

##----------------------------------------------------------------------------------------------------------------------
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '750')
Window.size = (1000, 750)
##----------------------------------------------------------------------------------------------------------------------
# You can create your kv code in the Python file
Builder.load_string("""


<MyInstructions@Label>:
    color:1, 1 ,1,1
    text:
        '\\n\\n\\n\\n'+\
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

    size_hint_y:None
    height: self.texture_size[1]



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
                    font_name: 'Arial'
                    font_size: 25
                    bold: True
                    color: 0, 1, 0, 1
                    size_hint: 0.3,0.2
                    background_normal: 'leather.png'
                    background_down: 'downleather.png'
                    pos_hint:{"top": 1,"left": 1}
                    text: "Need Help?"

                    on_press:
                        # You can define the duration of the change
                        # and the direction of the slide
                        root.manager.transition.direction = 'right'
                        root.manager.transition.duration = 1
                        root.manager.current = 'screen_help'



                Button:
                    font_name: 'Arial'
                    font_size: 25
                    bold: True
                    color: 0, 1, 0, 1
                    size_hint: 0.3,0.2
                    background_normal: 'leather.png'
                    background_down: 'downleather.png'
                    pos_hint:{"top": 1,"right": 1}
                    text: "Play Backgammon?"

                    on_press:
                        # You can define the duration of the change
                        # and the direction of the slide
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 1
                        root.manager.current = 'screen_game'

                Button:
                    font_name: 'Arial'
                    font_size: 25
                    bold: True
                    color: 0, 1, 0, 1
                    size_hint: 0.3,0.2
                    background_normal: 'leather.png'
                    background_down: 'downleather.png'
                    pos_hint:{"top": 1,"right": 2}
                    text: "Scores"

                    on_press:
                        # You can define the duration of the change
                        # and the direction of the slide
                        root.manager.transition.direction = 'up'
                        root.manager.transition.duration = 1
                        root.manager.current = 'screen_scores'

                Button:
                    font_name: 'Arial'
                    font_size: 25
                    bold: True
                    color: 0, 1, 0, 1
                    size_hint: 0.3,0.2
                    background_normal: 'leather.png'
                    background_down: 'downleather.png'
                    pos_hint:{"top": 1,"left": 2}
                    text: "QUIT?"

                    on_press:
                        exit()


<ScreenGame>:
    GridLayout:
        cols:2
        size_hint: 1,0.35
        rows:3
        
        Label:
            id: board
            font_name: 'Arial'
            font_size: 25
            bold: True
            color: 0, 1, 0, 1
            
            text: "Board array here"
            
        Label:
            id: bar
            font_name: 'Arial'
            font_size: 25
            bold: True
            color: 0, 1, 0, 1
            
            text: "Bar array here"
        
        
        Label:
            id: outlabel
            font_name: 'Arial'
            font_size: 25
            bold: True
            color: 0, 1, 0, 1

            text: "Let's Play!"              
            
        TextInput:
            id: userinput
            multiline: False
            
            font_name: 'Arial'
            font_size: 25
            bold: True
            color: 0, 1, 0, 1

            text: "User Input "
           
           # when user presses enter:  
            on_text_validate:
                app.getUserInput(userinput)
                app.changeLabelText(outlabel, "test")

        Button:
            font_name: 'Arial'
            font_size: 25
            bold: True
            color: 0, 1, 0, 1 
            background_normal: 'leather.png'
            background_down: 'downleather.png'

            text: "Main Menu"

            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'screen_menu'
                
        Button:
            font_name: 'Arial'
            font_size: 25
            bold: True
            color: 0, 1, 0, 1 
            background_normal: 'leather.png'
            background_down: 'downleather.png'

            text: "Quit"
            on_press:
                exit()

<ScreenHelp>:                             
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
    #                 pos: self.pos[0], self.pos[1] + self.height -950
    #                 texture: self.dice_texture
    #             Rectangle:
    #                 size: self.width, 500
    #                 pos: self.pos[0], self.pos[1] + self.height -300
    #                 texture: self.points_texture


    ScrollView:
        GridLayout:
            cols:1    
            size_hint_y: None 
            height: self.minimum_height 

            MyInstructions:


    BoxLayout:
        Button:
            font_name: 'Arial'
            font_size: 25
            bold: True                
            color: 0, 1, 0, 1
            size_hint: 0.3,0.2
            background_normal: 'leather.png'
            background_down: 'downleather.png'
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
            font_name: 'Arial'
            font_size: 25
            bold: True
            color: 0, 1, 0, 1
            size_hint: 0.3,0.2
            background_normal: 'leather.png'
            background_down: 'downleather.png'
            text: "Main Menu"
            on_press:
                root.manager.transition.direction = 'up'
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

    def main(self):
        # create board
        # def initialize():
        light_zone = 0  # positive endzone
        dark_zone = 0  # negative endzone
        center_bar = [0, 0]  # first num is positives on bar, second is negatives

        # Initialize board, positive nums are light peices, negative nums are dark peices
        board = [0, 2, 0, 0, 0, 0, -5, 0, -3, 0, 0, 0, 5,
                 -5, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, -2, 0]

        # this is the main function
        # board = initialize()

        # some game logic

        # fix later to allow roll to determine turn
        init_turn = randint(0, 1)  # if 0 then dark starts, if 1 then light starts
        print(board)
        print(center_bar)

        if (init_turn == 0):
            turn = -1
        else:
            turn = 1

        # alternates between player turns until game finishes
        while (abs(light_zone) < 15 and abs(dark_zone) < 15):
            if (turn == -1):
                print('Dark turn')
                moves = roll()
                makeMoves(moves)
                # movePiece(5,turn)
            else:
                print('Light turn')
                moves = roll()

                makeMoves(moves)

            time.sleep(2)
            turn = turn * -1

        # add check for overflowing board edge

    def roll():
        moves = [0, 0, 0, 0]
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)
        print('you got ' + str(dice1) + ' and ' + str(dice2))
        moves[0] = dice1
        moves[1] = dice2

        if (dice1 == dice2):
            print('you get four moves of ' + str(dice1))
            moves[2] = dice1
            moves[3] = dice1
        else:
            print('you get one move of ' + str(dice1) + ' and one move of ' + str(dice2))
        return moves

    # makes moves
    def makeMoves(moves):
        while (numpy.sum(moves) > 0):
            move_valid = False
            rand_index = 0
            rand_move = 0

            possible_moves = 0
            if turn == 1:
                for i in range(25):
                    for j in range(4):
                        if moves[j] > 0 and i + moves[j] < 25:
                            if board[i] > 0 and board[i + moves[j]] > -2:
                                possible_moves = possible_moves + 1
            elif turn == -1:
                # for i in range(25):
                #  for j in range (4):
                #    if moves[j]>0 and i - moves[j]>0:
                #      if board[i]<0 and board[i - moves[j]]<2:
                #        possible_moves = possible_moves+1
                for i in range(25):
                    for j in range(4):
                        if moves[j] > 0 and i - moves[j] > 0:
                            if board[i] < 0 and board[i - moves[j]] < 2:
                                possible_moves = possible_moves + 1

                # randomizes dark peice move for primative AI
                if possible_moves > 0:
                    picked_space = False
                    while picked_space == False:
                        rand_index = randint(1, 24)
                        rand_move = randint(0, 3)

                        spot_check = board[rand_index - moves[rand_move]] < 2 and board[rand_index] < 0 and rand_index - \
                                     moves[rand_move] > 1
                        check = 0

                        # while moves[rand_move] == 0 and spot_check == False and  and rand_index-rand_move< 1:
                        while moves[rand_move] == 0 or spot_check == False:
                            rand_move = randint(0, 3)
                            rand_index = randint(1, 24)
                            # spot_check =board[rand_index]<0 and board[rand_index - moves[rand_move]]<2
                            spot_check = board[rand_index - moves[rand_move]] < 2 and board[
                                rand_index] < 0 and rand_index - moves[rand_move] > 1
                            print ("check: " + str(check))
                            check = check + 1

                        # if board[rand_index]<0 and board[rand_index - moves[rand_move]]<2:
                        picked_space = True
                        move = moves[rand_move]
                        moves[rand_move] = 0

            print(possible_moves)

            if possible_moves > 0:

                while (move_valid == False and turn == 1):
                    # print(moves)
                    move = int(input("Which move would you like to take? "))
                    for i in range(0, 4):
                        if (moves[i] == move):
                            moves[i] = 0
                            move_valid = True
                            break
                    if (move_valid == False):
                        print("Move invalid, please try again")

                movePiece(move, turn, rand_index)
            else:
                print("No possible moves, turn over")


    # player movement and verification
    def movePiece(move, turn):
        print(board)

        if (turn == 1):

            if center_bar[0] > 0:
                origin_index = 0
            else:
                origin_index = int(input("What space would you like to move from? "))

                # origin validity check

            while (board[origin_index] < 1):
                print('That spot does not have enough peices or is not yours.')
                origin_index = int(input("What space would you like to move from? "))

            print(origin_index)
            print('there are ' + str(board[origin_index]) + ' at index ' + str(origin_index + 1))

            destination_index = origin_index + move

            # destination validity check
            while (board[origin_index + move] < -1):
                print("Invalid move, destination is blocked")
                origin_index = int(input("What space would you like to move from? "))
                while (board[origin_index] < 1):
                    print('That spot does not have enough peices or is not yours.')
                    origin_index = int(input("What space would you like to move from? "))

                destination_index = origin_index + move

            # STILL NEED TO FILL IN LOGIC FOR HITTING PIECE
            if (board[origin_index + move] == -1):
                print("You hit a dark peice")
                board[origin_index] = board[origin_index] - 1
                board[destination_index] = 1
                board[25] = board[25] - 1
                center_bar[1] = center_bar[1] - 1
                if origin_index == 0:
                    center_bar[0] = center_bar[0] - 1
                print(board)
                print(center_bar)
            else:

                board[origin_index] = board[origin_index] - 1
                board[destination_index] = board[destination_index] + 1
                if origin_index == 0:
                    center_bar[0] = center_bar[0] - 1
                print(board)
                print(center_bar)
        elif (turn == -1):
            if center_bar[1] < 0:
                origin_index = 25
            else:
                origin_index = int(input("What space would you like to move from? "))

                # origin validity check
            while (board[origin_index] > -1):
                print('That spot does not have enough peices or is not yours.')
                origin_index = int(input("What space would you like to move from? "))

            print(origin_index)
            print('there are ' + str(board[origin_index]) + ' at index ' + str(origin_index + 1))

            destination_index = origin_index - move

            # destination validity check
            while (board[origin_index - move] > 1):
                print("Invalid move, destination is blocked")
                origin_index = int(input("What space would you like to move from? "))
                while (board[origin_index] > -1):
                    print('That spot does not have enough peices or is not yours.')
                    origin_index = int(input("What space would you like to move from? "))

                destination_index = origin_index - move

            if (board[origin_index - move] == 1):
                print("You hit a light peice")
                board[origin_index] = board[origin_index] + 1
                board[destination_index] = -1
                board[0] = board[0] + 1
                center_bar[0] = center_bar[0] + 1
                if origin_index == 25:
                    center_bar[1] = center_bar[1] + 1
                print(board)
                print(center_bar)
            else:

                board[origin_index] = board[origin_index] + 1
                board[destination_index] = board[destination_index] - 1
                if origin_index == 25:
                    center_bar[1] = center_bar[1] + 1
                print(board)
                print(center_bar)

    # Prototyping possible move check

    # player movement and verification
    def movePiece(move, turn, rand_index):
        print("Rand_index:" + str(rand_index))
        print("move:" + str(move))
        if (turn == 1):

            if center_bar[0] > 0:
                origin_index = 0
            else:
                origin_index = int(input("What space would you like to move from? "))

                # origin validity check

            while (board[origin_index] < 1):
                print('That spot does not have enough peices or is not yours.')
                origin_index = int(input("What space would you like to move from? "))

            print(origin_index)
            print('there are ' + str(board[origin_index]) + ' at index ' + str(origin_index + 1))

            destination_index = origin_index + move

            # destination validity check
            while (board[origin_index + move] < -1 or origin_index + move > 24):
                print("Invalid move, destination is blocked")
                origin_index = int(input("What space would you like to move from? "))
                while (board[origin_index] < 1):
                    print('That spot does not have enough peices or is not yours.')
                    origin_index = int(input("What space would you like to move from? "))

                destination_index = origin_index + move

            # STILL NEED TO FILL IN LOGIC FOR HITTING PIECE
            if (board[origin_index + move] == -1):
                print("You hit a dark peice")
                board[origin_index] = board[origin_index] - 1
                board[destination_index] = 1
                board[25] = board[25] - 1
                center_bar[1] = center_bar[1] - 1
                if origin_index == 0:
                    center_bar[0] = center_bar[0] - 1
                print(board)
                print(center_bar)
            else:

                board[origin_index] = board[origin_index] - 1
                board[destination_index] = board[destination_index] + 1
                if origin_index == 0:
                    center_bar[0] = center_bar[0] - 1
                print(board)
                print(center_bar)
        elif (turn == -1):

            if center_bar[1] < 0:
                origin_index = 25
            else:
                # origin_index = int(input("What space would you like to move from? ")) \
                origin_index = rand_index

            # origin validity check
            while (board[origin_index] > -1):
                print('That spot does not have enough peices or is not yours.')
                origin_index = int(input("What space would you like to move from? "))

            print(origin_index)
            print('there are ' + str(board[origin_index]) + ' at index ' + str(origin_index + 1))

            destination_index = origin_index - move

            # destination validity check
            while (board[origin_index - move] > 1 or origin_index - move < 1):
                print("Invalid move, destination is blocked")
                origin_index = int(input("What space would you like to move from? "))
                while (board[origin_index] > -1):
                    print('That spot does not have enough peices or is not yours.')
                    origin_index = int(input("What space would you like to move from? "))

                destination_index = origin_index - move

            if (board[origin_index - move] == 1):
                print("You hit a light peice")
                board[origin_index] = board[origin_index] + 1
                board[destination_index] = -1
                board[0] = board[0] + 1
                center_bar[0] = center_bar[0] + 1
                if origin_index == 25:
                    center_bar[1] = center_bar[1] + 1
                print(board)
                print(center_bar)
            else:

                board[origin_index] = board[origin_index] + 1
                board[destination_index] = board[destination_index] - 1
                if origin_index == 25:
                    center_bar[1] = center_bar[1] + 1
                print(board)
                print(center_bar)



    def build(self):
        return screen_manager

    pass



    def getUserInput(self,TextInput):
        print(TextInput.text)

    def changeLabelText(self, Label, newLabel):
        Label.text = newLabel


app = Backgammon()
app.run()