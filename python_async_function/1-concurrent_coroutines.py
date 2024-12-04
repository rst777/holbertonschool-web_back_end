import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay and returns it.

    Args:
        max_delay (int): Maximum possible delay in seconds. Defaults to 10.

    Returns:
        float: Random delay between 0 and max_delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Spawn wait_random n times and return the list of delays in ascending order.

    Args:
        n (int): Number of times to spawn wait_random
        max_delay (int): Maximum possible delay for each wait_random call

    Returns:
        list[float]: List of delays, sorted without using sort()
    """
    # Create and wait for all tasks
    delays = await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])

    # Sort using list comprehension
    return sorted(delays)
