class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*(len(nums))

        prefix =1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]
        # for nums = [1,2,3,4] --> the res = [1,1,2,8]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i]*=postfix
            postfix*= nums[i]
        return res

        # res = [1,1,2,8]
        # as we are appending backward so
        # res[3] = 8*1  --> now postfix becomes 1*nums[3]--> 6
        # res[2] = 2*6 --> previous postfix= 6 and new will be ---> 6*4
        # res[1] = 1*24 --> previous postfix = 24 and new will be --> 24*2
        # res[0] = 1*48