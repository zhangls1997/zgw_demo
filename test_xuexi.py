#!/user/bin/python
#!-*- coding:utf-8 -*-
import pytest
def zhang(a,b):
    return a-b
def lu(a,b):
    return a*b
def sheng(a,b):
    return a/b
class Testcase(object):
    def test_one(self):
        print("\n正在执行-----test_one")
        assert add(1,2) == 3    #add 是上面函数的名称
    def test_two(self):
        print("正在执行-----test_two")
        assert zhang(1,2) == -1
        assert zhang(3,2) == 1    #哈哈
    def test_three(self):
        print("正在执行-----test_three")
        assert lu(1,2) == 2
    def test_thour(self):
        print("正在执行-----test_thour")
        assert sheng(6,2) == 3
if __name__ == "__main__":
    pytest.main(["-s","test_xuexi.py"])