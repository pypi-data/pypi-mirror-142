"""
@ModuleName: ErrorLogger
@Description: ERROR日志类，负责非自定义异常记录
@Author: Beier
@Time: 2022/2/23 23:16
"""
from sbiqer.log.BaseLogger import BaseLogging


class ErrorLogger(BaseLogging):
    def __init__(self):
        BaseLogging.__init__(self, name="error", level=BaseLogging.ERROR)
