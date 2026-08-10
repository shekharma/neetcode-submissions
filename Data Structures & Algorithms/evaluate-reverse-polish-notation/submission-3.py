class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]

        for c in tokens:
            if c =="+":
                second = int(stack.pop())
                first = int(stack.pop())
                add = second + first
                stack.append(add)
            elif c =="*":
                second = int(stack.pop())
                first = int(stack.pop())
                mul = second*first
                stack.append(mul)

            elif c =="-":
                second = int(stack.pop())
                first = int(stack.pop())
                sub = first - second
                stack.append(sub)
                
            elif c == "/":
                second = int(stack.pop())
                first = int(stack.pop())
                div = first/second
                stack.append(div)

            else:
                stack.append(c)
        return int(stack.pop())
