import random


def return_num():
    choice_int = ""
    for x in range(4):
        choice_int = choice_int + random.choice(list("123456789"))
    return choice_int