# https://blog.csdn.net/luzeqiang/article/details/7616893
# https://blog.csdn.net/mingliuboy/article/details/6743703
# https://blog.csdn.net/zjx2014430/article/details/41548991

# https://www.cnblogs.com/LXP-Never/p/11093896.html
# https://docs.python.org/zh-cn/3/library/argparse.html

from .globals import SHEET
from .generate_vcard import Vcard, VcardFile, make_vcard
from .read_file import read_file_xlsx_data

__all__ = [
    "SHEET",
    "Vcard",
    "VcardFile",
    "read_file_xlsx_data",
    "make_vcard",
]


__name__ = "make_vcard"
__author__ = "antianshi"
__version__ = "0.1.5"

