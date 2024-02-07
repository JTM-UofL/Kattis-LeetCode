class Solution:
    def hIndex(self, citations: list[int]) -> int:
        d, h = {}, len(citations)
        for num in citations: 
            if num in d: d[num] += num
            else: d[num] = num
        for key in d:
            print(key, d[key])
Solution.hIndex(Solution, citations=[3, 0, 6, 1, 5, 3])