from Base.base import Base


class Languagepage(Base):
    langs = ('class', 'langs')  # 语言切换栏
    english_tab = ('class', 'lang')  # English
    japanese_tab = ('class', 'lang', 1)  # Japanese
    veer_mark_text = ('class', 'app-des')  # 环 球 V R 内 容 社 区
