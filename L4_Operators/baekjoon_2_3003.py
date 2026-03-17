import sys
input = sys.stdin.readline

target_number = [1, 1, 2, 2, 2, 8]
current_count = list(map(int, input().rstrip().split(' ')))

need_count = [str(target_number[i] - current_count[i]) for i in range(len(target_number))]

print(" ".join(need_count))