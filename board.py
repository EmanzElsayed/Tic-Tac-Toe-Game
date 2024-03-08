class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1 , 10)]


    def display_board(self):
        for i in range(0 , 9 , 3):
            print("|".join(self.board[i : i + 3]))
            if i < 6 :
                print('-'*5)

    def update_board(self , choice , symbol):
        if self.validate_move(choice):
            self.board[choice - 1] = symbol
            return True
        else:
            return False

    def reset_board(self):
        self.board = [i for i in range(0 , 10)]

    def validate_move(self , choice):
        return self.board[choice - 1].isdigit()


    

