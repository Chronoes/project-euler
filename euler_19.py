# -*- coding:utf-8 -*-

calendar = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
sundays = 0
weekday = 1 # 1901, 1st January, Tuesday
for year in range( 1901, 2001 ):
    for month in range( 1, 13 ):
        days = calendar[ month ] + 1
        
        if year % 4 == 0 and month == 2:
            if year % 100 == 0:
                if year % 400 == 0:
                    days = range( 1, days + 1 )
                else:
                    days = range( 1, days )
                    
            else:
                days = range( 1, days + 1 )
        else:
            days = range( 1, days )
            
        for day in days:
            if day == 1 and weekday % 7 == 6:
                sundays += 1
            weekday += 1