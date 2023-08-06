"""
@ModuleName: SbiqerException
@Description: 基础异常类
@Author: Beier
@Time: 2022/2/23 23:00
"""
from sbiqer.log.BaseLogger import BaseLogging


class SbiqerException(Exception):
    def __init__(self, message):
        logger = BaseLogging("exception", BaseLogging.ERROR).get_logger()
        logger.error(message)
        # print(message)
