# -*- coding:utf-8 -*-
jagaja = 3
algarvud = [ 2 ]
while len( algarvud ) < 10001:
    on_algarv = True
    for algarv in algarvud:
        if jagaja % algarv == 0:
            on_algarv = False
            break
            
    if on_algarv:
        algarvud.append( jagaja )
        
    jagaja += 1
print( algarvud[ -1 ] )