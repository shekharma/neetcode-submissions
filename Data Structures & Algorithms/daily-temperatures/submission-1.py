class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # ls =[]

        # for i in range(len(temperatures)-1):
        #     j=i+1
        #     while j < len(temperatures):
        #         if temperatures[j] > temperatures[i]:
        #             diff = j - i
        #             ls.append(diff)
        #             break
        #         j += 1
        #     else:
        #         ls.append(0) ## for every last 
        # ls.append(0)
        # return ls

        res =[0]*len(temperatures)
        stack =[]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i-stackInd)
            stack.append([t,i])
        return res