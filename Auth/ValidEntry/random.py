# choose a random element from a list
from random import seed
from random import choice
def generateRandom():
    sequence = [i for i in range(20)]
    # make choices from the sequence
    choices = ""
    for _ in range(5):
        selection = choice(sequence)
        choices += str(selection)
    return choices