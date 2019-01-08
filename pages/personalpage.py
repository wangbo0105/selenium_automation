from Base.base import Base


class Personalpage(Base):
    personal_center = ('link_text', '个人中心')  # 用户tab——个人中心
    user_tab = ('class', 'ant-dropdown-trigger')  # 用户tab
    home_tab = ('class', 'tabs-tab', 0)  # 主页tab

    # def hover_user_tab(self):
    #     """将鼠标移动到个人中心tab"""
    #     self.move_to_element(self.findElement(self.user_tab))
    #
    # def go_personal_center(self):
    #     self.click(self.findElement(self.personal_center))
    #     return self
