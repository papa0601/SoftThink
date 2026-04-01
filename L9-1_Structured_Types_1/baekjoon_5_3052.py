import sys
input = sys.stdin.readline

num_list = [0] * 10

for i in range(10):
    num_list[i] =int(input().rstrip())

print(len(list(set(list(num % 42 for num in num_list)))))