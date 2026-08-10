class Solution:
    def isValid(self, s: str) -> bool:
        # stack =[]
        # closeToOpen = {")":"(", "]":"[", "}":"{"}

        # for c in s:
        #     if c in closeToOpen:
        #         if stack and stack[-1]==closeToOpen[c]:
        #             stack.pop()
        #         else:
        #             return False
        #     else:
        #         stack.append(c)
        # return True if not stack else False

        stack =[]
        closetoOpen = {")":"(", "]":"[", "}":"{"}
        if len(s)%2==1:
            return False
        for c in s:
            if c in closetoOpen:
                if stack and stack[-1]==closetoOpen[c]: 
                    ## last element of stack == value of  current key in closetoOpen
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

                    
        