import sys
input = sys.stdin.readline

num = int(input().rstrip(), 8)
print(bin(num)[2:])