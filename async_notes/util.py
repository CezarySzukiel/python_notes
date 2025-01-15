import asyncio
import functools
import time
from typing import Callable, Any


async def delay(delay_seconds: int) -> int:
    print(f'sleeping for {delay_seconds} seconds')
    await asyncio.sleep(delay_seconds)
    print(f'Finished sleeping for {delay_seconds} seconds')
    return delay_seconds


def async_timed() -> Callable:
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f'starting {func.__name__} with args: {args} and kwargs: {kwargs}')
            start_time = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end_time = time.time()
                total_time = end_time - start_time
                print(f"Finished {func.__name__} in {total_time:.4f} seconds")

        return wrapped

    return wrapper
