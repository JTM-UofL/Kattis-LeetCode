def majorityElement(nums: list[int]) -> int:
    dictionary = {}
    for i in nums:
        if i in dictionary: dictionary[i] += 1
        else: dictionary[i] = 1
    
    return max(dictionary, key=dictionary.get)


print(majorityElement(nums=[2,2,1,1,1,2,2]))