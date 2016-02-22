# -*- coding:utf-8 -*-
f = open( "words.txt" )
words = []
for word in f.readline().strip().split( "," ):
    words.append( word.strip( "\"" ) )
f.close()

letters = {}
for i, c in enumerate( "ABCDEFGHIJKLMNOPQRSTUVWXYZ" ):
    letters[ c ] = i + 1

max_len = letters[ "Z" ] * len( max( words, key = len ))
triangle = 0
triangles = []
for i in range( 1, max_len + 1 ):
    triangle += i
    triangles.append( triangle )
    
triangle_words = []
for word in words:
    word_sum = 0
    for c in word:
        word_sum += letters[ c ]
    if word_sum in triangles:
        triangle_words.append( word )
        
print( len( triangle_words ) )