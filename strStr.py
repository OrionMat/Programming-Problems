# Implement strStr()

# Return the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.

# faster than 78.32% less memory used than 10.26%
def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    needLen = len(needle)
    matchEnd = len(haystack) - needLen + 1
    for i in range(matchEnd):
        if haystack[i:i+needLen] == needle: return i
    return -1 if needle else 0