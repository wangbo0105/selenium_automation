from Base.element import Element
from Base.browser import Browser
from Base.window import Window


class BasePage(Element, Browser, Window):
    def __init__(self):
        self.element = Element()
        self.browser = Browser()
        self.window = Window()
