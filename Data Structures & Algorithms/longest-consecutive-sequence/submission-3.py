class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return 1

        inset = {}
        for i in nums:
            inset[i] = True

        seqs = []
        for k in inset.keys():
            if not k - 1 in inset:
                seqs.append(k)

        ret = 0
        for k in seqs:
            ind = k
            while ind + 1 in inset: ind += 1
            if ind - k > ret: ret = ind - k

        return ret + 1