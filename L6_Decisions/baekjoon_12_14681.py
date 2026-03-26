import sys
input = sys.stdin.readline

sa = {
    (True, True): '1',
    (False, True): '2',
    (False, False): '3',
    (True, False): '4',
}

x, y = [int(input().rstrip()) for _ in range(2)]

print(sa[(x>0, y>0)])
