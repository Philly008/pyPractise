# -*- coding: utf-8 -*-
# @Time       : 2019/5/28 10:54
# @Author     : Philly
# @File       : BaseElementEnum.py
# @Description:


class Element(object):
    # selenium关键字
    find_element_by_id = "id"
    find_elements_by_id = "ids"
    INDEX = "index"
    find_elements_by_xpath = "xpaths"
    find_element_by_xpath = "xpath"
    find_element_by_css_selector = "css"
    find_element_by_class_name = "class_name"
    find_element_by_link_text = "link_text"
    CLICK = "click"
    DOUBLE_CLICK = "double_click"
    GET_TEXT = "get_text"
    SEND_KEYS = "send_keys"
    GET_VALUE = "get_value"
    WAIT_TIME = 20  # 查找元素等待时间
    MOVE_TO_ELEMENT = "move_to_element"  # 鼠标悬停
    DEFAULT_OPERATE = "default_operate"  # 默认值



    # 错误日志
    TIME_OUT = "timeout"
    NO_SUCH = "nosuch"
    WEB_DRIVER_EXCEPTION = "WebDriverException"
    INDEX_ERROR = "index_error"
    STALE_ELEMENT_REFERENCE_EXCEPTION = "StaleElementReferenceException"
    DEFAULT_ERROR = "default_error"

    # 检查点
    CONTRARY = "contrary"   # 相反检查点，表示如果检查元素存在就说明失败，如删除后，元素依然存在
    CONTRARY_GETVAL = "contrary_getval"  # 检查点关键字contrary_getval: 相反值检查点，如果对比成功，说明失败
    DEFAULT_CHECK = "default_check"  # 默认检查点，就是查找页面元素
    COMPARE = "compare"  # 历史数据和实际数据对比

    RE_CONNECT = 1  # 是否打开失败后再次运行一次用例

    # 文件名字
    INFO_FILE = "info.pickle"
    SUM_FILE = "sum.pickle"
    DEVICES_FILE = "devices.pickle"
    REPORT_FILE = "Report.xlsx"
