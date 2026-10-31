class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        is_anagram = False
        if s.sort() == t.sort():
            is_anagram = True
        return is_anagram