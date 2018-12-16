# -*- coding: utf-8 -*-
# @Time       : 2018/12/15 17:58
# @Author     : Philly
# @File       : chrome_open.py
# @Description: 
import os
from selenium import webdriver


# get the path of chromedriver
# dir = os.path.dirname(__file__)
# chrome_driver_path = dir + "\chromedriver.exe"
chrome_driver_path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(15)
driver.maximize_window()

# navigate to the application home page
driver.get("http://demo.magentocommerce.com")

# get the search textbox
search_field = driver.find_element_by_name("q")
search_field.clear()

# enter search keyword and submit
search_field.send_keys("phones")
search_field.submit()

# get all the anchor elements which have product names displayed
# currently on result page using find_elements_by_xpath method
products = driver.find_elements_by_xpath("")

# get the number of anchor elements found
print("Found " + str(len(products)) + " products:")

# iterate through each anchor element and print the text that is # name of the product
for product in products:
    print(product.text)

# close the browser window
driver.quit()
