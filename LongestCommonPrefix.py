# Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# All given inputs are in lowercase letters a-z.

# faster than 73.61% less memory used than 6.25%
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    listLen = len(strs)
    if listLen: firstWord = strs[0]
    else : return ""
    pre = ""
    for i, char1 in enumerate(firstWord):
        j = 1
        while(j < listLen):
            if i < len(strs[j]): 
                if char1 == strs[j][i]: j += 1
                else: return pre
            else: return pre
        pre += char1
    return pre



list = ["flower","flow","flight"]
print(longestCommonPrefix(list))



# def longestCommonPrefix(strs):
#     """
#     :type strs: List[str]
#     :rtype: str
#     """
#     longestPre = ""
#     remaining = strs[1:]
#     for i, word1 in enumerate(strs):
#         for word2 in remaining[i:]:
#             pre = ""
#             for idx in range(len(word1)):
#                 if idx > len(word2) -1: break
#                 if word1[idx] == word2[idx]: pre += word1[idx]
#                 else: break
#             if len(pre) > len(longestPre): longestPre = pre
#     return longestPre

# list = ["cat", "clap", "dog", "catfish"]
# print(longestCommonPrefix(list))