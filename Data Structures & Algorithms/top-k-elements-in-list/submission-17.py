class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1 = dict()
        for num in nums:
            d1[num] = 1 + d1.get(num, 0)
        # print(d1)
        ls = []
        for i in d1.keys():
            if(d1[i] >= k):
                ls.append(d1)
        print(ls)
        return ls
            