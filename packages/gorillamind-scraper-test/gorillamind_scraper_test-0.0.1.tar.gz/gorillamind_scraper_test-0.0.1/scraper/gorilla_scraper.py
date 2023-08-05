import selenium
import time
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import uuid
import json
import pandas as pd
import os 
import urllib.request

class GorillaMindScraper:
    '''
    This class is a scraper which can be used to browse different websites and collect the deatils of each product on that site. 
    Parameters
    ---------- 
    url: str
        The link we would like to visit.
    Attribute
    --------- 
    driver:
        This is a webdriver object.
    '''
    def __init__(self, url: str = 'https://gorillamind.com/collections/all-products'):
        self.driver = Chrome(ChromeDriverManager().install())
        self.driver.get(url)
    def close_popup(self, xpath: str = '//button[@class= "sc-75msgg-0 boAhRx close-button cw-close"]'):
        '''
        This method waits for the popup to appear and then closes it by clicking the button.
        Parameters
        ----------
        xpath: str
            The xpath of the close popup button.   
        '''
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located ((By.XPATH, xpath)))
            self.driver.find_element(By.XPATH , xpath).click()
        except TimeoutException:
            print("No pop up present")
    def find_container(self):
        '''
        This method locates the contianer where all the products are listed. 
        It then iterates through each product link and appends the link to each product into a list.
        Parameters
        ----------
        xpath: str
            The xpath to the container holding each product.
            The xpath to iterate through the container to get each product.
        Returns
        -------
        list
            a list of links to each product. 
        '''
        self.container = self.driver.find_element(By.XPATH, '//div[@class="container collection-matrix"]')
        self.products = self.container.find_elements(By. XPATH, './div')
        prod_list = []
        for items in self.products:
            prod_list.append(items.find_element(By.TAG_NAME, 'a').get_attribute('href'))
        return prod_list
    def create_store(self, folder):
        '''
        Makes a folder within the raw_data folder.
        '''
        if not os.path.exists(folder):
            os.makedirs(folder)
    def data_dump(self, folder_name, data):
        '''
        This method dumps all the collected data for each product into a sperate folder created by it id.
        Paramters
        ---------
        folder_name :str   
        Data:
            Dictionary containing all the infromation about each product.
        '''
        with open(f"raw_data/{folder_name}/data.json", "w") as f:
            json.dump(data, f)   
    def product_details(self, Product_list):
        '''
        Iterates through every product and creates a new folder with the product id as the name. It then continues collecting every value for that product and placing it in the data dictionary.
        The infromation in the data dictionary is then dumped for that product and the process repeats. 
        Paramters
        ---------
        Product_list:
            A list containing the link to go to each product.
        Attribute
        --------- 
        driver:
            This is a webdriver object.
        Returns
        -------
        Folder:
            A folder is created for each product with the id as the name of the folder under the folder raw_data.
        Data:
            A dictionary containing all the information about the product is then dumped into the folder with its id as the name.
        Product_image: img 
            An image of the product is taken and stored in the folder correspondding to its id under raw_data.
        screenshot:
            A screenshot of the nutritional information page is taken and stored in the folder corresponding to its id under raw_data. 
        '''
        for products in Product_list[0:3]:
            data = { 
                "id": [],
                "UUID": [],
                "Product_Link": [],
                "Product_Name": [],
                "Price": [], 
                "No_of_servings": [], 
                "Flavours": [], 
                "Size": [], 
                "Nutritional_info": [],
                "No_of_Reviews": [],
                "Product_image": []
            }
            self.driver.get(products)
            data['id'].append(products.split("/")[-1])
            folder_name = data['id']
            self.create_store(f'raw_data/{folder_name}')
            data['UUID'].append(str (uuid.uuid4()))
            data['Product_Link'].append(products)
            time.sleep(3)
            try:
                product_name = self.driver.find_element(By.XPATH, '//h1[@class="product_name title"]').text
                data['Product_Name'].append(product_name)
            except NoSuchElementException:
                data['Product_Name'].append(None)
            try:
                price = self.driver.find_element(By.XPATH, '//p[@class="modal_price subtitle"]').text
                data['Price'].append(price)
            except NoSuchElementException:
                data['Price'].append(None)
            try:
                no_of_servings = self.driver.find_element(By.XPATH, '//span[@class= "variant-size"]').text
                data['No_of_servings'].append(no_of_servings)
            except NoSuchElementException:
                data['No_of_servings'].append(None)
            try:
                all_flavours = self.driver.find_element(By.XPATH, '//div[@data-option-index="0"]')
                flavour_list = all_flavours.find_elements(By.XPATH, './div')
                flavour_list = [flavour.text for flavour in flavour_list[1:]]
                data['Flavours'].append(flavour_list)
            except NoSuchElementException:
                data['Flavours'].append(None)
            try:
                all_sizes = self.driver.find_element(By.XPATH, '//div[@data-option-index="1"]')
                size_list = all_sizes.find_elements(By.XPATH, './div')
                size_list = [size.text for size in size_list[1:]]
                data['Size'].append(size_list)
            except NoSuchElementException:
                data['Size'].append(None)
            try:
                nutritional_informaion = self.driver.find_element(By.XPATH, '//iframe[@title="Nutrition or Supplement Facts Label"]').get_attribute('src')
                data['Nutritional_info'].append(nutritional_informaion)
            except NoSuchElementException:
                data['Nutritional_info'].append(None)
            try:
                no_of_reviews = self.driver.find_element(By.XPATH, '//span[@id="spr_badge_4898112667693"]').text
                data['No_of_Reviews'].append(no_of_reviews)
            except NoSuchElementException:
                data['No_of_Reviews'].append(None)
            try:
                product_image = self.driver.find_element(By.XPATH, '//img[@class="lazyload--fade-in lazyautosizes lazyloaded"]').get_attribute('src')
                data['Product_image'].append(product_image)
            except NoSuchElementException:
                data['Product_image'].append(None)
            urllib.request.urlretrieve(product_image, f"raw_data/{folder_name}/{folder_name}.jpg") 
            self.driver.get(nutritional_informaion)
            time.sleep(1)
            # self.driver.get_screenshot_as_file('nutritional_info.png')
            time.sleep(1)
            self.driver.save_screenshot(f"raw_data/{folder_name}/{folder_name}nutritional_info.png")
            self.data_dump(folder_name, data)
            self.driver.back()
            time.sleep(3)
        return data

if __name__ == '__main__':
    bot = GorillaMindScraper()
    bot.close_popup()
    # bot.find_container()
    Product_list = bot.find_container()
    #bot.product_details(Product_list)
    data_dict = bot.product_details(Product_list)



    