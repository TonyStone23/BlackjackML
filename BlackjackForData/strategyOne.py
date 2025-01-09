import hand as h
from deck import *

def StrategyOne(safePercentage):
    cleanDeck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
    'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
    'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
    'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
    #dealer and player

    pSI = h.Hand()
    pSI_wins = 0
    pSI_wins_out = []
    pSI_earnings = []
    pSI_bets = []
    pSI_numCards = []
    round_count = []
    pSI_startBalance = 100
    pSI.setBalance(pSI_startBalance)

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
        pSI_score = 0
        pSI.addCard(deck)
        pSI.addCard(deck)

        d_score = 0
        d.addCard(deck)
        d.addCard(deck)

        #game-playing
        bet = .4 * pSI.getBalance()
        pSI_bets.append(bet)
        pSI_score = pSI.getHand()
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
                pSI.addCard(deck)
                pSI_score = pSI.getHand()
            else: 
                stand = True
        pSI_numCards = pSI.handSize()

        d_score = d.getHand()
        while d_score < d_stand:
            d.addCard(deck)
            d_score = d.getHand()

        pSI_currBal = pSI.getBalance()
        if pSI_score < 22 and pSI_score > d_score: #player wins
            pSI_wins += 1
            pSI_wins_out.append(1)
            d_wins_out.append(0)
            pSI.moneyChange(bet)
            d.moneyChange(bet * -1)
        elif d_score < 22 and d_score > pSI_score: #dealerwins
            d_wins += 1
            pSI_wins_out.append(0)
            d_wins_out.append(1)
            pSI.moneyChange(bet * -1)
            d.moneyChange(bet)
        else: #both bust or tie
            ties +=1
            pSI_wins_out.append(0)
            d_wins_out.append(0)
        
        pSI_earnings.append(pSI.getBalance() - pSI_currBal)
        pSI.clearHand()
        d.clearHand()

    data = {
        'Round': round_count,
        'Player Wins': pSI_wins_out, 
        'Hand size': pSI_numCards,
        'Dealer Wins': d_wins_out, 
        'Stake': pSI_bets,
        'Round Earnings' :pSI_earnings
        }
    return data

print(StrategyOne(.50))