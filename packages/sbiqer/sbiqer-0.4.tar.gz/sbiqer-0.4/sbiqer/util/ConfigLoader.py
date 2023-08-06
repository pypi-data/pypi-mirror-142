"""
@ModuleName: ConfigLoader
@Description: 配置加载器，用于加载config.json配置项
@Author: Beier
@Time: 2022/2/23 22:46
"""

from sbiqer.util.BaseUtil import BaseUtil
from sbiqer import config as pc
import random
import os
import json


class ConfigLoader(BaseUtil):
    IOS = 1
    WEB = 2
    ANDROID = 3

    def __init__(self):
        BaseUtil.__init__(self)

    def get_log_path(self):
        '''
        :return: 如果config.yaml文件中log_path属性非空字符串，即返回相应路径，若为空字符串，返回默认路径
        '''
        return pc.LOGGING_PATH if self.config["log_path"] == "" else self.config["log_path"]

    def get_result_path(self):
        return pc.RESULT_PATH if self.config["result_path"] == "" else self.config["result_path"]

    def get_random_agent(self, platform: int):
        """

        :param platform: 平台，具体种类见类属性
        :return: 根据所给的平台返回相应的user-agent
        """
        if platform == self.IOS:
            return random.choice(self.user_agent["user_Agent_ios"])
        elif platform == self.WEB:
            return random.choice(self.user_agent["user_Agent_web"])
        elif platform == self.ANDROID:
            return random.choice(self.user_agent["user_Agent_android"])
        else:
            from sbiqer.exception.ConfigException import ConfigException
            raise ConfigException("error user-Agent key.")

    def get_random_cookie(self, cookie_pool_path: str):
        from sbiqer.exception.ConfigException import ConfigException
        '''
        根据给出的cookie池文件路径，读取cookie池，并随机返回
        :param cookie_pool_path: 该路径底部文件需是json文件
        :return: 随机从cookie池中抽取一个
        '''
        if os.path.splitext(cookie_pool_path)[-1] != ".json":
            raise ConfigException("can not find a json file as cookie pool")
        else:
            f_r = open(cookie_pool_path, "r", encoding="utf-8")
            cookie_json = json.load(f_r)
            if "cookie_pool" not in cookie_json or type(cookie_json["cookie_pool"]) != list:
                raise ConfigException("check your cookie_pool file format according to document: https://www.baidu.com/")
            else:
                return random.choice(cookie_json["cookie_pool"])


if __name__ == '__main__':
    cl = ConfigLoader()
    print(cl.get_random_cookie(r"D:\pycharm\PyCharm 2020.1.1\workplace\sbiqer\config\cookie_pool.json"))
