class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for ch in s:
            if ch == '[' or ch == '(' or ch == '{':
                stk.append(ch)
            elif ch == ']' or ch == ')' or ch == '}':
                if not stk:
                    return False
                if ch == ']' and stk[-1] != '[':
                    return False
                elif ch == ')' and stk[-1] != '(':
                    return False
                elif ch == '}' and stk[-1] != '{':
                    return False
                stk.pop()
        if stk:
            return False
        return True

    def isValid(self, s: str) -> bool:
        stk = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stk += ch,
                continue
            
            if not stk:
                return False

            if not ((ch == ')' and stk[-1] == '(') or 
                (ch == ']' and stk[-1] == '[') or 
                (ch == '}' and stk[-1] == '{')):
                return False
            
            stk.pop()
        return True if not stk else False

