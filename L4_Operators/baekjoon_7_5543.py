import sys
input = sys.stdin.readline

sang, jung, ha, coke, sprite = [int(input().rstrip()) for _ in range(5)]
burgers = (sang, jung, ha)
drinks = (coke, sprite)

print(min(burgers) + min(drinks) - 50)