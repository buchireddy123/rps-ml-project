import random

def play(player1, player2, num_games, verbose=False):
    p1_prev_play = ""
    p2_prev_play = ""

    p1_score = 0
    p2_score = 0
    tie = 0

    for i in range(num_games):

        p1_play = player1(p2_prev_play)
        p2_play = player2(p1_prev_play)

        if p1_play == p2_play:
            tie += 1
            winner = "Tie"
        elif (p1_play == "R" and p2_play == "S") or \
             (p1_play == "P" and p2_play == "R") or \
             (p1_play == "S" and p2_play == "P"):
            p1_score += 1
            winner = "Player 1"
        else:
            p2_score += 1
            winner = "Player 2"

        if verbose:
            print(i, p1_play, p2_play, winner)

        p1_prev_play = p1_play
        p2_prev_play = p2_play

    print("Final Results:")
    print("Player 1:", p1_score)
    print("Player 2:", p2_score)
    print("Ties:", tie)

    return (p1_score / num_games) * 100


# BOT 1
def quincy(prev_play, history=[]):
    if prev_play != "":
        history.append(prev_play)
    choices = ["R", "R", "P", "P", "S"]
    return random.choice(choices)

# BOT 2
def abbey(prev_play, history=[]):
    if prev_play != "":
        history.append(prev_play)
    if len(history) < 2:
        return "R"
    if history[-1] == history[-2]:
        return history[-1]
    return random.choice(["R","P","S"])

# BOT 3
def kris(prev_play):
    return random.choice(["R","P","S"])

# BOT 4
def mrugesh(prev_play, history=[]):
    if prev_play != "":
        history.append(prev_play)

    if len(history) < 10:
        return random.choice(["R","P","S"])

    most_common = max(set(history), key=history.count)

    counter = {"R":"P","P":"S","S":"R"}

    return counter[most_common]
