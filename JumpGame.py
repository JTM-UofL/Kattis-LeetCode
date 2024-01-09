
# Iterate backwards through the list and set goal to the closest number that can reach the current goal

# This accomplishes a greedy approach starting at the end of the list and working its way to the beginning,
# If the goal isnt at the beginning of the array at the end of iteration, then the end is not reachable

# O(n) time and complexity
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        g = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if (i + nums[i] >= g):
                g = i
        return g == 0