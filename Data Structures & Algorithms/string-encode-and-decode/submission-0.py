class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        ## store each string in the list with some indentifier which will be easy to decode so here we decide to add length of string, plus delimiter to handle scenario where the string starts with the the number and then string. example ["leet", "codes"] --> "4#leet5#codes"
        for s in strs:
            res+= str(len(s))+ "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j=i
            while s[j]!="#":
                j+=1
            length = int(s[i:j]) # this will be the length of string it could be more than one digit 
            res.append(s[j+1:j+1+length])
            i = j+1+length ## now next time i'll directly start from here to iterate for the next string
        return res

