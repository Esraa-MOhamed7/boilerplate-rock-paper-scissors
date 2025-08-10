from collections import Counter

def player(prev_play, opponent_history=[], my_history=[]):
    beaters = {"R": "P", "P": "S", "S": "R"}
    prediction_score = {"R": 0, "P": 0, "S": 0}

    if prev_play:
        opponent_history.append(prev_play)

    guess = "R"
    pattern_length = 4
    if len(opponent_history) > pattern_length:
        last_pattern = "".join(opponent_history[-pattern_length:])
        possible_next_moves = []
        for i in range(len(opponent_history) - pattern_length):
            if "".join(opponent_history[i:i + pattern_length]) == last_pattern:
                possible_next_moves.append(opponent_history[i + pattern_length])
        if possible_next_moves:
            most_common_next = Counter(possible_next_moves).most_common(1)[0][0]
            guess = beaters[most_common_next]
        else:
            most_common_overall = Counter(opponent_history).most_common(1)[0][0]
            guess = beaters[most_common_overall]

    my_history.append(guess)
    return guess