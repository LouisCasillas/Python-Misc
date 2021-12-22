CARD = """---------
|top     |
|       |
|   suit   |
|       |
|     bottom|
|_______|"""
BLANK = """---------
|       |
|       |
|       |
|       |
|       |
|_______|"""

# rank: 2-14,
# 2-10 + Jack + Queen + King + Ace
# suit: 's', 'd', h', 'c'
# Spades, Diamonds, Hearts, Clubs
def create_card(*, rank, suit, visible=True):
    rank_top = rank_bottom = str(rank)

    if rank != 10:
       rank_top += " "
       rank_bottom = " " + rank_bottom
   
    prototype = CARD
    if not visible:
        prototype = BLANK

    card = []
    for line in prototype.split('\n'):
        
        card.append( line.replace('top', rank_top).replace('bottom', rank_bottom).replace('suit', suit.upper()) )

    return card

def print_cards(cards=[]):
    hand = []

    for i in range(0, len(cards[0])):
        line = ""
        for card in cards:
            line += card[i] + " "
        hand.append(line)

    for line in hand:
        print(line)

print_cards( [ create_card(rank=10, suit='h') ] )
print_cards( [ create_card(rank=2, suit='h', visible=False) ] )

print_cards( [ create_card(rank=10, suit='h'), create_card(rank=2, suit='h') ] )
