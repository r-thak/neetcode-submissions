class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        groups = []

        for i in nums:
            freqs[i] = 1 + freqs.get(i, 0)
        
        for i, j in freqs.items(): groups.append([j, i])
        groups.sort()

        ret = []
        for i in range(k):
            ret.append(groups.pop()[1])
        return ret