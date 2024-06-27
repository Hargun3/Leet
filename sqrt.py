class Solution:
    def mySqrt(self, x: int) -> int:
        first = 0
        last = x

        while last>=first:
            mid= (first +last)//2
            if(mid*mid<=x):
