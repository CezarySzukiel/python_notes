import asyncio
from asyncio import Future
from typing import Callable, Any

import aiohttp


class Fetch(Future):
    def __init__(self, url: str) -> None:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        super().__init__()
        task = loop.create_task(self._fetch(url))
        self.result = None
        # loop.run_until_complete(task)

    async def _fetch(self, url: str) -> None:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                self.result = data
                self.set_result(data)

    def then(self, callback: Callable) -> None:
        self.add_done_callback(lambda future: callback(future.result()))


def fetch_data(url: str) -> None:
    data = yield Fetch(url)
    print("Data: ", data)

url_ = "https://api.nbp.pl/api/exchangerates/rates/a/eur"
# asyncio.run(fetch_data(url_))
gen_data = fetch_data(url_)
print(gen_data)
next(gen_data).then(lambda x: gen_data.send(x))




class CM:  # Context Manager
    def __enter__(self):
        pass

    def __exit__(self):
        pass


class ACM:  # Async Context Manager
    async def __aenter__(self):
        pass

    async def __aexit__(self):
        pass
