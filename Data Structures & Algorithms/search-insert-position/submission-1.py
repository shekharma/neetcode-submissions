class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        res= len(nums)
        while left <= right:
            mid = (right + left)//2

            if nums[mid]>target:
                res = mid
                right = mid-1
            
            elif nums[mid]<target:
                left = mid+1
            elif nums[mid]==target:
                return mid
        
        return res