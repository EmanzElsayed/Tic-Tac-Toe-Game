class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""
    def choose_name(self):
        while True:
            name = input('Please Enter Your name in letter Only: ')
            if name.isalpha():
                self.name = name
                break
            print('Invalid name , Please Enter letter Only')


    def choose_symbol(self):
        while True:
            symbol = input('Please Enter Your Symbol in single character: ')
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print('Invalid Symbol , Please Enter Single Letter')