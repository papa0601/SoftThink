import sys
input = sys.stdin.readline

total_call_count = int(input().rstrip())
num_list = []
for _ in range(total_call_count):
    num = int(input().rstrip())
    if num:
        num_list.append(num)
    
    else:
        num_list.pop()

print(sum(num_list))
