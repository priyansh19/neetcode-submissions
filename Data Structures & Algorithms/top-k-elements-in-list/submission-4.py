class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ls1 = set()
        dict1 = dict()
        for n in nums:
            if n in dict1:
                dict1[n] += 1
                if dict1[n] >= k:
                    ls1.append(n)
            else:
                dict1[n] = 1
        return ls1