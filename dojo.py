import requests
import asyncio

async def requests_coroutine(name, url):
    print(name, requests.get(url))

loop = asyncio.get_event_loop()

loop.run_until_complete(requests_coroutine("a", "http://www.google.com"))

loop.close()

