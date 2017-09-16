# castle_on_the_grid.py
"""
https://www.hackerrank.com/challenges/castle-on-the-grid
"""


from queue import Queue


def main():
    n = int(input())
    grid = [['0' for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j, char in enumerate(list(input())):
            grid[j][i] = char

    startX, startY, goalX, goalY = list(map(int, input().split()))







if __name__ == '__main__':
    main()
