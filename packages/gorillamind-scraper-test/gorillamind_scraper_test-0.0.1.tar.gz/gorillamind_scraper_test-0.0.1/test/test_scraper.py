import unittest
from scraper.gorilla_scraper import GorillaMindScraper
from selenium.webdriver.common.by import By
import time
import os
import urllib

class TestScraper(unittest.TestCase):
    def setUp(self):
        self.bot = GorillaMindScraper()
        

    def test1_close_popup(self):
        self.bot.close_popup(xpath= '//button[@class= "sc-75msgg-0 boAhRx close-button cw-close"]')
        self.bot.driver.find_element(By.XPATH, '//a[@class= "header__logo"]')

    def test2_find_container(self):
        product_list = self.bot.find_container()
        self.assertIsInstance(product_list, list)
        self.assertEquals(len(product_list), 45)
        for product in product_list:
            self.assertIsInstance(product, str)
            self.assertTrue(product.startswith("https"))
    
    def test3_product_details(self):
        product_list = self.bot.find_container()
        data_dict = self.bot.product_details(product_list)
        self.assertIsInstance(data_dict, dict)
        self.assertEquals(len(data_dict), 11)
        self.assertEquals(len(data_dict.values()), 11)
        self.assertTrue(data_dict["Nutritional_info"][0].startswith("https"))
        self.assertTrue(data_dict["Product_image"][0].startswith("https"))
        # self.driver.get_screenshot_as_file('nutritional_info.png')
    
        
    # def test4_product_details(self):
    #     product_list = self.bot.find_container()
    #     data_dict = self.bot.product_details(product_list)
    #     for products in data_dict:
    # folder_name = data_dict['id'].append(products.split("/")[-1])
    #         # directory_path = f'raw_data/{folder_name}'
    #         # self.assertTrue(os.path.exists(directory_path))
    
    def tearDown(self):
        del self.bot
    


if __name__ == '__main__':
    unittest.main(verbosity=2)