# -*- coding: utf-8 -*-
# @Time       : 2019/5/28 14:51
# @Author     : Philly
# @File       : BaseLog.py
# @Description: 
import logging
import time
import os
from time import sleep
import threading


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Log:
    def __init__(self, name):
        phone_name = name
        global logger, resultPath, logPath
        resultPath = PATH("../Log")
        logPath = os.path.join(resultPath, (phone_name + time.strftime('%Y%m%d%H%M%S', time.localtime())))
        if not os.path.exists(logPath):
            os.makedirs(logPath)
        self.checkNo = 0
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        # 创建句柄写入log
        fh = logging.FileHandler(os.path.join(logPath, "output.log"))
        formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        self.logger.addHandler(fh)

    def getMyLogger(self):
        return self.logger

    def buildStartLine(self, caseNo):
        startLine = "---- " + caseNo + "   " + "   " + " ----"
        self.logger.info(startLine)

    def buildEndLine(self, caseNo):
        endLine = "---- " + caseNo + "   " + "END" + "   " + " ----"
        self.logger.info(endLine)
        self.checkNo = 0

    def writeResult(self, result):
        reportPath = os.path.join(logPath, "report.txt")
        flogging = open(reportPath, "a")
        try:
            flogging.write(result + "\n")
        finally:
            flogging.close()
        pass

    def resultOK(self, caseNo):
        self.writeResult(caseNo + ": OK")

    def resultNG(self, caseNo, reason):
        self.writeResult(caseNo + ": NG--" + reason)

    def checkPointOK(self, driver, caseName, checkPoint):
        self.checkNo += 1
        self.logger.info("[CheckPoint_" + str(self.checkNo) + "]:" + checkPoint + ": OK")
        print("==用例%s检查点成功==" % caseName)

    def checkPointNG(self, driver, caseName, checkPoint):
        self.checkNo += 1
        self.logger.info("[CheckPoint_" + str(self.checkNo) + "]: " + checkPoint + ": NG")
        return self.screenshotNG(driver, caseName)

    def screenshotOK(self, driver, caseName):
        screenshotPath = os.path.join(logPath, caseName)
        screenshotName = "CheckPoint_" + str(self.checkNo) + "_OK.png"
        sleep(1)
        driver.get_screenshot_as_file(os.path.join(screenshotPath + screenshotName))

    def screenshotNG(self, driver, caseName):
        screenshotPath = os.path.join(logPath, caseName)
        screenshotName = "CheckPoint_" + str(self.checkNo) + "_NG.png"
        sleep(1)
        driver.get_screenshot_as_file(os.path.join(screenshotPath + screenshotName))
        return os.path.join(screenshotPath + screenshotName)

    def screenshotERROR(self, driver, caseName):
        screenshotPath = os.path.join(logPath, caseName)
        screenshotName = "ERROR.png"
        sleep(1)
        driver.get_screenshot_as_file(os.path.join(screenshotPath + screenshotName))


class myLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def getLog(devices):
        if myLog.log is None:
            myLog.mutex.acquire()
            myLog.log = Log(devices)
            myLog.mutex.release()
        return myLog.log

if __name__ == '__main__':
    logTest = myLog.getLog("devices")
    logTest.buildStartLine("33333333")








