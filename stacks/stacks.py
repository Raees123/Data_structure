from collections import deque

class Stack:
    def __init__(self):
        self.__list = deque()

    def push(self, items):
        self.__list.append(items)

    def pop(self):
       return self.__list.pop()

    def isEmpty(self):
       return len (self.__list) == 0


s = Stack()

s.push(1)
s.push(2)
s.push(3)

print(s.pop()) #3
print(s.pop()) #2
print(s.pop()) #1
