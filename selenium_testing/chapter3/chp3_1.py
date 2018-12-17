# -*- coding: utf-8 -*-
# @Time       : 2018/12/17 15:17
# @Author     : Philly
# @File       : chp3_1.py
# @Description:
import unittest
from selenium import webdriver

class HomePageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a new FireFox session
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

        # navigate to the application home page
        cls.driver.get('XXX')

    def test_search_text_field_max_length(self):
        # get the search textbox
        search_field = self.driver.find_element_by_id("")

        # check maxlength attribute is set to 128
        self.assertEqual('128', search_field.get_attribute("maxlength"))

    def test_search_button_enabled(self):
        # get Search buttong
        search_button = self.driver.find_element_by_class_name("")
        # check Search button is enabled
        self.assertTrue(search_button.is_displayed())

    def test_my_account_link_is_displayed(self):
        # get the Account link
        account_link = self.driver.find_element_by_link_text("")
        # check My Account link is displayed/visible in the Home page footer
        self.assertTrue(account_link.is_displayed())

    def test_account_links(self):
        # get the all the links with Account text in it
        account_links = self.driver.find_elements_by_partial_link_text("")
        # check Account and My Account link is displayed/visible in the Home Page footer
        self.assertTrue(2, len(account_links))

    def test_count_of_promo_banners_images(self):
        # get promo banner list
        banner_list = self.driver.find_element_by_class_name()
        # get images from the banner_list
        banners = banner_list.find_elements_by_tag_name("")
        # check there are 3 banners displayed on the page
        self.assertEqual(3, len(banners))

    def test_vip_promo(self):
        # get vip promo image
        vip_promo = self.driver.find_element_by_xpath("")
        # check vip promo logo is displayed on home page
        self.assertTrue(vip_promo.is_displayed())
        # click on vip promo images to open the page
        vip_promo.click()
        # check page title
        self.assertEqual("VIP", self.driver.title)

    def test_shopping_cart_status(self):
        # check content of My Shopping Cart block on home page
        # get the Shopping cart icon and click to
        shopping_cart_icon = self.driver.find_element_by_css_selector("")
        shopping_cart_icon.click()

        # get the shopping car status
        shopping_cart_status = self.driver.find_element_by_css_selector("").text
        self.assertEqual("", shopping_cart_status)

        # close the shopping cart section
        close_button = self.driver.find_element_by_css_selector("")
        close_button.click()

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
