from poker_eval import *
from pokerdeck import *

def test_deal_hand():
    assert(len(deal_hand()) == 5)
    
