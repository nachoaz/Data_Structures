# queue_using_two_stacks.py


import sys
sys.path.append('../Stacks')
from stack import Stack


class TwoStacksQueue(object):
    def __init__(self):
        self._instack = Stack()
        self._outstack = Stack()

    def enqueue(self, x):
        self._instack.push(x)

    def dequeue(self):
        if self._outstack.is_empty():
            while not self._instack.is_empty():
                popped_val = self._instack.pop()
                self._outstack.push(popped_val)

        return self._outstack.pop()

    def peekfront(self):
        if self._outstack.is_empty():
            while not self._instack.is_empty():
                popped_val = self._instack.pop()
                self._outstack.push(popped_val)

        return self._outstack.peek()


def main():
    n = int(input())
    q = TwoStacksQueue()
    
    for _ in range(n):
        cmd, *arg = input().split()
        
        if int(cmd) == 1:
            q.enqueue(int(arg[0]))
        elif int(cmd) == 2:
            q.dequeue()
        elif int(cmd) == 3:
            print(q.peekfront())


if __name__ == '__main__':
    main()
