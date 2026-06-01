class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        tracker = set()
        res = 0
        counter = 0

        for c in s:
            while c in tracker:
                tracker.remove(s[l])
                l += 1
                counter -= 1
            tracker.add(c)
            counter += 1
            res = max(res, counter)
        return res