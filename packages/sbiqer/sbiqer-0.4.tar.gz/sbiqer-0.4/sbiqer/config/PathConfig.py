import os
import platform

"""
@ModuleName: PathConfig
@Description: 基础路径以及系统相关信息保存文件
@Author: Beier
@Time: 2022/2/23 22:47
"""
#
# # 这个方法可以获取相关系统环境，可以使用这个方法配置保存路径，但是需要注意linux下的环境key和window下的key是不一样的，需要分系统
# for i in os.environ.keys():
#     print(i + "：" + os.environ[i])
# 操作系统
PLATFORM = platform.system()
# HOME路径
if PLATFORM == "Windows":
    HOME_PATH = os.environ["USERPROFILE"]
else:
    HOME_PATH = os.environ["HOME"]
import sbiqer
# print(HOME_PATH)
# 根路径
ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
# 配置项路径
CONFIG_PATH = ROOT_PATH + os.sep + "config"
# 工具类路径
UTIL_PATH = ROOT_PATH + os.sep + "util"
# 实体类路径
ENTITY_PATH = ROOT_PATH + os.sep + "entity"
# 异常类路径
EXCEPTION_PATH = ROOT_PATH + os.sep + "exception"
# 日志路径
LOGGING_PATH = ROOT_PATH + os.sep + "log"
# js逆向类路径
JS_PATH = ROOT_PATH + os.sep + "js"
# 请求器路径
REQUESTER_PATH = ROOT_PATH + os.sep + "requester"
# 解析器路径
PARSER_PATH = ROOT_PATH + os.sep + "parser"
# 时刻表路径（用于服务器部署）
SCHEDULE_PATH = ROOT_PATH + os.sep + "schedule"
# print(SCHEDULE_PATH)
# 默认结果保存路径
RESULT_PATH = ROOT_PATH + os.sep + "result"
