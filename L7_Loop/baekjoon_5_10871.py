import sys
input = sys.stdin.readline

count, crit = map(int, input().split())
nums = list(map(int, input().split()))
nums = [num for num in nums if num < crit]
print(*nums, sep=' ')