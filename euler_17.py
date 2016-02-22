# -*- coding:utf-8 -*-

d = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen", "14": "fourteen",
    "15": "fifteen", "16": "sixteen", "17": "seventeen", "18": "eighteen", "19": "nineteen", "20": "twenty", "30": "thirty", "40": "forty", "50": "fifty", "60": "sixty", "70": "seventy", "80": "eighty",
    "90": "ninety", "00": "hundred", "000": "thousand"}


def calc(i):
    if len(i) == 1 or len(i) == 2 and i[0] == '1':
        return d[i]
    elif len(i) == 2:
        if i[0] == '0':
            return calc(i[1])
        elif i[1] == '0':
            return d[i[0]+'0']
        return d[i[0]+'0'] + calc(i[1])
    elif len(i) == 3:
        if i[1:] == '00':
            return calc(i[0]) + d['00']
        return calc(i[0]) + d['00'] + 'and' + calc(i[1:])
    elif len(i) == 4:
        if i[1:] == '000':
            return calc(i[0]) + d['000']
        return calc(i[0]) + d['000'] + calc(i[1:])


sum = 0

for i in range( 1, 1001 ):
    sum += len(calc(str(i)))

print(sum)