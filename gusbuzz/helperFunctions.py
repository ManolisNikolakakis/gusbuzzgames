def increase_score(score, high_score):
    score = score + 10
    if score > high_score:
        high_score = score
    return score, high_score

def decrease_score(score):
    score = score - 10
    return score

def set_score_to_zero(score):
    score = 0;
    return score