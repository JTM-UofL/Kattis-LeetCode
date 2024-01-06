
def removeDuplicates(nums: list[int]):

    slow, fast = 0, 1

    hash_map = {}
    hash_map[nums[slow]] = 1

    while (fast <= len(nums)):

        if (nums[fast] in hash_map): #if the number is a key in the hashmap

            if (hash_map[nums[fast]] < 2): #if the number has been seen twice
                hash_map[nums[fast]] += 1
                slow += 1
                nums[slow] = nums[fast]


        else:
            hash_map[nums[fast]] = 1
            slow += 1
            nums[slow] = nums[fast]

        fast += 1

    return slow + 1, nums