# -*- coding: UTF-8 -*-
class Config(object):
    def __init__(self):
        # 定义有效期
        self.validity = 3000
        # 定义多快算频繁
        self.too_often = 1
        # 定义模板所在的文件夹
        self.template_folder = '../static/templates'