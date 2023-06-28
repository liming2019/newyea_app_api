import requests
from api.LoginApi import LoginApi
import unittest
from parameterized import parameterized
import logging
from utils import read_param_data, assert_response


class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.login = LoginApi()
        self.session = requests.session()

    def tearDown(self) -> None:
        logging.info('——————————————————————')
        self.session.close()

    @parameterized.expand(read_param_data('login.json', 'test_get_cms_code'))
    def test01_get_sms_code(self, desc, phone, status_code, code, text=None):
        logging.info('test_title = {}, phone = {}'.format(desc, phone))
        response = self.login.getcode(self.session, phone)
        logging.info('response_json_data = {}'.format(response.json()))
        assert_response(self, response, status_code, code, text)

    @parameterized.expand(read_param_data('login.json', 'test_login'))
    def test02_login(self, desc, phone, verify_code, status_code, code, text=None):
        logging.info('test_title = {}, phone = {}, verify_code = {}'.format(desc, phone, verify_code))
        response = self.login.login(self.session, phone, verify_code)
        logging.info('response_json_data = {}'.format(response.json()))
        assert_response(self, response, status_code, code, text)
