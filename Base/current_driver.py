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
    # option_chrome.add_argument('headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    option_chrome.add_argument('--no-sandbox')
    option_chrome.add_argument('--disable-dev-shm-usage')
    # option_chrome.add_argument('window-size=1920x3000') #指定浏览器分辨率
    option_chrome.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    option_chrome.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
    # option_chrome.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    option_chrome.add_argument(
        '--enable-features=NetworkService,NetworkServiceInProcess')  # 修复chrome74 版本静默模式cookies丢失问题

    if browser == 'chrome':
        driver = webdriver.Chrome(chrome_options=option_chrome)
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'safari':
        driver = webdriver.Safari()

    return driver
