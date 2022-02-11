# from selenium import webdriver
# import time
# from bs4 import BeautifulSoup
#
# CHROME_DRIVER_PATH = {'YOUR CHROME DRIVER PATH'}
#
#
# class CheckIsFree:
#     def __init__(self, path):
#         self.driver = webdriver.Chrome(executable_path=path)
#
#     def get(self):
#         search = str(input('Search: '))
#         self.driver.get(f'https://pubmed.ncbi.nlm.nih.gov/{id}/')
#
#     def download(self):
#         id = str(input('ID: '))
#         self.driver.get(f'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC{id}/')
#         time.sleep(3)
#         self.driver.find_element_by_xpath('//*[@id="rightcolumn"]/div[2]/div/ul/li[4]').click()
#         time.sleep(5)
#         self.driver.find_element_by_xpath('//*[@id="icon"]/iron-icon').click()
#         time.sleep(5)
#
#
# bot = CheckIsFree(CHROME_DRIVER_PATH)
# bot.download()
#

# For Safari


from selenium import webdriver
import time
from bs4 import BeautifulSoup


class CheckIsFree:
    def __init__(self):
        self.driver = webdriver.Safari()

    def get(self):
        search = str(input('Search: '))
        self.driver.get(f'https://pubmed.ncbi.nlm.nih.gov/{id}/')

    def download(self):
        id = str(input('ID: '))
        self.driver.get(f'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC{id}/')
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="rightcolumn"]/div[2]/div/ul/li[4]').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="icon"]/iron-icon').click()
        time.sleep(5)


bot = CheckIsFree()
bot.download()



