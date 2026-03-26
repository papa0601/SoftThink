import sys
input = sys.stdin.readline

string = ''
while True:
    string = input().rstrip()
    if string == '0 0':
        break
    print(sum(map(int, (x.strip() for x in string.split(' ')))))