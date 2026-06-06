class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        t_table = {}
        s_table = {}

        for c in t:
            t_table[c] = t_table.get(c, 0) + 1
        
        have = 0
        need = len(t_table)

        res_index = [-1, -1]
        res_len = float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            s_table[c] = s_table.get(c, 0) + 1

            # If curr char appears the same times as in t
            if c in t_table and s_table[c] == t_table[c]:
                have += 1

            # Valid substring of s
            while have == need: 
                if (r - l + 1) < res_len: # New shortest len
                    res_index = [l, r]
                    res_len = (r - l + 1)

                s_table[s[l]] -= 1 # Pop from left of window
                if s[l] in t_table and s_table[s[l]] < t_table[s[l]]: #If popped a needed char
                    have -= 1

                l += 1

        l, r = res_index
        if res_len != float("infinity"):
            return s[l:r+1]
        else:
            return ""

                