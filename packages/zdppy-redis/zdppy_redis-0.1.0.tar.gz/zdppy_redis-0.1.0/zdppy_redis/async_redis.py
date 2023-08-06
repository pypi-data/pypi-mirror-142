#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/15 7:58
# @Author  : 张大鹏
# @Site    : 
# @File    : async_redis.py
# @Software: PyCharm
import aioredis
from zdppy_log import Log
from typing import Dict, Any
import asyncio
import async_timeout

class AsyncRedis:
    def __init__(self,
                 host: str = "localhost",
                 port: int = 6379,
                 database: int = 0,
                 decode_responses: bool = True,
                 encoding: str = "utf-8",
                 max_connections: int = 10,
                 log_file_path: str = "logs/zdppy/zdppy_log.log"):
        # 日志
        self.log = Log(log_file_path)

        # redis核心对象
        self.host = host
        self.port = port
        self.database = database
        self.decode_responses = decode_responses
        self.encoding = encoding
        self.max_connections = max_connections
        self.pool = None

    def get_db(self):
        """
        获取redis连接对象
        :return:
        """
        # 创建pool
        if self.pool is None:
            # 不存在则创建
            url = f"redis://{self.host}:{self.port}/{self.database}"
            self.log.info(f"尝试与redis建立连接：{url}")
            self.pool = aioredis.ConnectionPool.from_url(url, encoding=self.encoding,
                                                         decode_responses=self.decode_responses,
                                                         max_connections=self.max_connections)
            self.log.info("与redis建立连接成功")

        db = aioredis.Redis(connection_pool=self.pool)
        return db

    async def set(self, key, value, expire=60 * 60 * 30):
        """
        设置值
        :param key:
        :param value:
        :return:
        """
        # 设置值
        db = self.get_db()
        await db.set(key, value, px=expire)

    async def get(self, key):
        """
        获取值
        :param key:
        :return:
        """
        # 获取值
        db = self.get_db()
        return await db.get(key)

    async def mset(self, kv_dict):
        """
        设置值
        :param key:
        :param value:
        :return:
        """
        # 设置值
        db = self.get_db()
        await db.mset(kv_dict)

    async def mget(self, *keys):
        """
        获取值
        :param key:
        :return:
        """
        # 获取值
        db = self.get_db()
        return await db.mget(*keys)

    async def incr(self, key, amount=1):
        """
        获取值
        :param key:
        :return:
        """
        # 获取值
        db = self.get_db()
        return await db.incr(key, amount=amount)

    async def incrbyfloat(self, key, amount=1.0):
        """
        获取值
        :param key:
        :return:
        """
        # 获取值
        db = self.get_db()
        return await db.incrbyfloat(key, amount=amount)

    async def delete(self, *keys):
        """
        删除key
        :param key:
        :return:
        """
        # 获取值
        db = self.get_db()
        return await db.delete(*keys)

    async def hset(self, key, value):
        """
        设置hash内容
        :return:
        """
        # 设置hash内容
        db = self.get_db()
        await db.hset(key, mapping=value)

    async def hgetall(self, key):
        """
        获取hash所有内容
        :param key:
        :return:
        """
        db = self.get_db()
        return await db.hgetall(key)

    async def close(self):
        if self.pool is not None:
            await self.pool.disconnect()
