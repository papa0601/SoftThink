import sys
input = sys.stdin.readline

T = int(input().rstrip())

for i in range(1, T+1):
    print(f"Case #{i}: {sum(map(int, input().split()))}")