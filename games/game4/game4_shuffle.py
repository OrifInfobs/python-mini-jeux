import random
def shuffle_list(lst):      # Shuffle a list and return the shuffled list
    shuffled_list = lst.copy()
    random.shuffle(shuffled_list)
    return shuffled_list
