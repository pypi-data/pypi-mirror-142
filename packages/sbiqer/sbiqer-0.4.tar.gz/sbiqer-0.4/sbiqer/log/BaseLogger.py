"""
@ModuleName: BaseLogger
@Description: 基础日志类，负责各类INFO输出【如：自定义异常日志等】，以及ERROR，WARNING，INFO日志类继承
@Author: Beier
@Time: 2022/2/23 23:15
"""
import logging
import os
from sbiqer.util import ConfigLoader

cl = ConfigLoader()


class BaseLogging:
    CRITICAL = logging.CRITICAL
    ERROR = logging.ERROR
    WARNING = logging.WARNING
    INFO = logging.INFO
    DEBUG = logging.DEBUG

    def __init__(self, name, level):
        logging.basicConfig(format="%(asctime)s - %(levelname)s: %(message)s",
                            datefmt="%Y-%m-%d %H:%M:%S",
                            level=level,
                            filemode='a')
        self.__logger = logging.getLogger(name)
        logging_formatter = logging.Formatter(fmt="%(asctime)s - %(levelname)s: %(message)s",
                                              datefmt='%Y-%m-%d %H:%M:%S')
        file_handler = logging.FileHandler(filename=cl.get_log_path() + os.sep + name + ".log", mode="a",
                                           encoding="utf-8")
        file_handler.setFormatter(logging_formatter)
        self.__logger.addHandler(file_handler)

    def get_logger(self):
        return self.__logger


if __name__ == '__main__':
    logger = BaseLogging("test", BaseLogging.INFO).get_logger()
    logger.error("测试")
