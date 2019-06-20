import json
import time
from selenium import webdriver

driver = webdriver.Chrome()
# driver.get('http://stg.veervr.tv')  # Load page
# # driver.find_element_by_xpath('//*[@id="app"]/div/div/header/nav[1]/div/ul/li[2]/a').click()
# driver.find_element_by_class_name("header-login").click()
# driver.find_element_by_css_selector('#loginIdentifier').send_keys('veerqa@veer.tv')
# driver.find_element_by_css_selector('#loginPassword').send_keys('123456')
# driver.find_element_by_class_name('submit-btn').click()
# time.sleep(5)
# cookies = driver.get_cookies()
# with open("cookies.json", "w") as fp:
#     json.dump(cookies, fp)
# driver.quit()

driver.get("http://stg.veervr.tv")
with open("cookies.json", "r") as fp:
    cookies = json.load(fp)
    for cookie in cookies:
        # cookie.pop('domain')  # 如果报domain无效的错误
        driver.add_cookie(cookie)

driver.get("http://stg.veervr.tv")
time.sleep(10)
driver.quit()