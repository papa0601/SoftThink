import sys
input = sys.stdin.readline

a, b = map(int, input().split())
a, b = (a, b) if a < b else (b, a)
n = b - a + 1
print(int(n*(n+1)/2 + n*(a-1)))