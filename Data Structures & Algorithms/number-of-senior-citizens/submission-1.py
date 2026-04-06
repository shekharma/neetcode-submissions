class Solution:
    def countSeniors(self, details: List[str]) -> int:
        total = 0
        for char in details:
            for i in range(len(char)):
                if char[i]=="M" or char[i]=="F" or char[i]=="O":
                    age = int(char[i+1])*10 + int(char[i+2])
                    if age>60:
                        total+=1
        return total
