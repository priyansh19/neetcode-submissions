class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in store:
                longest_streak, curr = 0, num
                while curr in store:
                    longest_streak += 1
                    curr += 1
                res = max(res, longest_streak)
        return res