# -*- coding: utf-8 -*-
# @Time       : 2018/12/18 14:42
# @Author     : Philly
# @File       : __init__.py.py
# @Description: Cross-browser Testing
"""
The Selenium standalone server is a component of Selenium
that provides the ability to run tests on remote machines.
RemoteWebDriver class

java -Dwebdriver.ie.driver="IEpath" -Dwebdriver.chrome.driver="chromepath"
-jar selenium-server-standalone.jar

# start a hub
java -jar selenium-server-standalone.jar -port 4444 -role hub

# start a hub node
java -Dwebdriver.ie.driver="iepath" -jar selenium-server-standalone.jar
-role webdriver -browser "browserName=internet explore, version=10,
maxinstance=1, platform=WINDOWS" -hubHost 192.168.1.1 -port 5555

# start a hub node from cfg.json
java -Dwebdriver.ie.driver="iepath" -jar selenium-server-standalone.jar
-role webdriver -nodeConfig selenium-node-win-ie10.cfg.json

# run test on the Windows and Chrome
python grid_test.py WINDOWS chrome
"""

