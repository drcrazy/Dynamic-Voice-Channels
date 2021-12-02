import asyncio
import json
import os
import uuid


class JSON:
    def __init__(self, path, *, loop=None):
        self.path = path
        self.loop = loop or asyncio.get_event_loop()
        self.lock = asyncio.Lock()

    def load(self, default):
        try:
            with open(self.path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return default

    async def save(self):
        async with self.lock:
            await self.loop.run_in_executor(None, self._dump)

    def copy(self):
        raise NotImplementedError()

    def _dump(self):
        temp = f'{self.path}-{uuid.uuid4()}.tmp'
        with open(temp, 'w', encoding='utf-8') as tmp:
            json.dump(self.copy(), tmp, ensure_ascii=True, separators=(',', ':'))
        os.replace(temp, self.path)


class JSONList(list, JSON):
    def __init__(self, path, *, loop=None):
        JSON.__init__(self, path, loop=loop)
        list.__init__(self, self.load([]))


class JSONDict(dict, JSON):
    def __init__(self, path, *, loop=None):
        JSON.__init__(self, path, loop=loop)
        dict.__init__(self, self.load({}))
