# -*- coding:utf-8 -*-
consecutive_values = "23456789TJQKA"
def sorting_poker( s ): return consecutive_values.find( s[ 0 ] )
    
player1, player2 = [], []
f = open( "poker.txt" )
for line in f:
    line = line.strip().split()
    values, suits = "", ""
    for card in sorted( line[ :5 ], key = sorting_poker ):
        values += card[ :1 ]
        suits += card[ 1:2 ]
    player1.append(( values, suits ))
    
    values, suits = "", ""
    for card in sorted( line[ 5:10 ], key = sorting_poker ):
        values += card[ :1 ]
        suits += card[ 1:2 ]
    player2.append(( values, suits ))

f.close()

poker_decks = [ "Royal Flush", "Straight Flush", "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind", "Two Pairs", "One Pair" ]
def define_type( deck ):
    values, suits = deck
    same_suit = suits.count( suits[0] ) == 5
    consecutive = values in consecutive_values
    d_amount = {}
    for value in values:
        if value not in d_amount:   d_amount[ value ] = values.count( value )
        
    amount_values = list( d_amount.values() )
    amount = max( amount_values )
    
    deck_type, deck_value, remaining = 0, 0, 0
    for c in d_amount:
        card_value = consecutive_values.find( c )
        if d_amount[ c ] == amount  :   deck_value += card_value
        else                        :   remaining += card_value
            
    if same_suit and "TJQKA" == values      :   pass
    elif same_suit and consecutive          :   deck_type = 1   
    elif amount == 4                        :   deck_type = 2
    elif amount == 3 and 2 in amount_values :   deck_type = 3
    elif same_suit                          :   deck_type = 4
    elif consecutive                        :   deck_type = 5 
    elif amount == 3                        :   deck_type = 6
    elif amount_values.count( 2 ) == 2      :   deck_type = 7
    elif amount == 2                        :   deck_type = 8
    else                                    :   deck_type = 9 + "".join( reversed( consecutive_values )).find( values[-1] )
    
    return deck_type, deck_value, remaining

    
count = 0
for i, deck1 in enumerate( player1 ):
    deck2 = player2[ i ]
    deck1_type, deck1_value, deck1_remaining = define_type( deck1 )
    deck2_type, deck2_value, deck2_remaining = define_type( deck2 )
    if deck1_type == deck2_type: 
        if deck1_value == deck2_value and deck1_remaining > deck2_remaining :   count += 1
        elif deck1_value > deck2_value                                      :   count += 1
            
    elif deck1_type < deck2_type: count += 1
        