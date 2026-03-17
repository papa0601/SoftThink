import sys
input = sys.stdin.readline

times = [int(input().rstrip()) for _ in range(4)]
print(sum(times) // 60, sum(times) % 60, sep='\n')