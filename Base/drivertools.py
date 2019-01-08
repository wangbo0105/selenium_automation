from selenium import webdriver


class DriverTools(object):
    @staticmethod
    def driver(browser='chrome'):
        option_chrome = webdriver.ChromeOptions()
        option_chrome.add_argument(
            'disable-infobars')  # 关闭“Chrome正处于软件的自动控制之下”信息栏
        option_chrome.add_argument('kiosk')  # Mac 全屏
        option_chrome.add_argument('maximized')  # Windows 全屏

        if browser == 'chrome':
            driver = webdriver.Chrome(chrome_options=option_chrome)
        elif browser == 'firefox':
            driver = webdriver.Firefox()
        elif browser == 'safari':
            driver = webdriver.Safari()
        return driver
