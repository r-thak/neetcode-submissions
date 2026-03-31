class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        groups = []

        for i in nums:
            freqs[i] = 1 + freqs.get(i, 0)
        
        for i in freqs.keys():
            heapq.heappush(groups, (freqs[i], i))
            if len(groups) > k: heapq.heappop(groups)
        
        ret = []
        for i in range(k):
            ret.append(heapq.heappop(groups)[1])
        return ret