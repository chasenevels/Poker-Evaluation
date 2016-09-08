from poker_eval import *
from pokerdeck import *

def test_deal_hand():
    assert(len(deal_hand()) == 5)
	
def test_pairs():
	pair_hand = [Card(rank='4', suit='♣'), Card(rank='5', suit='♠'), Card(rank='5', suit='♦'), Card(rank='6', suit='♥'), Card(rank='7', suit='♥')
	two_pair_hand = [Card(rank='4', suit='♣'), Card(rank='5', suit='♠'), Card(rank='5', suit='♦'), Card(rank='6', suit='♥'), Card(rank='6', suit='♦')
    ranks = ['4', '5', '8', '6', '7']
	assert find_pairs(ranks) == 0
	ranks = ['4', '5', '5', '6', '7']
	assert find_pairs(ranks) == 1
	ranks = ['4', '5', '5', '6', '6']
	assert find_pairs(ranks) == 2
	
def test_three_of_a_kind():
	hand = [Card(rank='4', suit='♣'), Card(rank='4', suit='♠'), Card(rank='4', suit='♦'), Card(rank='6', suit='♥'), Card(rank='7', suit='♥')
	assert three_of_a_kind(hand) == 1
	
def test_four_of_a_kind():
	hand = [Card(rank='4', suit='♣'), Card(rank='4', suit='♠'), Card(rank='4', suit='♦'), Card(rank='4', suit='♥'), Card(rank='7', suit='♥')
	assert four_of_a_kind(hand) == 1

def test_straight():
	hand = [Card(rank='4', suit='♣'), Card(rank='5', suit='♣'), Card(rank='6', suit='♣'), Card(rank='7', suit='♣'), Card(rank='8', suit='♣')
	assert straight(hand) == 1
	
def test_flush():
	hand = [Card(rank='4', suit='♣'), Card(rank='9', suit='♣'), Card(rank='6', suit='♣'), Card(rank='2', suit='♣'), Card(rank='8', suit='♣')
	assert flush(hand) == 1

def test_full_house():
	hand = [Card(rank='4', suit='♣'), Card(rank='4', suit='♠'), Card(rank='4', suit='♦'), Card(rank='7', suit='♣'), Card(rank='7', suit='♥')
	assert full_house(hand) == 1

def test_straight_flush():
	hand = [Card(rank='4', suit='♣'), Card(rank='5', suit='♣'), Card(rank='6', suit='♣'), Card(rank='7', suit='♣'), Card(rank='8', suit='♣')
	assert straight_flush(hand) == 1