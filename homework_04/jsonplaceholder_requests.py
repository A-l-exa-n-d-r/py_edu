"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio
import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(url: str) -> dict:
    async with aiohttp.ClientSession() as url_session:
        async with url_session.get(url, ssl=False) as req:
            return await req.json()


async def get_tuple_data() -> tuple:
    req = await asyncio.gather(fetch_json(USERS_DATA_URL),
                               fetch_json(POSTS_DATA_URL)
                               )
    return tuple(req)
