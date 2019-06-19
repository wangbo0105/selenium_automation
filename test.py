from selenium import webdriver
import time

option_chrome = webdriver.ChromeOptions()
option_chrome.add_argument('disable-infobars')  # 关闭“Chrome正处于软件的自动控制之下”信息栏
option_chrome.add_argument('--no-sandbox')
option_chrome.add_argument('--disable-dev-shm-usage')
# option_chrome.add_argument('window-size=1920x3000') #指定浏览器分辨率
option_chrome.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
# option_chrome.add_argument('--hide-scrollbars') #隐藏滚动条, 应对一些特殊页面
option_chrome.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
option_chrome.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败

driver = webdriver.Chrome(chrome_options=option_chrome)
driver.get("https://www.baidu.com")
time.sleep(3)
driver.quit()
