from tests.flow.flo import Flo
from game_of_greed.game_of_greed import GameLogic, Banker


def test_quitter():
    Flo.test("tests/flow/quitter.txt")
    
def test_wanna_play_then_quit():
    Flo.test("tests/flow/do_wanna_play_then_quit.txt")