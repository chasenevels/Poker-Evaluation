from poker_eval import *
from pokerdeck import *

def test_deal_hand():
    assert(len(deal_hand()) == 5)
	
def test_pairs():
	ranks = ['4', '5', '8', '6', '7']
	assert find_pairs(ranks) == 0
	ranks = ['4', '5', '5', '6', '7']
	assert find_pairs(ranks) == 1
	ranks = ['4', '5', '5', '6', '6']
	assert find_pairs(ranks) == 2
	
def test_three_of_a_kind():
	ranks = ['4', '5', '5', '5', '6']
	assert three_of_a_kind(ranks) == 1
	
def test_four_of_a_kind():
	ranks = ['4', '4', '4', '4', '5']
	assert four_of_a_kind(ranks) == 1

def test_straight():
	ranks = ['4', '5', '6', '7', '8']
	assert straight(ranks) == 1
	
def test_flush():
	hand = [Card('4','♣'), Card('5','♣'), Card('9','♣'), Card('7','♣'), Card('10','♣')]
	assert flush(hand) == 1

def test_full_house():
	hand = [Card('4', '♣'), Card('4', '♠'), Card('4', '♦'), Card('7', '♣'), Card('7', '♥')]
	rank_list = get_ranks(hand)
	assert full_house(rank_list) == 1

def test_straight_flush():
	hand = [Card('4', '♣'), Card('5', '♣'), Card('6', '♣'), Card('7', '♣'), Card('8', '♣')]
	rank_list = get_ranks(hand)
	assert straight_flush(hand, rank_list)