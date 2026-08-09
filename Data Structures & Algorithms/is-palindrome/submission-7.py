class Solution:
    def isPalindrome(self, s: str) -> bool:
        ## creating a cleaned string 
        res=""
        for char in s:
            if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9'): 
                res+=char.lower()
        
        
        l, r = 0, len(res)-1

        while l <r :
            if res[l]==res[r]:
                l+=1
                r-=1
                continue
            else:
                return False
        return True

        