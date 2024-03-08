from board import Board
from menu import Menu
from player import Player
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


class Game:
    def __init__(self):
        self.board = Board()
        self.menu = Menu()
        self.player = [Player() , Player()]
        self.current_player_index = 0

    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == '1':
            self.setup_player()
            self.play_game()
        else:
            self.quit_game()

    def setup_player(self):
        for index , player in enumerate(self.player , start=1):
            print(f'player {index}, Enter Your details')
            player.choose_name()
            player.choose_symbol()
            clear_screen()


    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                choice = self.menu.display_engame_menu()
                if choice == '1':
                    self.restart_game()
                else:
                    self.quit_game()
                    break
    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()
        
    def quit_game(self):
        print('Thanks For playing')
   
    def play_turn(self):
       while True:
        player = self.player[self.current_player_index]
        self.board.display_board()
        print(f'player {player.name}\'s turn with symbol {player.symbol}' )
        try:
            choice_cell = int(input('Choose a Cell [1:9]'))
            if 1 <= choice_cell <= 9 and self.board.update_board(choice_cell , player.symbol):
                break
            else:
                print("Invalid Move , Try again")
        except ValueError:
         print('please Enter a number in (1 : 9)') 
       self.switch_player()

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index 

    def check_win(self) :
        combination = [
            [0 , 1 , 2] , [3 , 4 , 5] , [6 , 7 , 8]
            , [0 , 3 , 6] , [1 , 4 , 7] , [2  ,5  , 8] , 
            [0 , 4 , 8], [2 , 4 , 6] 
        ] 
        for combo in combination:
            if self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]:
              self.board.display_board()
              print(f"{self.player[1- self.current_player_index].name} Win!")
              return True
        return False
    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)

game = Game()
game.start_game()


        