class Solution:
    def isPalindrome(self, s: str) -> bool:
        # is_valid = ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9')
        res=""
        for char in s:
            if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9'): 
                res+=char.lower()
        
        for i in range(len(res)//2):
            if res[i]!=res[len(res)-i-1]:
                return False
        return True

        