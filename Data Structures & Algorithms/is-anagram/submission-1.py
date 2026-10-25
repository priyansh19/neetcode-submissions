class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        is_anagram = False
        if sorted(s) == sorted(t):
            is_anagram = True
        return is_anagram