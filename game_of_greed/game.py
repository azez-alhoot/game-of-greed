from game_of_greed.game_of_greed import GameLogic, Banker
# from game_of_greed import GameLogic, Banker

import sys
class Game:

    def __init__(self, roller=None):
        self.roller= roller or GameLogic.role_dice

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


    def play(self):
        round = 1
        num_dice = 6
        score = 0
        x = Banker()

        print("Welcome to Game of Greed")
        response = input("Wanna play?")
        if response == 'n':
            print("OK. Maybe another time")
        elif response == 'y':
            print(f"Starting round {round}")
            print(f"Rolling {num_dice} dice...")
            roll = self.roller(num_dice)
            print(Game.print_roll(roll))
            self.print_roll(roll)

            while 0 < round <= 6:
                
                what_next = input("Enter dice to keep (no spaces), or (q)uit: ")
                if what_next == 'q' or what_next == 'quit':
                    
                    break
                else:
                    generate_new_tupe = Game.convert_to_tup(what_next)
                    score += GameLogic.calculte_score(generate_new_tupe)
                    num_dice = 6-len(generate_new_tupe)
                    print(f"You have {score} unbanked points and {num_dice} dice remaining")
                    inpt = input("(r)oll again, (b)ank your points or (q)uit ")
                    
                    if inpt == 'q' or inpt =='quit':
                        break

                    if inpt == 'r' or inpt =='roll':
                        # new_roll = GameLogic.role_dice(num_dice)
                        new_roll = self.roller(num_dice)
                        print(f"Rolling {num_dice} dice...")
                        rol3 = Game.print_roll(new_roll)
                        num_dice = 6-len(generate_new_tupe)
                        print(rol3)

                    if inpt == 'b' or inpt == 'bank':
                        x.shelf(score)
                        x.bank()
                        print(f"You banked {score} points in round {round}")
                        print(f"Total score is {x.total} points")
                        round +=1
                        print(f"Starting round {round}")
                        print("Rolling 6 dice...")
                        # new_numbers = GameLogic.role_dice(6)
                        new_numbers = self.roller(6)
                        rol3 = Game.print_roll(new_numbers)
                        print(rol3)
                        score = 0

            print(f"Total score is {x.total} points")
            print(f"Thanks for playing. You earned {x.total} points")
            

if __name__=='__main__':
    game = Game()
    game.play()