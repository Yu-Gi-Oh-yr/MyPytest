import requests
import pytest
from common.send_request import SendRequest
from common.yaml_util import write_yaml, read_yaml, read_test_yaml


class TestAPi:

    # access_token = ""

    # 抓取鉴权码(token、cookie、session,通过用户名和密码获取)
    # @pytest.mark.smoke
    # @pytest.mark.parametrize("caseinfo", test_yaml("/testcases/get_token.yaml"))
    # def test_get_token(self, caseinfo):
    #     url = "https://www.saucedemo.com"
    #     print("-----------------------------")
    #     name = caseinfo["name"]
    #     request = caseinfo["request"]
    #     headers = caseinfo["headers"]
    #     method = caseinfo["method"]
    #     url = caseinfo["url"]
    #     params = caseinfo["params"]
    #     validate = caseinfo["validate"]
    #     print("-----------------------------")
    #     res = SendRequest().all_send_request(method="get", url=url, params=params)
    #     # res = requests.get(url=url, params=datas)
    #     # res = SendRequest().all_send_request(method="get", url=url, params=datas)
    #     result = res.json()
    #     # TestAPi.access_token = result["access_token"]
    #     # write_yaml({"access_token": result["access_token"]})
    #     # write_yaml({"csrf_token": "123"})
    #     print(res.json())
    #
    # # 编辑标签接口
    # def test_edit_flag(self):
    #     url = "https://www.saucedemo.com/update?access_token" + read_yaml()
    #     datas = {"tag": {"id": 134, "name": "广东人"}}
    #     # res = requests.post(url=url, json=datas)
    #     res = SendRequest().all_send_request(method="post", url=url, json=datas)
    #     print(res.json())
    #
    # # 文件上传接口
    # def test_file_upload(self):
    #     url = "https://www.saucedemo.com/update?access_token" + read_yaml()
    #     datas = {"media": open("E:\\0.jpg", mode="rb")}
    #     # res = requests.post(url=url, files=datas)
    #     res = SendRequest().all_send_request(method="post", url=url, files=datas)
    #     print(res.json())

    def test_test_print(self):
        print("这是一个测试用例")

