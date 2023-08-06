from typing import Callable, List
from exceptions import BadStatusException


import aiohttp
import asyncio 
import time
import functools
import logging


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s: %(levelname)s: %(message)s"
)


class Fetch():
    
    def __init__(self, reqs_per_sec, data, show_results=True):
        self._semaphore = asyncio.Semaphore(reqs_per_sec)
        self.data = data # define data to later use it with parser func
        self.show_results = show_results
        

    async def _http_request(self, url: str, method: str) -> aiohttp.ClientResponse.text:
        async with self._semaphore:
            response = await self.session.request(
                method=method, 
                url=url
            )
            self._request_count += 1
            logging.info(f"Sending {method} request #{self._request_count} to endpoint {url}")
            # Rate limiting allow other func to run
            await asyncio.sleep(1)
            if response.ok:
                return await response.text()
            else:
                logging.info("Raised Error: BadStatusException")
                raise BadStatusException(f'Bad Status: Recieved {response.status}')
    

    async def _master_req(self, urls: List[str], method: str, parse_func: Callable) -> List[str]:

        self._request_count = 0

        async with aiohttp.ClientSession() as session:
            self.session = session

            tasks_map = {
                asyncio.ensure_future(
                    self._http_request(url, method)
                ): functools.partial(self._http_request, url, method)
                for url in urls
            }

            pending_tasks = set(tasks_map.keys())

            while pending_tasks:
                finished, pending_tasks = await asyncio.wait(
                    pending_tasks, return_when=asyncio.FIRST_EXCEPTION
                )  # --> finished tasks with results in task.result and pending tasks
                for task in finished:
                    if task.exception():
                        print(task.exception())
                        # pinpoint the coro that raised BadStatusException
                        coro = tasks_map[task]
                        new_task = asyncio.ensure_future(coro())
                        tasks_map[new_task] = coro
                        # append failed task to pending tasks
                        pending_tasks.add(new_task)
                    else:
                        parse_func(task.result())


    def __call__(self, urls: list, method: str, parse_func: Callable) -> List[str]:
        start = time.perf_counter()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._master_req(urls, method, parse_func))
        end = time.perf_counter(end - start)

    def __str__(self):
        return "Time taken to execute: {:.2f}".format()