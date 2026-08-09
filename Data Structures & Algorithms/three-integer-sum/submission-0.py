class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort() # this can help in avoiding duplocates
        
        for i, a in enumerate(nums):
            ## skip the repetative numbers
            if i > 0 and a ==nums[i-1]:
                continue

            left, right = i+1, len(nums)-1
            while left <right:
                threesum = a + nums[left] + nums[right]
                if threesum==0:
                    res.append([a, nums[left], nums[right]])
                    left+=1
                    ## to avoid duplication for 2nd pointer as well
                    while nums[left]==nums[left-1] and left < right:
                        left+=1


                if threesum >0:
                    right -=1
                if threesum <0:
                    left +=1
        return res
