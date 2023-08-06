import ujson
import orjson
import asyncio
from threading import Lock
from io import TextIOWrapper
from os import name as os_name
from collections import OrderedDict

try:
    if os_name != "nt":
        import uvloop

        uvloop.install()
except ModuleNotFoundError:
    pass


class LruDict:
    def __init__(self, capacity: int):
        if type(capacity) != int:
            raise ValueError("Capacity must be an integer!")
        self.capacity = capacity
        self.dic = OrderedDict()

    def changecapacity(self, capacity: int):
        if type(capacity) != int:
            raise ValueError("Capacity must be an integer!")
        if capacity < self.capacity:
            while capacity < len(self.dic):
                self.dic.popitem(last=False)

        self.capacity = capacity

    def get(self, key, default=None):
        if key not in self.dic:
            return default
        else:
            self.dic.move_to_end(key)
            return self.dic[key]

    def put(self, key, value):
        self.dic[key] = value
        if len(self.dic) > self.capacity:
            self.dic.popitem(last=False)


gcache: LruDict = None

files = {}


def setcache(*, on=False, capacity=100):
    global gcache
    if on:
        if gcache is None:
            gcache = LruDict(capacity)
        else:
            gcache.changecapacity(capacity)
    else:
        gcache = None


def resetcache():
    if gcache is not None:
        gcache.dic.clear()


def get_lock(file_name):
    lock = files.get(file_name)
    if lock is None:
        lock = Lock()
        files[file_name] = lock
    return lock


def dumps(data):
    return orjson.dumps(data)


def loads(data):
    return orjson.loads(data)


async def dump(data, fp: TextIOWrapper, indent=None):
    if not isinstance(fp, TextIOWrapper):
        raise ValueError("FP should be a instance TextIOWrapper")
    lock = get_lock(fp.name)

    def dumper():
        with lock:
            if indent is None:
                with open(fp.name, "wb") as lol:
                    string = orjson.dumps(data)
                    lol.write(string)
            else:
                ujson.dump(data, fp, indent=indent)

    if gcache is not None:
        gcache.put(fp.name, data)
    return await asyncio.get_running_loop().run_in_executor(None, dumper)


async def load(fp: TextIOWrapper):
    if not isinstance(fp, TextIOWrapper):
        raise ValueError("FP should be an instance of TextIOWrapper")

    lock = get_lock(fp.name)

    def loader():
        with lock:
            return orjson.loads(fp.read())

    if gcache is not None:
        fromcache = gcache.get(fp.name)
        if fromcache is not None:
            return fromcache

    data = await asyncio.get_running_loop().run_in_executor(None, loader)
    if gcache is not None:
        gcache.put(fp.name, data)

    return data


async def open_and_dump(data, file_name, indent=None):
    def dumper():
        lock = get_lock(file_name)
        with lock:
            if indent is None:
                with open(file_name, "wb") as f:
                    string = orjson.dumps(data)
                    f.write(string)
            elif type(indent) == int:
                with open(file_name, "w") as f:
                    ujson.dump(data, f, indent=indent)
            else:
                raise ValueError("Value should be an integer")

    if gcache is not None:
        gcache.put(file_name, data)

    return await asyncio.get_running_loop().run_in_executor(None, dumper)


async def open_and_load(file_name):

    lock = get_lock(file_name)

    def loader():
        with lock:
            with open(file_name, "r") as f:
                return orjson.loads(f.read())

    if gcache is not None:
        fromcache = gcache.get(file_name)
        if fromcache is not None:
            return fromcache

    data = await asyncio.get_running_loop().run_in_executor(None, loader)
    if gcache is not None:
        gcache.put(file_name, data)

    return data
