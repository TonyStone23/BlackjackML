import hand as h
from deck import *
import numpy as np

actions = {0: 'hit', 1: 'stand'}
states = (17, 17)

def state_to_ind(playerTotal, dealerTotal):
    return (playerTotal -4) * 17 + (dealerTotal - 4) * 17

def step(state, action):
    if action == 0:
        return

def StrategyOne(safePercentage):
    cleanDeck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
    'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
    'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
    'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
    #dealer and player

    q = h.Hand()
    q_wins = 0
    q_wins_out = []
    q_earnings = []
    q_bets = []
    q_numCards = []
    round_count = []
    q_startBalance = 100
    q.setBalance(q_startBalance)

    d = h.Hand()
    d_stand = 17
    d_wins = 0
    d_wins_out = []
    d_startBalance = 0
    d.setBalance(d_startBalance)

    ties = 0

    rounds = 0
    for i in range(5):
        round_count.append((rounds%5)+1)
        if rounds % 5 == 0:
            deck = shuffle(cleanDeck)
        rounds += 1

        #Cards are dealt
        q_score = 0
        q.addCard(deck)
        q.addCard(deck)

        d_score = 0
        d.addCard(deck)
        d.addCard(deck)

        #game-playing
        bet = .4 * q.getBalance()
        q_bets.append(bet)
        pSI_score = q.getHand()
        stand = False
        while not stand:
            safe = 0
            copyDeck = deck.copy()
            for i in range(0, len(copyDeck)):
                if copyDeck[i] == 'A':
                    potentialCard = 1
                else: 
                    potentialCard = copyDeck[i]
                if (pSI_score + potentialCard) <= 21:
                    safe += 1
            safeChance = safe/len(deck)
            if safeChance > safePercentage:
                q.addCard(deck)
                pSI_score = q.getHand()
            else: 
                stand = True
        pSI_numCards = q.handSize()

        d_score = d.getHand()
        while d_score < d_stand:
            d.addCard(deck)
            d_score = d.getHand()

        pSI_currBal = q.getBalance()
        if pSI_score < 22 and pSI_score > d_score: #player wins
            pSI_wins += 1
            q_wins_out.append(1)
            d_wins_out.append(0)
            q.moneyChange(bet)
            d.moneyChange(bet * -1)
        elif d_score < 22 and d_score > pSI_score: #dealerwins
            d_wins += 1
            q_wins_out.append(0)
            d_wins_out.append(1)
            q.moneyChange(bet * -1)
            d.moneyChange(bet)
        else: #both bust or tie
            ties +=1
            q_wins_out.append(0)
            d_wins_out.append(0)
        
        q_earnings.append(q.getBalance() - pSI_currBal)
        q.clearHand()
        d.clearHand()

    data = {
        'Round': round_count,
        'Player Wins': q_wins_out, 
        'Hand size': pSI_numCards,
        'Dealer Wins': d_wins_out, 
        'Stake': q_bets,
        'Round Earnings' :q_earnings
        }
    return data

print(StrategyOne(.50))