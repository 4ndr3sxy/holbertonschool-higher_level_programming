#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    score = 0
    score_key = ""
    for key, value in a_dictionary.items():
        if value > score:
            score_key = key or None
            score = value
    return score_key
