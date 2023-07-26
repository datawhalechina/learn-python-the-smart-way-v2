import asyncio
import time

import blivedm

# 直播间ID的取值看直播间URL
TEST_ROOM_IDS = [
    # 21482458, # Datawhale
    25933362, # Epsilon Luoo
]


async def main():
    await run_multi_clients()

async def run_multi_clients():
    """
    演示同时监听多个直播间
    """
    clients = [blivedm.BLiveClient(room_id) for room_id in TEST_ROOM_IDS]
    handler = MyHandler()
    for client in clients:
        client.add_handler(handler)
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
    async def _on_danmaku(self, client: blivedm.BLiveClient, message: blivedm.DanmakuMessage):
        with open(f"./bilibili/danmu/danmu_{time.strftime('%Y-%m-%d', time.localtime())}.md", "a", encoding="utf-8") as f:
            if client.room_id == 21482458:
                print(f'- [ ] {message.msg} => [Datawhle]: {message.uname}', file=f)
            elif client.room_id == 25933362:
                print(f'- [ ] {message.msg} => [Luoo]: {message.uname}', file=f)
            else:
                print(f'- [ ] {message.msg} => [Other]: {message.uname}', file=f)

if __name__ == '__main__':
    asyncio.run(main())