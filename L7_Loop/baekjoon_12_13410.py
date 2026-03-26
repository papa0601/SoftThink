import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))

largest = 0

for i in range(1, k+1):
    rslt = int(str(n * i)[::-1])
    largest = rslt if largest < rslt else largest

print(largest)