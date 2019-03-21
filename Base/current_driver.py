from selenium import webdriver

__driver = None


def get():
    global __driver

    if __driver is None:
        __driver = __create_driver()

    return __driver


def quit():
    global __driver

    if __driver is not None:
        __driver.quit()
        __driver = None


def __create_driver(browser='chrome'):
    global driver
    option_chrome = webdriver.ChromeOptions()
    option_chrome.add_argument('disable-infobars')  # 关闭“Chrome正处于软件的自动控制之下”信息栏
    # option_chrome.add_argument('kiosk')  # Mac 全屏
    # option_chrome.add_argument('start-fullscreen')
    # option_chrome.add_argument('maximized')  # Windows 全屏
    # option_chrome.add_argument("--proxy-server='direct://'")
    # option_chrome.add_argument("--proxy-bypass-list=*")
    option_chrome.add_argument('headless')

    if browser == 'chrome':
        driver = webdriver.Chrome(chrome_options=option_chrome)
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'safari':
        driver = webdriver.Safari()

    return driver
