import json
import os
from typing import Union, Tuple, List, Dict

from .encoder import DecimalEncoder


def loads(json_str: str):
    """
    将json字符串加载为python对象
    :return:
    """
    return json.loads(json_str)


def dumps(py_obj):
    """
    将python对象转换为json字符串
    :param py_obj:
    :return:
    """
    return json.dumps(py_obj, cls=DecimalEncoder)


def load(file_name: str):
    """
    加载文件数据
    :param file_name:
    :return:
    """
    data = None
    with open(file_name, "r", encoding="UTF-8") as f:
        data = json.load(f)
    return data


def dump(file_name: str, data):
    """
    写入文件数据
    :param file_name:
    :return:
    """
    with open(file_name, "w+", encoding="UTF-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


class Json:
    def __init__(self,
                 config: str = "config/config.json",
                 config_secret: str = "config/secret/.config.json"
                 ):
        """
        初始化json对象
        :param config:公开的配置文件
        :param config_secret: 私密的配置文件
        """
        self.__data = None
        self.__config_file = config
        self.__config_secret_file = config_secret
        self.config = {}  # 配置信息
        self.__init_config()  # 初始化配置

    def __init_config(self):
        """
        初始化配置
        :return:
        """
        # 读取公共配置
        if os.path.exists(self.__config_file):
            with open(self.__config_file, "r") as f:
                config = json.load(f)
                self.config.update(config)

        # 读取私密配置
        if os.path.exists(self.__config_secret_file):
            with open(self.__config_secret_file, "r") as f:
                config = json.load(f)
                self.config.update(config)

    def set(self, data):
        self.__data = data

    def __read_config(self, config: str):
        """
        读取单个配置文件
        :param config: 配置文件
        :return:
        """
        if os.path.exists(config):
            with open(config, "r") as f:
                c = json.load(f)
                self.config.update(c)

    def read_config(self, config: Union[str, List, Tuple]):
        """
        读取配置
        :return:
        """
        # 读取单个文件
        if isinstance(config, str):
            self.__read_config(config)
        # 读取多个文件
        elif isinstance(config, tuple) or isinstance(config, list):
            for c in config:
                self.__read_config(c)

    def save_config(self, config: str = "config/zdppy_json_config.json"):
        """
        保存配置
        :param config:配置文件名称
        :return:
        """
        with open(config, "w") as f:
            json.dump(f, self.config, ensure_ascii=False)

    def update_config(self, config: Union[Dict, str, List, Tuple]):
        """
        更新配置
        :param config:配置文件信息
        :return:
        """
        if isinstance(config, dict):
            self.config.update(config)
        else:
            self.read_config(config)

    def __str__(self):
        return json.dumps(self.config)
