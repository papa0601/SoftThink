import sys
input = sys.stdin.readline

n = int(input().rstrip())
if n < 100:
    print(n)
    exit()

else:
    count = 99
    for i in range(100, n + 1):
        stringfied = str(i)
        if int(stringfied[2]) - int(stringfied[1]) == int(stringfied[1]) - int(stringfied[0]):
            count += 1
        
    print(count)