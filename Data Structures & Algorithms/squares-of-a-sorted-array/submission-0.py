class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        final = []

        for i in range(len(nums)):
            final.append(nums[i]*nums[i])

        return sorted(final)