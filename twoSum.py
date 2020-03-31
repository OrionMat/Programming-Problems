# Two sum

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# faster than 91.50% less memory used than 5.13%
def onePassHash(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dict = {}
    i = 0
    for idx, num in enumerate(nums):
        result = target - num
        hash_index = dict.get(result)
        if hash_index and hash_index != idx:
            return [idx, hash_index]
        dict[num] = i
        i +=1
        return None

def twoPassHash(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hashtable = {value: index for index, value in enumerate(nums)}
    for index, value in enumerate(nums):
        result = target - value
        hash_index = hashtable.get(result)
        if hash_index and hash_index != index:
            return [index, hash_index]