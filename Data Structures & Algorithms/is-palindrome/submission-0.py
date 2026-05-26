class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = re.sub(r'[^a-zA-Z0-9]', '', s)
        start = 0
        end = len(new_s) - 1    
        
        while (start < end):
            if new_s[start].lower() != new_s[end].lower():
                return False
            start += 1
            end -= 1

        return True