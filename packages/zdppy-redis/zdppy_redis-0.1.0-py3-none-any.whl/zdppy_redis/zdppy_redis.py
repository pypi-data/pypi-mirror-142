import json
from typing import Dict, Union, Tuple, List

from zdppy_log import Log

import redis


class Redis:
    def __init__(self,
                 host: str = "localhost",
                 port: int = 6379,
                 database: int = 0,
                 decode_responses: bool = True,
                 encoding: str = "utf-8",
                 max_connections: int = 10,
                 log_file_path: str = "logs/zdppy/zdppy_log.log",
                 config: Dict = {},
                 config_secret: Dict = {}
                 ):
        """
        创建Redis核心对象
        :param host: redis主机地址
        :param port: redis端口号
        :param database: redis数据库
        :param decode_responses: 是否解析响应
        :param encoding: 编码格式
        :param max_connections: 最大连接数
        :param log_file_path: 日志路径
        :param config: 配置信息
        :param config_secret: 私密配置信息
        """
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

        # 配置对象
        self.config = {}
        self.config.update(config)
        self.config.update(config_secret)

    def update_config(self, config: Union[Dict, str, List, Tuple]):
        """
        读取配置信息
        :param config:配置对象
        :return:
        """
        # 配置对象本身是一个字典
        if isinstance(config, dict):
            self.config.update(config)

        # 配置对象是redis的key
        elif isinstance(config, str):
            c = json.loads(self.get(config))
            if isinstance(c, dict):
                self.config.update(c)
                self.log.info(f"更新配置成功：{c}")
            else:
                self.log.error(f"更新配置失败，{config}不是字典类型：{c}")

        # 配置对象是redis的key列表
        elif isinstance(config, list) or isinstance(config, tuple):
            for cl in config:
                c = json.loads(self.get(cl))
                if isinstance(c, dict):
                    self.config.update(c)
                    self.log.info(f"更新配置成功：{c}")
                else:
                    self.log.error(f"更新配置失败，{cl}不是字典类型：{c}")

    def save_config(self, config="zdppy_redis_config"):
        """
        保存配置
        :param config: 配置的redis的key
        :return:
        """
        self.set(config, json.dumps(self.config))

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
            self.pool = redis.ConnectionPool.from_url(url, encoding=self.encoding,
                                                      decode_responses=self.decode_responses,
                                                      max_connections=self.max_connections)
            self.log.info("与redis建立连接成功")

        db = redis.Redis(connection_pool=self.pool)
        return db

    def set(self, key, value, expire=60 * 60 * 30):
        """
        设置值
        :param key:
        :param value:
        :return:
        """
        # 设置值
        db = self.get_db()
        db.set(key, value, px=expire)

    def get(self, key):
        """
        获取值
        :param key:
        :return:
        """
        # 获取值
        db = self.get_db()
        return db.get(key)

    def mset(self, kv_dict):
        """
        设置值
        :param key:
        :param value:
        :return:
        """
        # 设置值
        db = self.get_db()
        db.mset(kv_dict)

    def mget(self, *keys):
        """
        获取值
        :param key:
        :return:
        """
        # 获取值
        db = self.get_db()
        return db.mget(*keys)

    def incr(self, key, amount=1):
        """
        获取值
        :param key:
        :return:
        """
        # 获取值
        db = self.get_db()
        return db.incr(key, amount=amount)

    def incrbyfloat(self, key, amount=1.0):
        """
        获取值
        :param key:
        :return:
        """
        # 获取值
        db = self.get_db()
        return db.incrbyfloat(key, amount=amount)

    async def delete(self, *keys):
        """
        删除key
        :param key:
        :return:
        """
        # 获取值
        db = self.get_db()
        return await db.delete(*keys)

    def hset(self, key, value):
        """
        设置hash内容
        :return:
        """
        # 设置hash内容
        db = self.get_db()
        db.hset(key, mapping=value)

    def hgetall(self, key):
        """
        获取hash所有内容
        :param key:
        :return:
        """
        db = self.get_db()
        return db.hgetall(key)

    async def close(self):
        if self.pool is not None:
            await self.pool.disconnect()
