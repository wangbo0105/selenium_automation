from Base.base import Base
from robot.api.deco import keyword
from services.CommonLibrary import CommonLibrary

class Searchpage(Base):
    cl = CommonLibrary()
    search_box = ('class', 'search-box')  # 搜索框
    search_input = ('id', 'searchInput')  # 搜索词输入框
    search_result = ('class', 'item-container') #搜索结果内容容器

    def click_search_box(self):
        self.click(self.findElement(self.search_box))

    def input_searchWord(self, searchword):
        #输入搜索词
        self.send_keys(self.findElement(self.search_input), searchword)
        #点击回车
        self.enter(self.findElement(self.search_input))
    def check_searchResult(self):
        self.findElement(self.search_result)







