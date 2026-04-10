import time
from contextlib import contextmanager


@contextmanager
def check_time():
    start_time = time.time()
    try:
        yield

    finally:
        print(f"took {((time.time() - start_time) * 1000):.5f}ms")


def gcd(a: int, b: int) -> int:
    """ "유클리드 알고리즘으로 최소 공약수 구하기"""
    while b:
        a, b = b, a % b

    return a


counter = 0


def fibo(n: int, count: bool = False) -> int:
    """ "피보나치 수열을 재귀적으로 구하기"""
    global counter
    if count:
        counter += 1

    if n <= 1:
        return n

    return fibo(n - 1, count=count) + fibo(n - 2, count=count)


def fibo_for(n: int) -> int:
    """for 루프를 이용해서 피보나치 수열을 구한다"""
    if n == 0 or n == 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


if __name__ == "__main__":
    # print(gcd(6, 8))
    with check_time():
        print(f"fibo(5): {fibo(5)}")

    with check_time():
        print(f"fibo_for(5): {fibo_for(5)}")
