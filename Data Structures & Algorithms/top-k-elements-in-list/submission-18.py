class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1 = dict()
        ls = []
        for num in nums:
            d1[num] = 1 + d1.get(num, 0)
        for i in d1.keys():
            if(d1.get(i) >= k):
                ls.append(i)
        return ls
            