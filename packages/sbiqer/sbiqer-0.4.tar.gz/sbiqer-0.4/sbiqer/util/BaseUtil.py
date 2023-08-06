"""
@ModuleName: BaseUtil
@Description: 工具包基础类，进行基础配置供子类调用
@Author: Beier
@Time: 2022/2/23 22:47
"""

import os
from sbiqer import config as pc
from ruamel import yaml
import json


class BaseUtil:
    def __init__(self):
        f_r_config = open(pc.CONFIG_PATH + os.sep + "config.yaml", mode="r", encoding="utf-8")
        self.yaml = yaml.YAML()
        self.config = self.yaml.load(f_r_config)
        f_r_agent = open(pc.CONFIG_PATH + os.sep + "user_agent.json", mode="r", encoding="utf-8")
        self.user_agent = json.load(f_r_agent)

    def _update_config(self, key: str, value):
        if key in self.config:
            f_w = open(pc.CONFIG_PATH + os.sep + "config.yaml", mode="w", encoding="utf-8")
            self.config[key] = value
            self.yaml.dump(data=self.config, stream=f_w)
        else:
            from sbiqer.exception.ConfigException import ConfigException
            raise ConfigException(f"config file update fail with do not find the key：{key}")
