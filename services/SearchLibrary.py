from robot.api.deco import keyword
from pages.searchpage import Searchpage


class SearchLibrary(object):
    def __init__(self):
        self.search = Searchpage()

    @keyword
    def search_content(self, searchword):
        """点击搜索，输入搜索词，敲击回车，查看搜索结果，切换tab，查看搜索结果"""
        self.search.click_search_box()
        self.search.input_searchWord(searchword)
        # if expectedResult==True:
        #     self.isElementExist(self.user_tab)
        # else:
        #     self.isElementExist(self.loginBtn)

    @keyword
    def check_search_result(self):
        self.search.check_searchResult()
