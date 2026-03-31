class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dict_s = Counter(s)
        char_dict_t = Counter(t)

        if not char_dict_s == char_dict_t: return False
        return True