from functools import lru_cache
import timecheck

@lru_cache(maxsize=None)
def fibo(num: int) -> int:
    if num in (0, 1):
        return num
    
    return fibo(num-1) + fibo(num-2)


if __name__ == '__main__':
    with timecheck.check_time():
        print(fibo(5))