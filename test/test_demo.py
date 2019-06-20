from selenium import webdriver
import time

browse = webdriver.Chrome()
browse.get('http://veervr.tv')  # Load page
browse.find_element_by_xpath('//*[@id="app"]/div/div/header/nav[1]/div/ul/li[2]/a').click()
print(browse.title)  # print title
time.sleep(5)
browse.quit()