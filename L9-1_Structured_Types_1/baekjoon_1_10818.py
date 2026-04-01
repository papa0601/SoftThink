import sys
input = sys.stdin.readline

count = int(input().rstrip())
nums = list(map(int, input().split()))

print(min(nums), max(nums))
