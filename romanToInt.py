# Given a roman numeral, convert it to an integer. 
# Input is guaranteed to be within the range from 1 to 3999.

# roman numerals are represented by seven different symbols:
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# Roman numerals are usually written largest to smallest from left to right. 
# However, there are six instances where subtraction is used instead:
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.

# faster than 96.52% less memory used than 6.45%
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    romDict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    subDict = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900 }
    num, i, lenIdx = 0, 0, len(s)-1
    while i < lenIdx:
        if s[i]+s[i+1] in subDict:
            num += subDict[s[i]+s[i+1]]
            i += 2
        else: 
            num += romDict[s[i]]
            i += 1     
    if i == lenIdx: num += romDict[s[-1]]
    return num

print(romanToInt("MCMXCIV"))