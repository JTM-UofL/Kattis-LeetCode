def rotate(nums: list[int], k: int) -> None:

    k = k % len(nums)
    buffer = nums[-k:] + nums[:-k]
    for i in range(len(buffer)):
        nums[i] = buffer[i]
        print(nums[i])

rotate(nums= [1,2,3,4,5,6,7,8,9], k=7)