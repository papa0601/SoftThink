import sys
input = sys.stdin.readline

target_num = int(input().rstrip())
att = target_num // 5
for five_count in list(range(1, att+1))[::-1]:
    if target_num - five_count * 5 == 0:
        print(int(five_count))
        break
    
    elif (target_num - five_count * 5) % 3 == 0:
        print(int(five_count + (target_num - five_count * 5) / 3))
        break

else:
    if target_num % 3 == 0:
        print(int(target_num / 3))
    
    else:
        print(-1)
