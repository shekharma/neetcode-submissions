class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi=0
        for i in range(len(nums)):
            j=i
            length=0
            while j<len(nums) and nums[j]!=0:
                j+=1
                length += 1
            maxi = max(maxi, length)
        return maxi
