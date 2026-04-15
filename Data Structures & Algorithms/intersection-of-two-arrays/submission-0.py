class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ls1 = list(set(nums1))
        ls2 = list(set(nums2))
        final = []
        for i in range(len(ls1)):
            if ls1[i] in ls2:
                final.append(ls1[i])
        
        return final


