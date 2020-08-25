# from game_of_greed.game_of_greed import GameLogic, Banker
from game_of_greed import GameLogic, Banker
#for python

import sys
class Game:
    status = False
    status_quit = False
    num_dice = 6
    def __init__(self, roller=None):
        self.roller= roller or GameLogic.role_dice
        self.round=1
        self.score=0


    @staticmethod
    def print_roll(roll):
        roll_as_string = [str(i) for i in roll]
        to_be_printed = ','.join(roll_as_string)
        
        return to_be_printed


    @staticmethod
    def convert_to_tup(str_val):
        new_str = [int(i) for i in str_val]
        new_tup= tuple(new_str)
        return new_tup

# ______________________________________________
    def zilch_method(self):
        Game.num_dice = 6
        print("Zilch!!! Round over")
        print(f"You banked 0 points in round {self.round}")
        print(f"Total score is {self.score} points")
        x = Banker()
        x.clear_shelf()
        self.round+=1
        print(f'Starting round {self.round}')
        print(f'Rolling {Game.num_dice} dice...')
        


    @staticmethod
    def check_cheat(tup,npt):
        # print(Game.status)
        while not Game.status:
            elem =[]
            for i in npt:
                if tup.count(i) >= npt.count(i):
                    elem.append(i)
            if len(elem) != len(npt):
                print('Cheater!!! Or possibly made a typo...')
                print(Game.print_roll(tup))
                what_next = input('Enter dice to keep (no spaces), or (q)uit: ')
                npt = Game.convert_to_tup(what_next)
                if npt == 'q' or npt == 'quit':
                    print('Thanks for playing. You earned 0 points')
                    sys.exit()
            else:
                Game.status = True
                Game.status_quit = True
        return npt
        
        


    def play(self):
        # round = 1
        Game.status_quit = False
        Game.num_dice = 6
        # score = 0
        x = Banker()
        # self.zilch_method()
        print("Welcome to Game of Greed")
        response = input("Wanna play?")
        if response == 'n':
            print("OK. Maybe another time")
        elif response == 'y':
            print(f"Starting round {self.round}")
            print(f"Rolling {Game.num_dice} dice...")
            roll = self.roller(Game.num_dice)
            print(Game.print_roll(roll))
            self.print_roll(roll)
            
            

            while True:
                Game.status = False
                Game.status_quit = False

                what_next = input("Enter dice to keep (no spaces), or (q)uit: ")

                if what_next == 'q' or what_next == 'quit':
                    # Game.status_quit = True
                    break
                else:
                    generate_new_tupe = Game.convert_to_tup(what_next)
                    Game.status = False
                    Game.status_quit = False
                    generate_new_tupe =Game.check_cheat(roll,generate_new_tupe)

                    self.score += GameLogic.calculte_score(generate_new_tupe)
                    if GameLogic.calculte_score(generate_new_tupe) == 0:
                        print('+'*50)
                        self.zilch_method()
                        print(Game.print_roll(self.roller(6)))
                    else:
                        Game.num_dice -=len(generate_new_tupe)

                    
                    print(f"You have {self.score} unbanked points and {Game.num_dice} dice remaining")
                
                    inpt = input("(r)oll again, (b)ank your points or (q)uit ")
                    
                    if inpt == 'q' or inpt =='quit':
                        # Game.status_quit = True
                        break
                    


                    if GameLogic.calculte_score(generate_new_tupe) == 0:
                        print('+'*50)
                        self.zilch_method()
                        print(Game.print_roll(self.roller(6)))

                        
                    if inpt == 'r' or inpt =='roll':
                        new_roll = self.roller(Game.num_dice)
                        new = self.convert_to_tup(new_roll)
                        print(f"Rolling {Game.num_dice} dice...")
                        rol3 = Game.print_roll(new_roll)
                        # Game.num_dice -=len(new)
                        print(rol3)
                        if GameLogic.calculte_score(new) == 0: # if its true y
                            print('_'*50)
                            self.zilch_method()
                            print(Game.print_roll(self.roller(6)))


                    if inpt == 'b' or inpt == 'bank':
                        x.shelf(self.score)
                        x.bank()
                        Game.status= False
                        Game.num_dice = 6
                        print(f"You banked {self.score} points in round {self.round}")
                        print(f"Total score is {x.total} points")
                        self.round +=1
                        print(f"Starting round {self.round}")
                        print("Rolling 6 dice...")
                        # new_numbers = GameLogic.role_dice(6)
                        roll = self.roller(6)
                        rol3 = Game.print_roll(roll)
                        print(rol3)
                        self.score = 0
            if not Game.status_quit:
                # print(Game.status_quit)
                print(f"Total score is {x.total} points")
                print(f"Thanks for playing. You earned {x.total} points")
            else:
                print("Thanks for playing. You earned 0 points")
            

if __name__=='__main__':
    game = Game()
    game.play()