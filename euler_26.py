# -*- coding:utf-8 -*-
count = 0
for d in range( 2, 10 ):
    f = str( 1 / d )[ 2: ]
    recur = f[ 0 ]
    if len( f ) > 1:
        for i in range( 1, len( f ) ):
            if f[ i:i + len( recur ) ] == recur: break
            recur += f[ i ]
        
    if len( recur ) > count: 
        print( len( recur ), d, f )
        count = len( recur )