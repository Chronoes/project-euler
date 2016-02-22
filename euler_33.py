# -*- coding:utf-8 -*-
numbers = []
numerator, denominator = 1, 1
for n in range( 12, 100 ):
    if n % 10 == 0:
        continue

    for m in range( 11, 100 ):
        if m % 10 == 0:
            continue
            
        number = m / n
        
        m_str = str( m )
        n_str = str( n )
        # print( m, n )
        if number >= 1 or m_str == "".join( reversed( n_str )):
            break
        for m1 in m_str:
            for n1 in n_str:
                if m1 == n1:
                    mpos = m_str.find( m1 )
                    npos = n_str.find( n1 )        
                    m_str = m_str[ mpos - 1]
                    n_str = n_str[ npos - 1]
                    break
        if m_str != str( m ):
            # print( m_str, n_str )
            testnumber = int( m_str ) / int( n_str )
            if number == testnumber:
                numerator *= int( m_str )
                denominator *= int( n_str )
                numbers.append( ( int( m_str ), int( n_str ), testnumber ) )