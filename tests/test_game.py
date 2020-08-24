from tests.flow.flo import Flo
# from game_of_greed.game_of_greed import GameLogic, Banker


def test_quitter():
    Flo.test("flow/quitter.txt")
    
def test_wanna_play_then_quit():
    Flo.test("flow/do_wanna_play_then_quit.txt")

# def test_bank_first():
#     Flo.test("flow/bank_one_roll_then_quit.txt")

def test_bank_roll():
    Flo.test("flow/bank_first_for_two_rounds.txt")