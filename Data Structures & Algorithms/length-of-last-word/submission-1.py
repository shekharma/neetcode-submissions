class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        length = 0
        for i in range(len(s)-1, -1, -1):
            if length==0 and s[i]==" ":
                continue

            while s[i]!=" " and i>=0:
                length+=1
                i-=1
            return length
        