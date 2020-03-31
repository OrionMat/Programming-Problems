# Determine whether an integer is a palindrome. 
# An integer is a palindrome when it reads the same backward as forward.

# faster than 99.49% less memory used than 6.03%
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    y = str(x)
    return y == y[::-1]

print(isPalindrome(1221))