import hand as h
from deck import *
import numpy as np
import random as r
import pandas as pd

cleanDeck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def state_to_ind(playerTotal, dealerTotal):
    return (playerTotal -3) * 18 + (dealerTotal - 3)

def step(player, dealer, action, state, deck):
    ps = player.getHand()
    ds = dealer.getHand()

    if action == 0:
        player.addCard(deck)
        ps = player.getHand()
        if ps > 21:
            return state, -10, True
        return state, 10, False

    if action == 1:
        ds = dealer.getHand()
        while ds < 17:
            dealer.addCard(deck)
            ds = dealer.getHand()
        if ps < 22 and ds < ps: #playerwins
            return state, 10, True
        elif ds < 22 and ps < ds: #dealerwins
            return state, -10, True
        else: #both bust or tie
            return state, -5, True
        
    return state, 0, False

#dealer and player

q = h.Hand()
d = h.Hand()

actions = [0, 1] # 0 to hit, 1 to stand
Qtable = np.zeros((8000, 2))

alpha = 0.1 #Learning rate
gamma = 0.9 #Discount factor
epsilon = 0.1 #Exploration rate

rounds = 0
for round in range(100):
    if rounds % 5 == 0:
        deck = shuffle(cleanDeck)
    rounds += 1
    #Cards are dealt
    q.addCard(deck)
    q.addCard(deck)

    d.addCard(deck)
    d.addCard(deck)

    qs, ds = q.getHand(), d.getHand()
    state = (qs, ds)

    done = False
    while not done:
        state_ind = state_to_ind(qs, ds)

        if r.uniform(0, 1) < epsilon:
            action = r.choice(actions)  #Explore
        else:
            action = np.argmax(Qtable[state_ind]) #Exploit

        nextState, reward, done = step(q, d, action, state, deck)
        next_state_ind = state_to_ind(*nextState)

        Qtable[state_ind, action] += alpha * (
            reward + gamma * np.max(Qtable[next_state_ind]) - Qtable[next_state_ind, action]
        )
        state = nextState

    print(f"Player: {q.getCards()}, Dealer: {d.getCards()}")
    q.clearHand()
    d.clearHand()

