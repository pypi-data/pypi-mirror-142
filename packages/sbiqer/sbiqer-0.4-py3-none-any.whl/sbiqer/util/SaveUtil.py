"""
@ModuleName: SaveUtil
@Description: 保存工具类，暴露给用户进行调用
@Author: Beier
@Time: 2022/2/23 22:45
"""
from sbiqer.util.BaseUtil import BaseUtil
from sbiqer.util import ConfigLoader
# import config.PathConfig as pc

cl = ConfigLoader()


class SaveUtil(BaseUtil):
    def __init__(self):
        BaseUtil.__init__(self)

    def get_save_path(self):
        return cl.get_result_path()

    def set_save_path(self, path):
        self._update_config("result_path", path)
