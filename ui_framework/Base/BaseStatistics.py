# -*- coding: utf-8 -*-
# @Time       : 2019/5/28 13:10
# @Author     : Philly
# @File       : BaseStatistics.py
# @Description: 
import xlsxwriter
from ui_framework.Base.BaseElementEnum import Element
from ui_framework.Base.BaseExcel import OperateReport
from ui_framework.Base.BaseInit import destroy
from ui_framework.Base.BasePickle import *
from datetime import datetime


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

'''统计数据相关'''
def countInfo(**kwargs):
    _info = {}
    step = ""   # 操作步骤信息
    check_step = ""     # 检查点步骤信息

    for case in kwargs["testCase"]:
        step = step + case["info"] + "\n"

    if type(kwargs["testCheck"]) == list:   # 检查点为列表
        for check in kwargs["testCheck"]:
            check_step = check_step + check["info"] + "\n"
    elif type(kwargs["testCheck"]) == dict:
        check_step = kwargs["testCheck"]["info"]
    else:
        print("获取 检查点步骤数据错误，请检查")
        print(kwargs["testCheck"])

    _info["step"] = step    # 用例操作步骤
    _info["checkStep"] = check_step     # 用例检查点

    if kwargs["result"]:
        _info["result"] = "通过"
        kwargs["logTest"].checkPointOK(driver=kwargs["driver"], caseName=kwargs["testInfo"][0]["title"],
                                       checkPoint=kwargs["caseName"] + "_" + kwargs["testInfo"][0].get(
                                           "msg", " "))
    else:
        _info["result"] = "失败"
        _info["img"] = kwargs["logTest"].checkPointNG(driver=kwargs["driver"], caseName=kwargs["testInfo"][0]["title"],
                                                      checkPoint=kwargs["caseName"] + "_" + kwargs["testInfo"][0].get(
                                                          "msg", " "))
    _info["id"] = kwargs["testInfo"][0]["id"]   # 用例id
    _info["title"] = kwargs["testInfo"][0]["title"]   # 用例名称
    _info["caseName"] = kwargs["caseName"]   # 测试函数
    _info["name"] = kwargs["name"]   # 设备名
    # 如果get()错误写成get[]，会报错 TypeError: 'builtin_function_or_method' object is not subscriptable
    _info["msg"] = kwargs["testInfo"][0].get("msg", "")   # 备注
    _info["info"] = kwargs["testInfo"][0]["info"]   # 前置条件

    writeInfo(data=_info, path=PATH("../Log/" + Element.INFO_FILE))


# 统计所有用例数
def countSum(result):
    data = {"sum": 0, "pass": 0, "fail": 0}
    _read = read(PATH("../Log/sum.pickle"))
    if _read:
        data = _read
    data["sum"] += 1
    if result:
        data["pass"] += 1
    else:
        data["fail"] += 1
    write(data=data, path=PATH("../Log/" + Element.SUM_FILE))


def countDate(testDate, testSumDate):
    data = read(PATH("../Log/" + Element.SUM_FILE))
    if data:
        data["testDate"] = testDate
        data["testSumDate"] = testSumDate
        write(data=data, path=PATH("../Log/" + Element.SUM_FILE))
    else:
        print("统计数据失败")
    data = read(PATH("../Log/" + Element.SUM_FILE))
    print("==统计数据： %s==" % data)


'''测试报告'''
def writeExcel():
    workbook = xlsxwriter.Workbook(PATH('../Report/' + Element.REPORT_FILE))
    worksheet = workbook.add_worksheet("测试总况")
    worksheet2 = workbook.add_worksheet("测试详情")
    operateReport = OperateReport(workbook)
    operateReport.init(worksheet, read(PATH("../Log/" + Element.SUM_FILE)))
    operateReport.detail(worksheet2, readInfo(PATH("../Log/" + Element.INFO_FILE)))
    operateReport.close()


if __name__ == '__main__':
    writeExcel()











