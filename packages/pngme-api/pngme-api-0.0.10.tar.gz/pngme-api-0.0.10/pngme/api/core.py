import asyncio
from abc import ABC
from contextlib import asynccontextmanager
from typing import AsyncGenerator, Coroutine, TypeVar

import httpx
import nest_asyncio

nest_asyncio.apply()


T = TypeVar("T")


DEFAULT_BASE_URL = "https://api.pngme.com/beta"


class BaseClient(ABC):
    def __init__(
        self,
        access_token: str,
        concurrency_limit: int = 50,
        base_url: str = DEFAULT_BASE_URL,
    ):
        """Client SDK to interact with Pngme financial report resources.

        Args:
            access_token: API key from https://admin.pngme.com
            concurrency_limit: maximum allowed concurrent API requests
            base_url: root url for API resources
        """
        self.access_token = access_token
        self.concurrency_limit = concurrency_limit
        self.base_url = base_url

        try:
            self.loop = asyncio.get_running_loop()
        except RuntimeError:
            self.loop = asyncio.new_event_loop()

        self.semaphore = asyncio.Semaphore(concurrency_limit)

    def run(self, coroutine: Coroutine[None, None, T]) -> T:
        """Run coroutine in managed event loop."""
        return self.loop.run_until_complete(coroutine)

    @asynccontextmanager
    async def session(self) -> AsyncGenerator[httpx.AsyncClient, None]:
        """Configure connection and concurrency settings."""
        headers = {"Authorization": f"Bearer {self.access_token}"}
        transport = httpx.AsyncHTTPTransport(retries=10)

        async with self.semaphore:
            async with httpx.AsyncClient(
                base_url=self.base_url,
                headers=headers,
                timeout=30,
                transport=transport,
            ) as session:
                yield session
