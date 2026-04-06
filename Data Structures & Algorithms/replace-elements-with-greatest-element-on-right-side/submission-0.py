class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        final = []

        for i in range(len(arr)):
            j =i+1
            maxi =-1
            for j in range(i+1,len(arr)):
                maxi = max(maxi,arr[j])
            print(i, maxi)
            final.append(maxi)
        return final