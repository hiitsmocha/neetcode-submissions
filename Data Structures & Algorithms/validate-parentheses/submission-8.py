class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_op = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for i in s:
            if i not in close_to_op:
                stack.append(i)
            elif i in close_to_op and len(stack) != 0 and stack[-1] != close_to_op[i] :
                return False
            elif i in close_to_op and len(stack) != 0 and stack[-1] == close_to_op[i]:
                stack.pop()
            else:
                return False
        return len(stack) == 0