import sys
input = sys.stdin.readline

nums = [int(input().rstrip()) for _ in range(9)]
M = max(nums)

print(M, nums.index(M) + 1, sep='\n', end='')   