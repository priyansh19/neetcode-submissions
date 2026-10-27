class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix and suffix product arrays
        l = len(nums)
        prefix = [1] * l
        suffix = [1] * l

        # populate the prefix sum arrays
        for i in range(1, l):
            prefix[i] = prefix[i-1] * nums[i-1]

        for j in range(l - 2, -1, -1):
            suffix[j] = suffix[j+1] * nums[j+1]
        
        newRes = [1] * l
        for i in range(l):
            newRes[i] = prefix[i] * suffix[i]
    
        return newRes