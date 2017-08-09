import requests
import asyncio

async def requests_coroutine(name, url):
    print(name, requests.get(url))

async def parallel_on_loop():
    await asyncio.gather(
            requests_coroutine("A", "https://httpbin.org/range/1024?duration=5"),
            requests_coroutine("B", "http://www.google.com"),
            requests_coroutine("C", "http://www.google.com")
            )

loop = asyncio.get_event_loop()

loop.run_until_complete(parallel_on_loop())

loop.close()

