# from exception.ConfigException import ConfigException
# from exception.SbiqerException import SbiqerException
# from log.BaseLogger import BaseLogging
# from log.ErrorLogger import ErrorLogger
import sys
from pprint import pprint

pprint(sys.builtin_module_names)
# save_util = SaveUtil()
# print(sys.argv)
# save_util.set_save_path("D:\pycharm\PyCharm 2020.1.1\workplace\sbiqer")
# a = 0
# b = 1
# try:
#     c = b / a
# except:
#     logger=ErrorLogger().get_logger()
#     logger.exception(traceback.print_exc())
# if a == 0:
#     raise SbiqerException("配置文件出错，请重新更改配置文件")

# import yaml
# import config.PathConfig as pc
# import os
# import json
#
# config = open(pc.CONFIG_PATH + os.sep + "config.yaml", mode="r", encoding="utf-8")
# config_json = open(pc.CONFIG_PATH + os.sep + "config.json", mode="r", encoding="utf-8")
# cfg = config.read()
# json_line = json.load(config_json)
# yaml_line = yaml.load(stream=cfg, Loader=yaml.FullLoader)
# print(type(yaml_line))
# print(type(json_line))
