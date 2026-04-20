class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums

        final =[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                final.append(nums[i])
        
        for i in range(len(nums)):
            if nums[i]%2!=0:
                final.append(nums[i])

        return final
