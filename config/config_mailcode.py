# -*- coding: UTF-8 -*-
class Config(object):
    def __init__(self):
        # 定义有效期
        self.validity = 3000
        # 定义多快算频繁
        self.too_often = 1
        # 定义邮件模板所在的文件夹
        self.template_folder = '../static/templates'
        # 定义博客md、html所在的路径
        self.article_path = './static/articles/'
        # 定义一个临时文件夹，用来存放上传的图片
        self.temporary_path = './static/articles/temporary/'