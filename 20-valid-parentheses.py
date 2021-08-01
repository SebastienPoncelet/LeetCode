class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        ref = {
            ')': '(',
            ']' : '[',
            '}' :'{'
        }
        
        if len(s) <= 1:
            return False
    
        for bracket in s:
            
            if bracket == '(' or bracket == '[' or bracket == '{':
                stack.append(bracket)
            elif ref[bracket]:
                if len(stack) == 0:
                    return False
                if stack[-1] == ref[bracket]:
                    stack.pop()
                else:
                    return False
      
        if len(stack) > 0:
            return False
        
        return True
      
# Runtime: 20 ms, faster than 99.22% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 14.2 MB, less than 86.87% of Python3 online submissions for Valid Parentheses.
