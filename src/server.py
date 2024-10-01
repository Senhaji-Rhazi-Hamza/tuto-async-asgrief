from sanic import Sanic, text
from asgiref.sync import sync_to_async

import time
import asyncio

app = Sanic("app")


async def async_wait_task():
    print("Start async wait_task")
    await asyncio.sleep(1)  # Non-blocking, event loop is free to run other tasks
    print("Finish async wait_task")


def wait_task():
    print("Start wait_task")
    time.sleep(1)
    print("Finish wait_task")


@app.get("/task")
def task(request):
    wait_task()
    return text("")


@app.get("/async_task")
async def async_task(request):
    await async_wait_task()
    return text("")


@app.get("/asgiref_task")
async def task_asgrief(request):
    await sync_to_async(thread_sensitive=False)(wait_task)()
    return text("")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
