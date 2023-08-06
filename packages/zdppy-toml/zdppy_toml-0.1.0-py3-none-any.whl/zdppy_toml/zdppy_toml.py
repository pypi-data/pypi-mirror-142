#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/14 22:20
# @Author  : 张大鹏
# @Site    : 
# @File    : zdppy_toml.py
# @Software: PyCharm
import os
from typing import Union, List, Tuple, Dict

from .libs.toml import load, dump, loads, dumps


class Toml:
    def __init__(self,
                 config: str = "config/config.toml",
                 secret_config: str = "config/secret/.config.toml"
                 ):
        """
        toml配置对象
        :param config: 普通的配置文件 ，可以公开的
        :param secret_config: 私密的配置文件，不想要公开的
        """
        self.__config_file = config
        self.__secret_config_file = secret_config
        self.config = {}  # 配置对象
        self.__init_config()  # 初始化配置

    def __init_config(self):
        """
        初始化配置
        :return:
        """
        configs = []

        # 判断配置文件是否存在
        if os.path.exists(self.__config_file):
            configs.append(self.__config_file)
        if os.path.exists(self.__secret_config_file):
            configs.append(self.__secret_config_file)

        # 读取配置文件
        self.config = load(configs)

    def read_config(self, config: Union[str, List, Tuple]):
        """
        读取配置
        :param config 要读取的配置文件列表
        :return:
        """
        # 将元组转换为列表
        if isinstance(config, tuple):
            config = list(config)

        # 读取配置
        _config = load(config)

        # 更新到整体的配置中
        self.config.update(_config)

    def save_config(self, config="config/zdppy_toml_config.toml"):
        """
        保存配置
        :param config:要保存的配置文件名称
        :return:
        """
        with open(config, "w") as f:
            dump(self.config, f)

    def update_config(self, config: Union[Dict, str]):
        """
        更新配置
        :return:
        """
        # 如果是toml字符串，解析为字典
        if isinstance(config, str):
            config = loads(config)

        # 更新配置字典
        self.config.update(config)

    def __str__(self):
        return dumps(self.config)
