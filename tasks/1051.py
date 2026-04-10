import sys
input = sys.stdin.readline

n, m = map(int, input().split())
square = list()

for _ in range(n):
    square.append(list(map(int, input().rstrip())))

for x in range(min(n, m), -1, -1):
    for i in range(n-x):
        for j in range(m-x):
            if square[i][j] == square[i+x][j] == square[i][j+x] == square[i+x][j+x]:
                print(pow((x+1), 2))
                exit()
            
            