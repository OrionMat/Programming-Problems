# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# faster than 61.76% less memory used than 5.04%
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    brakDict = {')':'(', '}':'{', ']':'['}
    openSet = {'(', '[', '{'}
    stack = []
    
    for i in s:
        if i in openSet:
            stack.append(i)
        else:
            if not stack:
                return False
            if brakDict[i] == stack[-1]:
                stack.pop()
            else:
                return False
    if len(stack) > 0:
        return False
    return True

print(isValid('()'))