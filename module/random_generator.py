import random


class RandomGenerator:
    @staticmethod
    def random_comments(_length=16):
        """
        生成一个指定长度的随机字符串
        """
        random_str = ''
        base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
        length = len(base_str) - 1
        for i in range(int(_length)):
            random_str += base_str[random.randint(0, length)]
        return random_str
