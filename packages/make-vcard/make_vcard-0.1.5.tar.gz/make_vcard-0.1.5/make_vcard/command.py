import sys
import argparse

import openpyxl

from make_vcard import make_vcard




def arguments_parse():
    parser = argparse.ArgumentParser(prog="make_vcard",
                                    description="基本用法 python -m make_vcard inputFileName.xlsx outputFileName",
                                    epilog="该程序目前只支持字段：姓名、电话、邮箱、备注",
                                    )
    parser.add_argument("--example", action="store_true", help="生成示例execl文件；")
    parser.add_argument("--sheet", type=str, help="指定读取哪张表；默认为当前表")
    
    parser.add_argument("inputFileName", default="", type=str, help="指定读取的xlsx文件；仅支持xlsx格式文件")
    parser.add_argument("outputFileName", type=str, default="", help="输出保存的文件名；不需要加后缀！")
    return parser.parse_args()



def example():
    execl = openpyxl.Workbook()
    sheet = execl.active
    sheet["A1"] = "姓名"
    sheet["A2"] = "张三"
    sheet["B1"] = "电话"
    sheet["B2"] = "1301008611"
    sheet["C1"] = "备注"
    sheet["C2"] = "备注备注备注备注备注备注备注备注备注备注备注备注"
    sheet["D1"] = "邮箱"
    sheet["D2"] = "123@456.com"
    execl.save("example.xlsx")
    print("示例文件已成功生成。")
    return 0


def cmd():
    if len(sys.argv) == 2 and sys.argv[1] == "--example":
        sys.exit(example())
    args = arguments_parse()
    make_vcard(args.inputFileName, args.outputFileName)