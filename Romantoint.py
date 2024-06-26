class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I":1,"V":5 ,"X":10 ,"L":50,"C":100,"D":500,"M":1000}

        count = 0
        i =0
        while len(s)> i :
            if i + 1 < len(s) and dic[s[i]] < dic[s[i+1]]:
                count = count + dic[s[i+1]] - dic[s[i]]
                i = i+2
                
            else:
                count= count +dic[s[i]]
                i = i+1
                
        return count
