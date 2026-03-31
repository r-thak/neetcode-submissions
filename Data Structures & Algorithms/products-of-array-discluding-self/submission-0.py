class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]] # Prefixes starting at nums[1]
        suffix = [nums[len(nums) - 1]] # Suffixes ending at nums[last]

        for i in range(1, len(nums) - 1): # Ascending order [0] ommitted
            prefix.append(nums[i] * prefix[i - 1])


        for i in range(len(nums) - 2): # Descending order [last] ommitted
            suffix.append(suffix[i] * nums[len(nums) - 2 - i])

        output = [suffix[len(suffix) - 1]] # First element is suffix for nums[0]

        for i in range(1, len(nums) - 1): # [FILLED, ..., WILL FILL]
            output.append(prefix[i - 1] * suffix[len(suffix) - 1 - i])
        
        output.append(prefix[len(prefix) - 1]) #[FILLED, MIDDLE, FILLED]

        return output