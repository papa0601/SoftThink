import sys
input = sys.stdin.readline

money, pocket = map(int, input().split())
print(money // pocket, money % pocket, sep='\n')