# -*- coding:utf-8 -*-
def d( number ):
    sum = 1
    if number % 2 == 0:
        step = 1
    else:
        step = 2
        
    for i in range( 2 + step // 2, number // 2 + 1, step ):
        if number % i == 0:
            sum += i
    
    if number == sum or number == 0:
        return False
    return sum

amicables = []    
for i in range( 10000 ):
    if i in amicables:
        continue
    divsum = d( i )
    
    if divsum:
        if d( divsum ) == i:
            amicables.append( i )
            amicables.append( divsum )

print( sum( amicables ) )