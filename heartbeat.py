import asyncio
import json
import opcodes

_HEARTBEAT_DATA = json.dumps({opcodes.key: opcodes.HEARTBEAT})


class Heartbeat:
    def __init__(self, gateway, interval_ms):
        self._gateway = gateway
        self._interval_sec = interval_ms / 1000
        self._next_beat = asyncio.get_event_loop().create_task(
            self._scheduled_send())

    async def _scheduled_send(self):
        await asyncio.sleep(self._interval_sec)
        await self.fire()
        self._next_beat = asyncio.get_event_loop().create_task(
            self._scheduled_send())

    async def fire(self):
        await self._gateway.send(_HEARTBEAT_DATA)
        
    async def ack(self):
        pass
