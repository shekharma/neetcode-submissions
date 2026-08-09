class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset =set()
        l =0
        res =0

        for r in range(len(s)):
            ## i'm starting from 0-index, now continue loop to remove the first char     because we are seeing the current char is same as the first and we are incresing windowsize
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            ## now new char is not in set we are adding in set and calculating the new length
            charset.add(s[r])
            res = max(res, r-l+1)
        return res