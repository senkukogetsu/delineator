import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import zipfile
import re
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)

accum_basins_url = 'https://mghydro.com/watersheds/rasters/accum_basins/'
flow_dir_basins_url = 'https://mghydro.com/watersheds/rasters/flow_dir_basins/'
 
# browser = webdriver.Chrome(ChromeDriverManager().install())

# browser.get(f'{accum_basins_url}')

# # # button = browser.find_element(By.TAG_NAME,'pre')
# # # # button = browser.find_element(By.TAG_NAME,'pre').text
# # # button.click()

# soup = BeautifulSoup(browser.page_source, 'html.parser')
# # # print(soup.prettify())

# # # a_tags = soup.find_all('a')
# # # for tag in a_tags:
# # #   # 輸出超連結的文字
# # #     print(tag.get('href'))

# # # 以正規表示法比對超連結網址
# # # links = soup.find_all(href=re.compile(r"accum(\d+).tif"))
# files = soup.find_all(href=re.compile(r"accum(\d+).tif"))
# # print(files)
# for file in files:
# #     print(file)
#     # print(type(link))
#     name = file['href']
#     print("Download: ", name)
#     response = requests.get(accum_basins_url + name)
#     # link = file.find('href')
#     # print(link)
#     with open(f'./data/raster/accum_basins/{name}', 'wb') as file:
#         file.write(response.content)
#         file.close()
#     print("finish")
# browser.close()


browser.get(f'{flow_dir_basins_url}')
soup = BeautifulSoup(browser.page_source, 'html.parser')
files = soup.find_all(href=re.compile(r"flowdir(\d+).tif"))
# print(files)
for file in files:
#     print(file)
    # print(type(link))
    name = file['href']
    print("Download: ", name)
    response = requests.get(flow_dir_basins_url + name)
    # link = file.find('href')
    # print(link)
    with open(f'./data/raster/flowdir_basins/{name}', 'wb') as file:
        file.write(response.content)
        file.close()
    print("finish")
browser.close()
print("All finish")



# https://selenium-python.readthedocs.io/locating-elements.html
# conda install -c conda-forge brotlipy
