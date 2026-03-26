import sys
input = sys.stdin.readline

n = input().rstrip()
n = n if len(n) > 1 else n + '0'
cache = ''
loop = 0

while n != cache:
    loop += 1
    if not cache:
        cache = n

    cache = cache[1] + str(int(cache[0]) + int(cache[1]))[-1]

print(loop)
    
