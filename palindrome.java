class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        sr = str(x)
        if sr[::-1] == sr:
            return True
