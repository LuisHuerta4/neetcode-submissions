class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        # Go through strings. Store each in a dict. If dicts are the same, anagram

        s_dict = dict()
        t_dict = dict()

        for i in s:
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 1

        for i in t:
            if i in t_dict:
                t_dict[i] += 1
            else:
                t_dict[i] = 1

        if s_dict != t_dict:
            return False 

        return True