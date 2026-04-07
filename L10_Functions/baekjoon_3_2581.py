from math import sqrt
import sys
input = sys.stdin.readline

lower = int(input().rstrip())
upper = int(input().rstrip())

def check_sosu(num: int) -> bool:
    for i in range(2, int(sqrt(num)) + 1):
        if i in not_sosu_cache:
            continue
        elif num % i == 0:
            return False
    return True

sosu_cache = set()
not_sosu_cache = set()
def create_cache(max: int) -> list[int]:
    for i in range(2, max + 1):
        if not check_sosu(i):
            not_sosu_cache.add(i)
        else:
            sosu_cache.add(i)

create_cache(upper)
sosu_list = [n for n in iter(sosu_cache) if lower <= n <= upper]
if sosu_list:
    print(sum(sosu_list))
    print(min(sosu_list))
else:
    print(-1)




