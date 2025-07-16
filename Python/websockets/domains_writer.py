#!/usr/bin/env python3

import asyncio
import os
from websockets.asyncio.client import connect
from websockets.exceptions import ConnectionClosedError

async def main():
    username = os.environ['username']
    password = os.environ['password']
    while True:
        exit_code = await run_stream(username, password)
        if exit_code == -1:
            break
        await asyncio.sleep(5)

async def run_stream(username, password):
    async with connect(f"wss://{username}:{password}@api.domainsproject.org/ws/domain_stream") as websocket:
        while True:
            try:
                message = await websocket.recv()
                print(message)
            except KeyboardInterrupt:
                return -1
            except ConnectionClosedError:
                break
    return 0

if __name__ == '__main__':
    asyncio.run(main())
