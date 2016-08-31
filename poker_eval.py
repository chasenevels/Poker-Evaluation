from pokerdeck import *
from random import shuffle, choice
   
def deal_hand(deck):
    hand = []
    for _ in range(5):
        card = choice(deck)
        deck.remove(card)
        hand.append(card)
    return hand
        
def get_ranks(hand):
    rank_list = []
    for card in hand:
        if card[0] == 'J':
            rank_list.append(11)
        elif card[0] == 'Q':
            rank_list.append(12)
        elif card[0] == 'K':
            rank_list.append(13)
        elif card[0] == 'A':
            rank_list.append(14)
        else:
            rank_list.append(int(card[0]))
    return rank_list
    
def get_suits(hand):
    suit_list = []
    for card in hand:
        suit_list.append(card.suit)
    return suit_list

def find_pairs(rank_list):
    pairs = []
    for rank in rank_list:
        if rank_list.count(rank) == 2 and rank not in pairs:
            pairs.append(rank)
    return len(pairs)

def three_of_a_kind(rank_list):
    for card in rank_list:
        if rank_list.count(card) == 3:
            return 3
    return 0

def straight(rank_list):
    if (rank_list[4]) - (rank_list[0]) == 4:
        return 4
    return 0
            
def flush(hand):
    suits = get_suits(hand)
    if suits.count(suits[0]) == 5:
        return 5
    return 0 

def full_house(rank_list):
    if find_pairs(rank_list) == 2 and three_of_a_kind(rank_list):
        return 6
    return 0
        
def four_of_a_kind(rank_list):
    for card in rank_list:
        if rank_list.count(card) == 4:
            return 7
    return 0

def straight_flush(rank_list, hand):
    if straight(rank_list) and flush(hand):
        return 8
    return 0

def evaluate_hand(rank_list, hand):
    best_hand = find_pairs(rank_list)
    best_hand = 3 if three_of_a_kind(rank_list) > best_hand else best_hand
    best_hand = 4 if straight(rank_list) > best_hand else best_hand
    best_hand = 5 if flush(hand) > best_hand else best_hand
    best_hand = 6 if full_house(rank_list) > best_hand else best_hand
    best_hand = 7 if four_of_a_kind(rank_list) > best_hand else best_hand
    best_hand = 8 if straight_flush(rank_list, hand) > best_hand else best_hand
           
            
if __name__ == '__main__':
    deck = PokerDeck()
    shuffle(deck)    
    hand = deal_hand(deck)
    rank_list = get_ranks(hand)
    evaluate_hand(rank_list, hand)    
    

    
