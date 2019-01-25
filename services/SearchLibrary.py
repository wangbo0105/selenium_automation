from robot.api.deco import keyword
from pages.searchpage import Searchpage
from services.CommonLibrary import CommonLibrary

class SearchLibrary(Searchpage):
    cl = CommonLibrary()

    @keyword
    def search(self,searchword):

    #点击搜索，输入搜索词，敲击回车，查看搜索结果，切换tab，查看搜索结果
        self.click_search_box()
        self.input_searchWord(searchword)
        # if expectedResult==True:
        #     self.isElementExist(self.user_tab)
        # else:
        #     self.isElementExist(self.loginBtn)
        self.check_searchResult()

      

