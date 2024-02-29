class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort()
        citations.reverse()
        h_index = 0
        for citation in citations:
            if citation > h_index:
                h_index += 1
            else: break
        return h_index

print(Solution.hIndex(Solution, citations=[3, 0, 6, 1, 5, 3]))