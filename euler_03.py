# -*- coding:utf-8 -*-
jagaja = 3
algarvud = [ 2 ]
arv = 600851475143
while jagaja <= arv:
    on_algarv = True
    for algarv in algarvud:
        if jagaja % algarv == 0:
            on_algarv = False
            break
            
    if on_algarv:
        algarvud.append( jagaja )
        
    if arv % jagaja == 0:
        arv /= jagaja
        
    jagaja += 1
print( algarvud[ -1 ] ) 