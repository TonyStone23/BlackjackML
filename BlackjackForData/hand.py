import pandas as pd
import numpy as np
from deck import *

class Hand:
    def __init__(self):
        """initializes hand with a balance"""
        self.hand = []

    def setBalance(self, balance):
        """sets the balance, used in determining earnings"""
        self.balance = balance
    
    def moneyChange(self, change):
        """changes balance based off of the outcome of a hand"""
        self.balance = self.balance + change

    def getBalance(self):
        """returns balance"""
        return self.balance

    def addCard(self, deck):
        """a hit"""
        self.hand.append(drawCard(deck))

    def getHand(self): #this might be able to be done in one function within the hand
        """returns hand value"""
        return handValue(self.hand)
    
    def getCards(self):
        return self.hand
    
    def clearHand(self):
        """clears hand for the next round"""
        self.hand = []

    def handSize(self):
        return len(self.hand)