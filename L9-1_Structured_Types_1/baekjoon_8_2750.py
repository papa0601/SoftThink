import sys

digit_count = int(sys.stdin.readline().strip())
digit_list = [0] * digit_count
for i in range(digit_count):
    digit_list[i] = int(sys.stdin.readline().strip())

digit_list.sort()

for i in range(digit_count):
    print(digit_list[i])