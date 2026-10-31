class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for i in range(len(strs)):
            anas = [strs[i]]
            for j in range(i+1, len(strs)):
                if sorted(strs[i]) == sorted([j]):
                    anas.append(strs[j])
            anagrams['test'].append(anas)
        return anagrams['test']