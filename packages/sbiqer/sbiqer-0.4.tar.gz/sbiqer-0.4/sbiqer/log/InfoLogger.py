"""
@ModuleName: InfoLogger
@Description: INFO日志类，负责各类INFO输出【如：各种result，中间提示等】
@Author: Beier
@Time: 2022/2/23 23:16
"""
from sbiqer.log.BaseLogger import BaseLogging


class InfoLogger(BaseLogging):
    def __init__(self, name):
        BaseLogging.__init__(self, name=name, level=BaseLogging.INFO)
