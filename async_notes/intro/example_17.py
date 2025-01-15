import asyncio


async def main() -> None:
    await asyncio.sleep(1)


loop = asyncio.new_event_loop()

try:
    loop.run_until_complete(main())
    # loop.run_forever(main()) działa dopóki ręcznie nie zabijesz, lub nie skończy się program
finally:
    loop.close()

