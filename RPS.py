import random

def player(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)

    # First few moves random
    if len(opponent_history) < 5:
        return random.choice(["R", "P", "S"])

    # Pattern detection (last 2 moves)
    last_two = "".join(opponent_history[-2:])
    patterns = {}

    for i in range(len(opponent_history) - 2):
        seq = "".join(opponent_history[i:i+2])
        next_move = opponent_history[i+2]

        if seq not in patterns:
            patterns[seq] = []

        patterns[seq].append(next_move)

    if last_two in patterns:
        prediction = max(set(patterns[last_two]),
                         key=patterns[last_two].count)
    else:
        prediction = random.choice(["R", "P", "S"])

    counter = {
        "R": "P",
        "P": "S",
        "S": "R"
    }

    return counter[prediction]
