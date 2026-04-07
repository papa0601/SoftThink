import sys
input = sys.stdin.readline

def d(num: int):
    return num + sum(map(int, str(num)))

not_self_nums = set()

for i in range(1, 10001):
    not_self_nums.add(d(i))

self_nums = [n for n in range(1, 10001) if n not in not_self_nums]

print(*self_nums, sep='\n')