#!/user/bin/python
#!-*- coding:utf-8 -*-
import yaml
import warnings
warnings.simplefilter("ignore", ResourceWarning)
# with open(r'C:\Users\123456\Desktop\kaiwan_AuToTest\Caps\Caps.yaml','r',encoding='utf-8') as fb:
#     # a=yaml.load(fb)使用yaml模块的load方法将yaml文件中的数据转换成python字典的形式
#     # item_data=yaml.load(fb,Loader=yaml.FullLoader)
#     item_data = yaml.load(fb)
class BaseDriver(object):
    def base_driver(self,automationName='appium',noRest=True):
        # warnings.simplefilter("ignore", ResourceWarning)
        with open(r'C:\Users\123456\Desktop\kaiwan_AuToTest\Caps\Caps.yaml', 'r', encoding='utf-8') as fb:
            datas = yaml.load(fb,Loader=yaml.FullLoader)
        if automationName != "appium":
            datas[0] = "appium"
        if noRest == False:
            datas[0]["noRest"] = False
        server = 'http://{0}:{1}/wd/hub'.format(datas[])
BaseDriver().base_driver()