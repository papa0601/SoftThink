import sys
input = sys.stdin.readline

# TODO 이거 완성하기 
a, b = map(int, input().split())
a, b = (a, b) if a < b else (b, a)
n = b - a + 1
avg = (a + b) // 2
print()