class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hash_dict = {}

        # for num in nums:
        #     hash_dict[num] = 1 + hash_dict.get(num,0)
        # ls = []
        # for key, value in hash_dict.items():
        #     if len(ls)<k+1:
        #         ls.append(value)
        #     else:
        #         temp = min(ls)
        #         final_temp = min(temp, value)
        #         ls.append(final_temp)
        #         ls.pop(0)
        # return ls

        #### solution using bucket sort
        #1. create a hashmap
        count ={}
        #2. we are creating a lists to store the each value that store each value seprately if total list has unique value
        freq =[[] for i in range (len(nums)+1)] ## fpr n unique numbers, unique lists

        for n in nums:
            count[n] = 1+ count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)
        ## example nums = [1,2,2,3,3,3, 4]  freq = [[], [1, 4], [2], [3], [], [], [], []]

        res =[]
        for i in range(len(freq)-1, 0, -1):  ## reverse index 6,5,4...
            for n in freq[i]: ## start from the last of freq list 
                res.append(n)
                if len(res)==k:
                    return res
                

