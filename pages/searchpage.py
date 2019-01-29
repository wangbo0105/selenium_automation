from pages.basepage import BasePage


class Searchpage(BasePage):
    search_box = ('class', 'search-box')  # 搜索框
    search_input = ('id', 'searchInput', 0)  # 搜索词输入框
    search_result = ('class', 'tabs-nav', 0)  # 搜索结果内容容器

    def click_search_box(self):
        self.element.click(self.search_input)

    def input_searchWord(self, searchword):
        # 输入搜索词
        self.element.send_keys(self.search_input, searchword)
        # 点击回车
        self.element.enter(self.search_input)

    def check_searchResult(self):
        self.element.is_element_exist(self.search_result)
