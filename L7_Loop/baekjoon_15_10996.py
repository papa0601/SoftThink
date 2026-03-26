import sys
input = sys.stdin.readline

n = int(input().rstrip())

if n == 1:
    print('*')
    exit()

for _ in range(n):
    print('* ' * (n//2) + '*' * (n%2))
    print(' *' * (n//2) + ' ' * (n%2))