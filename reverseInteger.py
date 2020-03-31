# Given a 32-bit signed integer, reverse digits of an integer.
# Assume we are dealing with an environment which could only store 
# integers within the 32-bit signed integer range: [−231,  231 − 1]. 
# For the purpose of this problem, assume that your function 
# returns 0 when the reversed integer overflows.

# faster than 86.17% less memory used than 6.45%
def reverseInt(x):
    """
    :type x: int
    :rtype: int
    """
    intList = []
    if x >= 0:
        for i in str(x):
            intList = [i] + intList
        num = int("".join(intList))
        if (num > (2 ** 31 - 1)): return 0 
        else: return num
    else:
        for i in str(-x):
            intList = [i] + intList
        num = -int("".join(intList))
        if (num < -(2 ** 31)): return 0 
        else: return num

print(reverseInt(-2340))

