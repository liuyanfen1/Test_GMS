from Common import Request,Assert,read_excel
import allure
import pytest


request=Request.Request()
assertion=Assert.Assertions()

url='http://192.168.9.121:8082'

class Test_GMS:
    def test_login(self):
        login_resp=request.post_request(url=url+'/gm-data/v1/user/login',
                                        json={"tenantId":"","name":"Admin","password":"Abc123","country":"Singapore"})
        resp_text=login_resp.text
        print(type(resp_text))

        resp_dict = login_resp.json()
        print(type(resp_dict))

        assertion.assert_code(login_resp.status_code,200)
        assertion.assert_in_text(resp_dict['message'],'Succeeded')

