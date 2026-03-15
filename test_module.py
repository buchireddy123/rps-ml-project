from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player

def test():
    bots = [quincy, abbey, kris, mrugesh]

    for bot in bots:
        win_rate = play(player, bot, 1000)
        assert win_rate >= 60, "Failed against bot"

    print("All tests passed!")

if __name__ == "__main__":
    test()
