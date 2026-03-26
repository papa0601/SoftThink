import sys
import math
input = sys.stdin.readline

given_string = input().rstrip()
num = 0

for char in given_string:
    if 97 <= ord(char) <= 122:
        num += ord(char) - 96
    else:
        num += ord(char) - 38

def is_prime(num: int) -> bool:
    if num == 1: return True
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0: return False
    return True

print(f"It is {'' if is_prime(num) else 'not '}a prime word.")