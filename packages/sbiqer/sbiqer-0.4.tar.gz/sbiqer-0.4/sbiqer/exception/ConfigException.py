"""
@ModuleName: ConfigException
@Description: 配置异常类
@Author: Beier
@Time: 2022/2/23 23:02
"""
from sbiqer.exception.SbiqerException import SbiqerException


class ConfigException(SbiqerException):
    def __init__(self, message):
        SbiqerException.__init__(self, message)
