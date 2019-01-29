from Base.element import Element
from Base.browser import Browser
from Base.window import Window
from Base.frame import Frame
from Base.javascript import JavaScript


class BasePage(object):
    def __init__(self):
        self.element = Element()
        self.browser = Browser()
        self.window = Window()
        self.frame = Frame()
        self.js = JavaScript()
        self.url = 'https://stg.veervr.tv/'
