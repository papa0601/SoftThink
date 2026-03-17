import sys
input = sys.stdin.readline

print(int(sum([(score if (score := int(input().rstrip())) > 40 else 40) for _ in range(5)]) / 5))