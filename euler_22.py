# -*- coding:utf-8 -*-
f = open( "names.txt" )
names = []
for name in f.readline().strip().split( "," ):
    names.append( name.strip( "\"" ) )
f.close()

chars = {'N': 14, 'O': 15, 'L': 12, 'M': 13, 'J': 10, 'K': 11, 'H': 8, 'I': 9, 'F': 6, 'G': 7, 'D': 4, 'E': 5, 'B': 2, 'C': 3, 'A': 1, 'Z': 26, 'X': 24, 'Y': 25, 'V': 22, 'W': 23, 'T': 20, 'U': 21, 'R': 18, 'S': 19, 'P': 16, 'Q': 17}

names = sorted( names )
sum = 0
for i, name in enumerate( names, 1 ):
    name_sum = 0
    for c in name:
        name_sum += chars[ c ]
    sum += i * name_sum
print( sum )