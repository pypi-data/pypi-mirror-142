# Selenium

Selenium is an open web-based automation tool which can be used with Python language for testing.

# WebDriver_manager

WebDriverManager automates the browser setup in the Selenium code and is used to import Chrome driver manager. 


# Milestone 2

A scraper class has been built which navigates through the Gorilla mind website by first closing any popups that appear and then it locates the container to where all the products are stored. Through this container it iterates through the child's div tags to get the list of links to each product on that website. 

# Milestone 3 

The scraper then collects all the URL links to each product and iterates through them, one by one. While iterating through it extracts information about each product and then stores the information into a dictionary. A folder is then created for each product dictionary created with the unique ID being the title of each folder. This folder will contain all the product information as well as two images (product image, nutritional information)  

# Milestone 4

The code for the scraper has been refracted and optimised by removing unnecessary nested loops and other time and space complexities. Doc strings were added to each function and unit testing and integration testing was done on every public method present within the code.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install selenium.

```zsh
pip install selenium
pip install webdriver_manger
pip install pandas 
```

## Usage

```python
import selenium
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import uuid
import json
import os 
import urllib.request

# closes the popup when going on the site
close_popup(self, xpath)

# returns the list of products located within the contianer with each product and it's http link.
find_container(self)

# returns a dictionary containing all the product information

```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)