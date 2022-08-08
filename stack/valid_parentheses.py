class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        brackets = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for bracket in s:
            if bracket not in brackets:
                stack.append(bracket)
            else:
                if not stack or brackets[bracket] != stack.pop():
                    return False
        return True if not stack else False
