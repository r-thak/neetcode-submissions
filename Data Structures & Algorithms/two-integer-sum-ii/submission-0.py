class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hind = len(nums) - 1
        lind = 0

        while(True):
            high = nums[hind]
            low = nums[lind]
            if high + low == target: return [lind +1, hind + 1]
            if target - low < high:
                hind -= 1
                continue
            lind += 1