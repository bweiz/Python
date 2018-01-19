import random
import numpy as np
import matplotlib.pyplot as mp


class Deck:
    def __init__(self):
        self.cards = []
        
    
    def Deck(self):
        d = []
        for s in range(4):
            for value in range(1, 14):
                d.append(value)
        d = [x if (x != 12 and x != 13) else 10 for x in d]
        
        random.shuffle(d)
        print(d)
        return d
        
                
    
    
def generateHands(a):
    hands = np.ndarray(a, dtype=int)
    deck = Deck()
    builtDeck = deck.Deck()
    

    for x in range(a):
        y = random.randint(0, 51)
        z = random.randint(0, 51)
        if y!= z:
            
        
            card1 = builtDeck[y]
            card2 = builtDeck[z]
            if card1 == 11 and card2 == 11:
                card2 = 1
            handSum = card1 + card2
            hands[x] = handSum
            
    print(hands)
    return hands
        
        
    
def main():
    hands = generateHands(100000)
    
    mp.hist(hands, bins = np.arange(4, 23), facecolor = 'g', align = 'left', density = True)
    mp.xticks(np.arange(4, 22))  
        
    mp.title("Histogram of Blackjack Hands")
    mp.xlabel("Hand Value")
    mp.ylabel("Probability")
    mp.grid(True)
    mp.show()
        
main()



