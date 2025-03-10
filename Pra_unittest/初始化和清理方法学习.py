#coding:utf-8

import unittest
from Pra_unittest.myfun import *

class TestMyFun(unittest.TestCase):

    # TestCase基类方法,所有case执行之前自动执行
    @classmethod
    def setUpClass(cls):
        print("这里是所有测试用例前的准备工作")

    # TestCase基类方法,所有case执行之后自动执行
    @classmethod
    def tearDownClass(cls):
        print("这里是所有测试用例后的清理工作")

    # TestCase基类方法,每次执行case前自动执行
    def setUp(self):
        print("这里是一个测试用例前的准备工作")

    # TestCase基类方法,每次执行case后自动执行
    def tearDown(self):
        print("这里是一个测试用例后的清理工作")

    def test_add(self):
        print('这里是运行的test开头的用例')
        result = add(1,2)
        self.assertEqual(3, result)
        self.assertEqual(1,2,'断言失败，请检查两个对比参数')
        # self.assertNotEqual(3, add(2, 2))  # 测试业务方法add

    @unittest.skip('这是跳过的原因/描述')
    def test_sub(self):
        print('这里跳过的用例')
        self.assertEqual(3, add(1, 2))
        self.assertEqual(1,2,'1!=2')
        self.assertNotEqual(3, add(2, 2))  # 测试业务方法add


if __name__ == '__main__':
    unittest.main(verbosity=2)


