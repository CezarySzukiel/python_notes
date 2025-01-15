import asyncio

from util import delay


async def hello_every_second():
    for i in range(2):
        await asyncio.sleep(1)
        print(f'Running other code while I am sleeping')


async def main():
    first_delay = asyncio.create_task(delay(3))
    second_delay = asyncio.create_task(delay(3))
    await hello_every_second()
    await first_delay
    await second_delay


asyncio.run(main())  # tworzy pętle zdarzeń i wrzuca courutyny do kolejki zdarzeń

# zwykły sleep jest blokujący, a await asyncio.sleep() jest nieblokujący innych operacji
