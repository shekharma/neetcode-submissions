class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left =0 
        right = len(nums)-1

        while left <= right:
            m = left + ((right- left)//2)

            if ((m-1 < 0 or nums[m-1]!= nums[m]) and (m+1 == len(nums) or nums[m]!= nums[m+1])):
                return nums[m]

            leftsize = m-1 if nums[m-1]==nums[m] else m

            if leftsize%2:
                right = m-1
            else:
                left = m+1