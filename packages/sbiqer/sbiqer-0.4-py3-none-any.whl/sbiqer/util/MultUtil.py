"""
@ModuleName: MultUtil
@Description: 杂项类，用来存放如进度条等无处安放的小插件，暂定内部组件皆为静态方法，以方便调用
@Author: Beier
@Time: 2022/2/23 22:44
"""


class MultUtil(object):
    # def __init__(self):
    #     pass

    @staticmethod
    def process_bar(percent, start_str='', end_str='', total_length=0):
        bar = '\r' + start_str + ''.ljust(int(percent * total_length), "=") + '> {:0>5.2f}%|'.format(
            percent * 100) + end_str
        print(bar, end='', flush=True)
