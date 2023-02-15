import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import zipfile


accum_basins_url = 'https://mghydro.com/watersheds/rasters/accum_basins/'
 
browser = webdriver.Chrome(ChromeDriverManager().install())
for i in range(12,13):
    browser.get(f'{accum_basins_url}/accum{i}.tif')
    print(browser)
    # button = browser.find_element_by_class_name('button.search')
    # button.click()
# print("success")

# https://selenium-python.readthedocs.io/locating-elements.html
# conda install -c conda-forge brotlipy
# https://github.com/senkukogetsu/delineator