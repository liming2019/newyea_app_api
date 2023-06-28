import time
import unittest
from lib.HTMLTestRunner import HTMLTestRunner
import app
from script.Login import TestLogin

suite = unittest.TestSuite()
suite.addTests(unittest.makeSuite(TestLogin))

report_file = app.base_path + '/report/report_{}.html'.format(time.strftime("%Y-%m-%d %H-%M-%S"))
with open(report_file, 'wb') as f:
    runner = HTMLTestRunner(f, title='新页充电app接口测试')
    runner.run(suite)
