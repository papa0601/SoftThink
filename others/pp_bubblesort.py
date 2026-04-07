import sys
input = sys.stdin.readline

given_num = map(int, input().split()) if False else (2, 5, 3, 6)
target_list = list(given_num)

print(target_list)
print("=====================")

for i in range(len(target_list) - 1):
    print(f'i iter {i}')
    for x in range(len(target_list) - 1 - i):
        print(f'x iter {x}')
        if target_list[x] > target_list[x+1]:
            target_list[x], target_list[x+1] = target_list[x+1], target_list[x]
        print(target_list)
        
print("=====================")
print(target_list)

