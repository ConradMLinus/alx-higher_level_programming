#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == {} or a_dictionary is None:
        return (None)
    else:
        best_score = list(a_dictionary.keys())[0]
        for key, value in a_dictionary.items():
            if value > a_dictionary[best_score]:
                best_score = key
    return (best_score)
