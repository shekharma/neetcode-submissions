class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash_set = set()
        i =0
        while i <len(nums):
            if nums[i] in hash_set:
                return int(nums[i])
            else:
                hash_set.add(nums[i])
                i+=1
        return -1