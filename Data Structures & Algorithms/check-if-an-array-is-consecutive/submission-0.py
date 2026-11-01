class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        l = len(nums)
        minim = nums[0]
        for i in nums:
            minim = min(i, minim)

        hash1 = set()
        for i in nums:
            if 0 <= i <= (minim + l + 1):
                if i in hash1:
                    return False
                hash1.add(i)
            else:
                return False
        return True