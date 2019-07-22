# -*- coding: utf-8 -*-
# @Time       : 2019/5/29 10:07
# @Author     : Philly
# @File       : BaseOperate.py
# @Description: 
from selenium.webdriver.support.ui import WebDriverWait
import selenium.common.exceptions
from ui_framework.Base.BaseElementEnum import Element as be
from selenium.webdriver.common.action_chains import *
import time
import re


class OperateElement:
    def __init__(self, driver=""):
        self.driver = driver

    def findElement(self, operate):
        '''
        查找元素 operate, dict | list
        operate_type: 对应的操作
        element_info: 元素详情
        find_type: find 类型
        '''
        try:
            t = operate["check_time"] if operate.get("check_time",
                                                     "0") != "0" else be.WAIT_TIME
            if type(operate) == list:   # 多检查点
                for item in operate:
                    t = item["check_time"] if item.get("check_time", "0") != "0" else be.WAIT_TIME
                    WebDriverWait(self.driver, t).until(lambda x: self.elements_by(item))
                return {"result": True}
            if type(operate) == dict:   # 单检查点
                if operate.get("element_info", "0") == "0": # 如果没有页面元素，就不检测是页面元素
                    return {"result": True}
                WebDriverWait(self.driver, t).until(lambda x: self.elements_by(operate))
                return {"result": True}
        except selenium.common.exceptions.TimeoutException:
            return {"result": False, "type": be.TIME_OUT}
        except selenium.common.exceptions.NoSuchElementException:
            return {"result": False, "type": be.NO_SUCH}
        except selenium.common.exceptions.WebDriverException:
            return {"result": False, "type": be.WEB_DRIVER_EXCEPTION}

    '''
    查找元素 mOperate是字典：operate_type, element_info, find_type
    testInfo: 用例介绍
    logTest: 记录日志
    '''
    def operate(self, operate, testInfo, logTest):
        res = self.findElement(operate)
        if res["result"]:
            return self.operate_by(operate, testInfo, logTest)
        else:
            return res

    def operate_by(self, operate, testInfo, logTest):
        try:
            info = "%s_%s_%s_%s" % (
                operate.get("element_info", " "), operate.get("find_type"),
                operate.get("operate_type", " "), operate.get("msg", " ")
            )
            print("==操作步骤： %s==" % info)
            logTest.buildStartLine(testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + info)  # 记录日志

            if operate.get("operate_type", "0") == "0":  # 如果没有此字段，说明没有相应操作
                return {"result": True}
            elements = {
                be.CLICK: lambda: self.click(operate),
                be.DOUBLE_CLICK: lambda: self.double_click(operate),
                be.GET_VALUE: lambda: self.get_value(operate),
                be.GET_TEXT: lambda: self.get_text(operate),
                be.SEND_KEYS: lambda: self.send_keys(operate),
                be.MOVE_TO_ELEMENT: lambda: self.move_to_element(operate),
            }
            return elements[operate.get("operate_type")]()
        except IndexError:
            logTest.buildStartLine(
                testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + operate["element_info"] + "索引错误"
            )
            return {"result": False, "type": be.INDEX_ERROR}

        except selenium.common.exceptions.NoSuchElementException:
            logTest.buildStartLine(
                testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + operate[
                    "element_info"
                ] + "页面元素不存在或没加载完成"
            )
            return {"result": False, "type": be.NO_SUCH}

        except selenium.common.exceptions.StaleElementReferenceException:
            logTest.buildStartLine(
                testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + operate[
                    "element_info"
                ] + "页面元素已经变化"
            )
            return {"result": False, "type": be.STALE_ELEMENT_REFERENCE_EXCEPTION}
        except KeyError:
            # 如果key不存在，一般都是在自定义的page页面去处理
            return {"result": True}

    # 点击事件
    def click(self, operate):
        if operate["find_type"] == be.find_element_by_id or operate["find_type"] == be.find_element_by_xpath or \
                        operate["find_type"] == be.find_element_by_css_selector or operate["find_type"] == be.find_element_by_class_name or \
                        operate["find_type"] == be.find_element_by_link_text:
            self.elements_by(operate).click()
        elif operate.get("find_type") == be.find_elements_by_id:
            self.elements_by(operate)[operate["index"]].click()
        return {"result": True}

    # 双击
    def double_click(self, operate):
        if operate["find_type"] == be.find_element_by_id or operate["find_type"] == be.find_element_by_xpath or \
                        operate["find_type"] == be.find_element_by_css_selector or operate[
            "find_type"] == be.find_element_by_class_name or \
                        operate["find_type"] == be.find_element_by_link_text:
            ActionChains(self.driver).double_click(self.elements_by(operate)).perform()
        elif operate.get("find_type") == be.find_elements_by_id:
            ActionChains(self.driver).double_click(self.elements_by(operate)).perform()
        return {"result": True}

    def send_keys(self, operate):
        time.sleep(0.5)
        self.elements_by(operate).send_keys(operate["msg"])
        return {"result": True}

    def get_text(self, operate):
        if operate.get("find_type") == be.find_elements_by_id:
            element_info = self.elements_by(operate)[operate["index"]]
            result = element_info.get_attribute("text")
            re_result = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', result) # 只匹配中文，大小写字母
            return {"result": True, "text": "".join(re_result)}

        element_info = self.elements_by(operate)
        result = element_info.get_attribute("text")
        re_result = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', result)
        return {"result": True, "text": "".join(re_result)}

    def get_value(self, operate):
        if operate.get("find_type") == be.find_elements_by_id:
            element_info = self.elements_by(operate)[operate["index"]]
            result = element_info.get_attribute("text")
            re_result = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', result) # 只匹配中文，大小写字母
            return {"result": True, "text": "".join(re_result)}

        element_info = self.elements_by(operate)
        result = element_info.get_attribute("value")
        re_result = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', result)
        return {"result": True, "text": "".join(re_result)}

    # 鼠标悬停
    def move_to_element(self, operate):
        ActionChains(self.driver).move_to_element(self.elements_by(operate)).perform()
        return {"result": True}

    # 封装常用的标签
    def elements_by(self, operate):
        elements = {
            be.find_element_by_id: lambda: self.driver.find_element_by_id(operate["element_info"]),
            be.find_element_by_xpath: lambda: self.driver.find_element_by_xpath(operate["element_info"]),
            be.find_element_by_class_name: lambda: self.driver.find_element_by_class_name(operate["element_info"]),
            be.find_elements_by_id: lambda: self.driver.find_elements_by_id(operate["element_info"]),
            be.find_element_by_css_selector: lambda: self.driver.find_element_by_css_selector(operate["element_info"]),
            be.find_element_by_link_text: lambda: self.driver.find_element_by_link_text(operate["element_info"]),
        }
        return elements[operate["find_type"]]()








