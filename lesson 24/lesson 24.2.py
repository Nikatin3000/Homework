# from pythonds.basic import Stack
#
# def parChecker(symbolString):   це рішення з сайту
#     s = Stack()
#     balanced = True
#     index = 0
#     while index < len(symbolString) and balanced:
#         symbol = symbolString[index]
#         if symbol in "([{":
#             s.push(symbol)
#         else:
#             if s.isEmpty():
#                 balanced = False
#             else:
#                 top = s.pop()
#                 if not matches(top,symbol):
#                        balanced = False
#         index = index + 1
#     if balanced and s.isEmpty():
#         return True
#     else:
#         return False
#
# def matches(open,close):
#     opens = "([{"
#     closers = ")]}"
#     return opens.index(open) == closers.index(close)
#
#
# print(parChecker('{({([][])}())}'))
# print(parChecker('[{()]'))

def balanced(string):
    stack = []
    for i in string:
        if i in ['(', '[', '{']:
            stack.append(i)
        elif i in [')', ']', '}']:
            if not stack:
                return False
            if i == ')' and stack[-1] != '(':
                return False
            if i == ']' and stack[-1] != '[':
                return False
            if i == '}' and stack[-1] != '{':
                return False
            stack.pop()
    return not stack


print(balanced("()[]{}"))
print(balanced("([{}])"))
print(balanced("({)}"))