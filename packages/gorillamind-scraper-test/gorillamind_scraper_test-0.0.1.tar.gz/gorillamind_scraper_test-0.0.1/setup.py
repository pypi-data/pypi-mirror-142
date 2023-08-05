from setuptools import setup
from setuptools import find_packages

setup(
    name='gorillamind_scraper_test', ## This will be the name your package will be published with
    version='0.0.1', 
    description='A test package which scrapes the gorilla mind website',
    # url='https://github.com/IvanYingX/project_structure_pypi.git', # Add the URL of your github repo if published 
                                                                   # in GitHub
    author='Ismael Patel', # Your name
    # license='MIT',
    packages=find_packages(), # This one is important to explain. See the notebook for a detailed explanation
    install_requires=['selenium', 'webdriver_manager'], # For this project we are using two external libraries
                                                     # Make sure to include all external libraries in this argument
)
