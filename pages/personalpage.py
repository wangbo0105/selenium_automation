from services.BrowserLibrary import BrowserLibrary


class Personalpage(BrowserLibrary):
    personal_center = ('link_text', '个人中心')  # 用户tab——个人中心
    user_tab = ('xpath', '//*[@id="app"]/div/div/header/nav[1]/div/div[2]/a/div[2]')  # 用户tab

    def hover_user_tab(self):
        """将鼠标移动到个人中心tab"""
        mine = self.base.findElement(self.user_tab)
        self.base.move_to_element(mine)

    def go_personal_center(self):
        personal = self.base.findElement(self.personal_center)
        self.base.click(personal)
        return self
