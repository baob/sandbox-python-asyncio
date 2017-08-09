import requests
import asyncio
import aiohttp
from aiohttp import ClientSession

async def requests_coroutine(name, url):
    print(name, requests.get(url))

async def parallel_on_loop():
    await asyncio.gather(
            get_file("A", "https://httpbin.org/range/1024?duration=15"),
            get_file("B", "https://httpbin.org/range/1024?duration=10"),
            get_file("C", "https://httpbin.org/range/1024?duration=5"),
            )

async def get_file(name, url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            result = await response.read()
            print(name, response.status)

loop = asyncio.get_event_loop()

loop.run_until_complete(parallel_on_loop())

loop.close()

