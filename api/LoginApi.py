import json
import time
import app


class LoginApi:
    def __init__(self):
        self.getcode_url = app.base_url + '/appapi/apiGetVerifyCode?param={}'
        self.login_url = app.base_url + '/appapi/apiUserLogin?param={}'

    def getcode(self, session, phone):
        param_data = {"phoneNo": phone,
                      "timestamp": int(time.time()),
                      "newyeaAppVersion": app.app_version,
                      "newyeaAppType": app.app_type,
                      "deviceId": app.device_id,
                      "isEncryption": "1"}
        self.getcode_url = self.getcode_url.format(json.dumps(param_data))
        response = session.post(url=self.getcode_url)
        return response

    def login(self, session, phone, verify_code):
        param_data = {"phoneNo": phone,
                      "timestamp": int(time.time()),
                      "newyeaAppVersion": app.app_version,
                      "verifyCode": verify_code,
                      "newyeaAppType": app.app_type,
                      "deviceId": app.device_id,
                      "isEncryption": "1"}
        self.login_url = self.login_url.format(json.dumps(param_data))
        response = session.post(url=self.login_url)
        return response
