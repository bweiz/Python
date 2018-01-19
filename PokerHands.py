#-------------------------------------------------------------
# Benton Weizenegger
# 10/3/17
# Lab Section 2
# Program 2
#-------------------------------------------------------------
def evaluate(hand, poker_output):
    if Flush(hand):
        return "Flush"
    elif Three_of_a_Kind(hand):
        return "Three of a kind" 
    elif Two_of_a_Kind(hand):
        return "Two of a Kind"
    elif Nothing(hand):
        return "Nothing"

def Flush(hand):
    if hand[0][1] == hand[1][1] == hand[2][1]:
        return True
def Three_of_a_Kind(hand):
    if hand[0][0] == hand[1][0] == hand[2][0]:
        return True
def Two_of_a_Kind(hand):
    if hand[0][0] == hand[1][0] or hand[0][0] == hand[2][0] or hand[1][0] == hand[2][0]:
        return True
def Nothing(hand):
    if not hand[0][1] == hand[1][1] == hand[2][1]:
        return True
    if not hand[0][0] == hand[1][0] == hand[2][0]:    
        return True
    if not hand[0][0] == hand[1][0] or hand[0][0] == hand[2][0] or hand[1][0] == hand[2][0]:
        return True

def print_hand(hand_as_list, poker_output):
    
        cardnum = 1                                     # Number to print in output function
        poker_output.write("Poker Hand \n" + "---------- \n")
        for hand in hand_as_list:                       
            poker_output.write("Card " + str(cardnum) + ": " + hand[0] + " of " + hand[1] + "\n")
            hand = hand_as_list[0][0:], hand_as_list[1][0:], hand_as_list[2][0:]
            cardnum += 1
        poker_output.write("\n")    
        poker_output.write("Poker hand Evaluation: " + str(evaluate(hand, poker_output)) + "\n")   
        poker_output.write("\n")
   
# --------------------------------------
# Do not change anything below this line
# --------------------------------------

def main(poker_input, poker_output, cards_in_hand):    

    for hand in poker_input:
        hand = hand.split()
        hand_as_list = []
        for i in range(cards_in_hand):
            hand_as_list.append([hand[0], hand[1]])
            hand = hand[2:]
        print_hand(hand_as_list, poker_output)
        evaluate(hand_as_list, poker_output)

# --------------------------------------

poker_input = open("poker.in", "r")
poker_output = open("poker.out", "w")

main(poker_input, poker_output, 3)

poker_input.close()
poker_output.close()
