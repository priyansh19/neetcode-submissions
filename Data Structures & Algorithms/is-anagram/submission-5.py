class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # is_anagram = False
        # if sorted(s) == sorted(t):
        #     is_anagram = True
        # return is_anagram
        if len(s) != len(t):
            return False

        is_anagram = False
        seen_s = sorted(s)
        seen_t = sorted(t)
        if seen_s == seen_t:
            return True
        return False
