"""
class Stack:
"""
class Stack:
    #contructor
    def __init__(self):
        self.elements = []
    def __str__(self):
        new_list = ["|"+str(ele)+ "|" for ele in self.elements]
        return "\n".join(new_list) + "\n ‾"

    def push(self, value):
        self.elements.insert(0, value)
    def empty(self):
        if len(self.elements) == 0:
            return True
        else:
            return False
    def peek(self):
        return self.elements[0]

    def pop(self):
        return self.elements.pop(0)



if __name__ == '__main__':
    s = Stack()
    print(s.empty()) # True
    s.push(1)
    print(s.empty()) # False
    s.push(2)
    s.push(3)
    print(s.peek()) # 3
    print(s.pop()) # 3
    print(s.peek()) # 2
    print(s)
