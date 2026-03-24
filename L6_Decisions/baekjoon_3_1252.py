import sys
input = sys.stdin.readline

bint = lambda x: int(x, 2)
a, b = map(bint, input().split())
print(bin(a + b)[2:])