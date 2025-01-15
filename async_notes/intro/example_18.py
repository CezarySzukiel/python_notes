import asyncio

from util import delay


def call_later():
    print('calling in future')


async def main():
    loop = asyncio.get_running_loop()  # pobiera aktualną pętlę, która działa, a jeśli jej nie ma to zwraca błąd
    loop.call_soon(call_later)  # call_soon() - wywołuje kod niezwłocznie
    print("yolo")

    d5 = asyncio.create_task(delay(5))
    d3 = asyncio.create_task(delay(3))
    await delay(3)
    await delay(5)


asyncio.run(main())
