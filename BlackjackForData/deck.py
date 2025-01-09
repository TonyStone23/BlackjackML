import random as r
import numpy as np

def shuffle(adeck):
    """takes a deck and returns the cards in a randomized order"""
    deck_sh = r.sample(adeck, len(adeck))
    return deck_sh

def drawCard(deck_sh):
    """takes the last card off of the stack"""
    card = deck_sh.pop()
    return card

def handValue(ahand):
    """Determines the value of the hand to inform the next decision
        There are extra considerations for an ace"""
    aceCount = 0
    for i in range(len(ahand)):
        if ahand[i] == 'A':
            aceCount += 1
    while 'A' in ahand:
        ahand.remove('A')
    score = np.sum(ahand)
    for ii in range(aceCount):
        ahand.append('A')
    while aceCount > 0:
        if (score + 11) > 21:
            score = score + 1
        else:
            score = score + 11
        aceCount -= 1
    return score
