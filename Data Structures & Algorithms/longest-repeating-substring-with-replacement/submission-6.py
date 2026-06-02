class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        res = 0

        for r in range(len(s)):
            # Update count for character
            freq[s[r]] = freq.get(s[r], 0) + 1

            # if k > amount of least appearing characters, you can replace them for valid string
            # Otherwise, move left over until you can replace characters for a valid string
            while (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] = freq.get(s[l], 0) - 1
                l += 1

            res = max(res, (r - l + 1))
    
        return res