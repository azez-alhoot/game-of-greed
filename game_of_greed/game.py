from game_of_greed import GameLogic, Banker
import sys
class Game:

    def __init__(self, roller=None):
        self.roller= roller

    @staticmethod
    def print_roll(roll):
        roll_as_string = [str(i) for i in roll]
        to_be_printed = ','.join(roll_as_string)
        # print(to_be_printed)
        return to_be_printed
        # print(','.join([str(i) for i in roll]))


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
            # Because Flo use mock roller
            roll = self.roller(num_dice)
            print(Game.print_roll(roll))
            # In case we don't use Flo
            # roll = GameLogic.roll_dice(num_dice)
            self.print_roll(roll)
            # count =1
            while 0 < round <= 6:
                what_next = input("Enter dice to keep (no spaces), or (q)uit: ")
                if what_next == 'q' or what_next == 'quit':
                    print(f"Total score is {score} points")
                    print(f"Thanks for playing. You earned {score} points")
                    break
                else:
                    inpt = Game.convert_to_tup(what_next)
                    score += GameLogic.calculte_score(inpt)
                    num_dice -= len(what_next)
                    print(f"You have {score} unbanked points and {num_dice} dice remaining")
                    inpt = input("(r)oll again, (b)ank your points or (q)uit ")

                    if what_next == 'q' or what_next =='quit':
                        break

                    if what_next == 'r' or 'roll':
                        print('******************************')
                        new_roll = GameLogic.role_dice(num_dice)
                        print(f"Rolling {num_dice} dice...")
                        rol3 = Game.print_roll(new_roll)
                        num_dice -= len(what_next)
                        print(rol3)
                        round+=1

                    if what_next == 'b' or 'bank':
                        print(f"You banked {score} points in round {round}")
                        print(f"Total score is {score} points")
                        print(f"Starting round {round}")
                        x.shelf(score)
                        x.bank()
                        new_numbers = GameLogic.role_dice(6)
                        rol3 = Game.print_roll(new_numbers)
                        print(rol3)
                        round +=1
                        # print(x.total)
                # round+=1
            print(f"Total score is {x.total} points")
            print(f"Thanks for playing. You earned {x.total} points")
            

if __name__=='__main__':
    game = Game(GameLogic.role_dice)
    # game = Game()
    game.play()
    # game.convert_to_tup("111")