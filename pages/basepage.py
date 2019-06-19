import os

from Base.element import Element
from Base.browser import Browser
from Base.window import Window
from Base.frame import Frame
from Base.javascript import JavaScript


def getEnvVar(key, default=None):
    if key in os.environ:
        return os.environ[key]
    else:
        return default


class BasePage(object):
    def __init__(self):
        self.element = Element()
        self.browser = Browser()
        self.window = Window()
        self.frame = Frame()
        self.js = JavaScript()
        # self.url = getEnvVar("SITE",'https://stg.veervr.tv/')
        self.url = "https://{site}veervr.tv".format(site="" if getEnvVar("PRODUCTION") else "stg.")
