import sys
input = sys.stdin.readline

n = int(input().rstrip())

c = 5
p = 2

for _ in range(n-1):
    p += 1
    c += 3*p -2

print(c % 45678)