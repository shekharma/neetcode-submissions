class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     second = target - nums[i]
        #     j=i+1
        #     while j< len(nums):
        #         if nums[j]==second:
        #             return [i, j]
        #         j+=1
        # return False

        ##HashMap 
        hash_dict ={}
        for i, n in enumerate(nums):
            diff = target -n
            if diff in hash_dict:
                return[hash_dict[diff], i]
            hash_dict[n]=i


        