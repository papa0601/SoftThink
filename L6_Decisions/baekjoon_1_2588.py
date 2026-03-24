import sys
input = sys.stdin.readline

origin = int(input().rstrip())
target = input().rstrip()
i = iter(target[::-1])

for _ in range(3):
    print(origin * int(next(i)))
print(origin * int(target))