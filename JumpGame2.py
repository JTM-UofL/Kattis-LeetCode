class Solution:
    def jump(self, nums: list[int]) -> int:
        left, right, jumps, n = 0, 0, 0, len(nums)
        if n == 1: return 0
        if n == 2: return 1
        while (right != n-1):
            max = 0
            for _ in range(left + nums[left] - right):
                right += 1
                if max < right + nums[right]:
                    max = right + nums[right]
                    left = right
                if right == n-1:
                    break
            jumps += 1
        return jumps
