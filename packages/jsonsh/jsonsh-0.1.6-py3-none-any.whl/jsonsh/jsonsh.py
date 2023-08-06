import os
import asyncio
from uuid import uuid4
from typing import List
from inspect import isclass
from pydantic import BaseModel
import jsonsh.aiojson as aiojson


class Instance:
    def __init__(self, folder, *, cache_state=False, cache_capacity=100):
        self.main_folder = folder
        aiojson.setcache(on=cache_state, capacity=cache_capacity)

    def setcache(self, on: bool, capacity: int):
        aiojson.setcache(on=on, capacity=capacity)

    async def file_list(self, dir) -> List[str]:
        def inner():
            try:
                lis = os.listdir(dir)
                return list(filter(lambda x: x.endswith(".json"), lis))
            except FileNotFoundError:
                return

        return await asyncio.get_running_loop().run_in_executor(None, inner)

    def match(self, details: dict, data: dict):
        for key, value in details.items():
            if key not in data:
                return False
            if value != data.get(key):
                return False
        return True

    def get_indexes(self, temp) -> List[str]:
        if hasattr(temp, "Meta"):
            if isclass(temp.Meta):
                if hasattr(temp.Meta, "indexes"):
                    if isinstance(temp.Meta.indexes, list):
                        try:
                            temp.Meta.indexes.remove("id")
                        except:
                            pass
                        for i in temp.Meta.indexes:
                            if not isinstance(i, str):
                                raise TypeError("Indexes must be of type str")

                        temp.Meta.indexes = ["id"] + temp.Meta.indexes
                        return temp.Meta.indexes

        return ["id"]

    def get_index_data(self, temp, details):
        indexes = self.get_indexes(temp)

        found = False

        for idx, index in enumerate(indexes):
            if index in details:
                found = True
                index = str(details[index])
                break

        return found, idx, index

    def register(self, temp):
        temp.__instance__ = self
        self.get_indexes(temp)
        return temp


class Template(BaseModel):
    __instance__ = None
    __cached_file_list__ = None

    @classmethod
    async def find_one(cls, get_with_file=False, **details: str):
        ins = cls.__instance__

        if ins is None:
            raise NotImplementedError("Instance is not yet registered")

        if not isinstance(get_with_file, bool):
            raise TypeError("get_with_file must be of type bool")

        if cls.__cached_file_list__ is None:
            cls.__cached_file_list__ = await ins.file_list(
                f"{ins.main_folder}/{cls.__name__}"
            )
        if cls.__cached_file_list__ is None:
            if get_with_file:
                return None, None
            return None

        found, idx, index = ins.get_index_data(cls, details)
        if found:
            for file in cls.__cached_file_list__:
                arr = file.strip(".json").split("-")
                try:
                    if arr[idx] == index:
                        data = await aiojson.open_and_load(
                            f"{ins.main_folder}/{cls.__name__}/{file}"
                        )
                        if ins.match(details, data):
                            if get_with_file:
                                return file, cls(**data)
                            return cls(**data)
                        else:
                            if get_with_file:
                                return None, None
                except IndexError:
                    pass
        for file in cls.__cached_file_list__:
            data = await aiojson.open_and_load(
                f"{ins.main_folder}/{cls.__name__}/{file}"
            )
            if ins.match(details, data):
                if get_with_file:
                    return file, cls(**data)
                return cls(**data)
        if get_with_file:
            return None, None
        return None

    @classmethod
    async def find_many(cls, deep_search: bool = False, **details: str):
        ins = cls.__instance__
        if ins is None:
            raise NotImplementedError("Instance is not yet registered")

        if cls.__cached_file_list__ is None:
            cls.__cached_file_list__ = await ins.file_list(
                f"{ins.main_folder}/{cls.__name__}"
            )

        results = []
        payloads = []

        if cls.__cached_file_list__ is None:
            return results

        if deep_search:
            for file in cls.__cached_file_list__:
                data = aiojson.open_and_load(f"{ins.main_folder}/{cls.__name__}/{file}")
                payloads.append(data)
        else:
            found, idx, index = ins.get_index_data(cls, details)
            if found:
                for file in cls.__cached_file_list__:
                    arr = file.strip(".json").split("-")
                    try:
                        if arr[idx] == index:
                            data = aiojson.open_and_load(
                                f"{ins.main_folder}/{cls.__name__}/{file}"
                            )
                            payloads.append(data)
                    except IndexError:
                        pass
            else:
                for file in cls.__cached_file_list__:
                    data = aiojson.open_and_load(
                        f"{ins.main_folder}/{cls.__name__}/{file}"
                    )
                    payloads.append(data)

        if payloads:
            payloads = await asyncio.gather(*payloads)
            for data in payloads:
                if ins.match(details, data):
                    results.append(cls(**data))
        return results

    @classmethod
    async def delete_one(cls, **details):
        ins = cls.__instance__
        if ins is None:
            raise NotImplementedError("Instance is not yet registered")
            
        file, _ = await cls.find_one(True, **details)
        if file is None:
            return 1
        try:
            cls.__cached_file_list__.remove(file)
        except:
            pass
        try:
            os.remove(f"{cls.__instance__.main_folder}/{cls.__name__}/{file}")
        except:
            return 0
        return 1

    async def save(self):
        ins = self.__instance__

        if ins is None:
            raise NotImplementedError("Instance is not yet registered")
        dic = self.dict()

        if not os.path.exists(f"{ins.main_folder}/{self.__class__.__name__}"):
            os.makedirs(f"{ins.main_folder}/{self.__class__.__name__}", exist_ok=True)

        id = dic.get("id", uuid4().hex)
        dic["id"] = id

        indexes = ins.get_indexes(self)

        file_name = "-".join([str(dic[i]) for i in indexes])

        if self.__class__.__cached_file_list__ is None:
            self.__class__.__cached_file_list__ = await ins.file_list(
                f"{ins.main_folder}/{self.__class__.__name__}"
            )

        if self.__class__.__cached_file_list__:
            for file in self.__cached_file_list__:
                arr = file.strip(".json").split("-")
                if len(arr) == 1 and len(indexes) == 1:
                    continue
                try:
                    if arr[0] == str(id):
                        await self.delete_one(id=id)
                except IndexError:
                    pass

        await aiojson.open_and_dump(
            dic,
            f"{ins.main_folder}/{self.__class__.__name__}/{file_name}.json",
            indent=4,
        )
        self.__class__.__cached_file_list__ = await ins.file_list(
            f"{ins.main_folder}/{self.__class__.__name__}"
        )

        return id
