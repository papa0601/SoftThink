import sys
input = sys.stdin.readline

t = int(input().rstrip())
for i in range(t):
    print(' '*(t-(i+1)) + '*'*(i+1))