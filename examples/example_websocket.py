import asyncio
import json
import websockets

async def sinegy_ws():
    async with websockets.connect('wss://stream.sinegy.com/ws') as websocket:
        message = '''{
            "event": "subscribe",
            "channel": "book",
            "symbol": "btcmyr"
        }'''
        await websocket.send(message)

        while True:
            data = await websocket.recv()
            data = json.loads(data)
            print(data)

asyncio.get_event_loop().run_until_complete(sinegy_ws())
