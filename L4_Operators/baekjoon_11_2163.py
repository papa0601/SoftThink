import sys
input = sys.stdin.readline

n, m = sorted(list(map(int, input().split())))
print((n-1) + (m-1) * (n))