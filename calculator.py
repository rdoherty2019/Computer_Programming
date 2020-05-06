from stack import Stack
"""
class RPNCalculator:
"""

class RPNCalculator:
    def __init__(self, expression):
        self.expression = expression

    def evaluate(self):
        s = Stack()
        for token in self.expression:
            if token.isnumeric():
                s.push(token)
            else:
                if token == '+':
                    op1 = int(s.pop())
                    op2 = int(s.pop())
                    ans = op1 + op2
                    s.push(ans)
                elif token == "*":
                    op1 = int(s.pop())
                    op2 = int(s.pop())
                    ans = op1 * op2
                    s.push(ans)
                elif token == "-":
                    op1 = int(s.pop())
                    op2 = int(s.pop())
                    ans = op1 - op2
                    s.push(ans)
                elif token == "/":
                    op1 = int(s.pop())
                    op2 = int(s.pop())
                    ans = op1 / op2
                    s.push(ans)
                elif token == "**":
                    op1 = int(s.pop())
                    op2 = int(s.pop())
                    ans = op1 ** op2
                    s.push(ans)

        temp = s.pop()

        if s.empty():
            ans = temp
            return ans
        else:
            return None




if __name__ == '__main__':
    c = RPNCalculator('2 3 * 4 +')
    print(c)
    print(c.expression) # '2 3 * 4 +'
    print(c.evaluate()) # 10

""" if s.empty():
            return None
        else:
            return s.peek()"""