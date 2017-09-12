# maximum_element.py
"""
https://www.hackerrank.com/challenges/maximum-element
"""


from stack_with_max_api import StackWithMaxAPI


def main():
    my_stack = StackWithMaxAPI()

    n = int(input())
    for _ in range(n):
        cmd, *arg = list(map(int, input().split()))
        if cmd == 1:
            my_stack.push(arg[0])
        elif cmd == 2:
            my_stack.pop()
        elif cmd == 3:
            print(my_stack.max())


if __name__ == '__main__':
    main()
