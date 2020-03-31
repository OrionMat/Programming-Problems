# Sorted Two sum

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

def twoSumHash(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    dict = {}
    for idx, num in enumerate(numbers):
        val = target - num
        if val in dict: return [dict[val]+1, idx+1]
        else: dict[num] = idx

print(twoSumHash([2,7,11,15], 9))