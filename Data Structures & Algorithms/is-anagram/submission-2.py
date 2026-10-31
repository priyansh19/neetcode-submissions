class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # is_anagram = False
        # if sorted(s) == sorted(t):
        #     is_anagram = True
        # return is_anagram

        is_anagram = False
        seen_s = set(sorted(s))
        seen_t = set(sorted(t))
        if seen_s == seen_t:
            return True
        return False
