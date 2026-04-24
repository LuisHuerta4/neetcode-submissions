class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = dict()
        t_list = dict()

        if len(s) != len(t):
            return False
        
        for char in s:
            if char not in s_list:
                s_list[char] = 1
            else:
                s_list[char] += 1

        for char in t:
            if char not in t_list:
                t_list[char] = 1
            else:
                t_list[char] += 1

        for key in s_list:
            if key not in t_list:
                return False
            elif s_list[key] != t_list[key]:
                return False
        
        return True