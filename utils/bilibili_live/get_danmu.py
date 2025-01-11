# 代码源自：https://github.com/xfgryujk/blivedm
import asyncio
import http.cookies
import random
from typing import *
import time
import aiohttp

import blivedm
import blivedm.models.web as web_models

# 直播间ID的取值看直播间URL
TEST_ROOM_IDS = [
    21482458, # Datawhale
    25933362, # Epsilon Luoo
]

# 这里填一个已登录账号的cookie的SESSDATA字段的值。不填也可以连接，但是收到弹幕的用户名会打码，UID会变成0
SESSDATA = ''

session: Optional[aiohttp.ClientSession] = None


async def main():
    init_session()
    try:
        await run_multi_clients()
    finally:
        await session.close()


def init_session():
    cookies = http.cookies.SimpleCookie()
    cookies['SESSDATA'] = SESSDATA
    cookies['SESSDATA']['domain'] = 'bilibili.com'

    global session
    session = aiohttp.ClientSession()
    session.cookie_jar.update_cookies(cookies)


async def run_multi_clients():
    """
    演示同时监听多个直播间
    """
    clients = [blivedm.BLiveClient(room_id, session=session) for room_id in TEST_ROOM_IDS]
    handler = MyHandler()
    for client in clients:
        client.set_handler(handler)
        client.start()

    try:
        await asyncio.gather(*(
            client.join() for client in clients
        ))
    finally:
        await asyncio.gather(*(
            client.stop_and_close() for client in clients
        ))


class MyHandler(blivedm.BaseHandler):
    def _on_danmaku(self, client: blivedm.BLiveClient, message: web_models.DanmakuMessage):
         with open(f"./bilibili/danmu/danmu_{time.strftime('%Y-%m-%d', time.localtime())}.md", "a", encoding="utf-8") as f:
            if client.room_id == 21482458:
                print(f'- [ ] {message.msg} => [Datawhle]: {message.uname}', file=f)
            elif client.room_id == 25933362:
                print(f'- [ ] {message.msg} => [Luoo]: {message.uname}', file=f)
            else:
                print(f'- [ ] {message.msg} => [Other]: {message.uname}', file=f)

if __name__ == '__main__':
    asyncio.run(main())