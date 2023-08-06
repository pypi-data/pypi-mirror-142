"""
@ModuleName: WarningLogger
@Description: WARNING日志类，负责各类WARNING输出【如：各类使用到的如requests库的内置WARNING等】
@Author: Beier
@Time: 2022/2/23 23:16
"""
from sbiqer.log.BaseLogger import BaseLogging


class WarningLogger(BaseLogging):
    def __init__(self):
        BaseLogging.__init__(self, name="warning", level=BaseLogging.WARNING)
