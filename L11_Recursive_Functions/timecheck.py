from contextlib import contextmanager
import time

@contextmanager
def check_time():
    start_time = time.time()
    try:
        yield

    finally:
        print(f"took {((time.time() - start_time) * 1000):.5f}ms")