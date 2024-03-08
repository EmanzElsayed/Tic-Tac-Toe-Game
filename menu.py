class Menu:
    def __init__(self) -> None:
        pass

    def display_main_menu(self):
        while True:
            menu_text = """
            Welcome to our X-O Game
            1. Start Game
            2. Quit Game
            Enter Your Choice (1 or 2) :  """
            choice = input(menu_text)
            if self.validate_choice(choice):
                return choice
            print('Invalid Input Please Enter Correct Choice (1 or 2) : ')
            
    
    def display_engame_menu(self):
        while True:
            menu_text = """
            1. Start Game
            2. Quit Game
            Enter Your Choice (1 or 2) :  """
            choice = input(menu_text)
            if self.validate_choice(choice):
                return choice
            else:
                print('Invalid Input Please Enter Correct Choice (1 or 2) : ')
            
    
    def validate_choice(self,choice):
        if choice =='1' or choice == '2':
            return True
        else:
            return False 
           

   