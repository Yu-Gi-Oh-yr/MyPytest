import time
import pytest

from common.send_request import SendRequest
from common.yaml_util import read_yaml, write_yaml


class TestLogin:

    """def setup_class(self):
        print("类执行前")

    def teardown_class(self):
        print("类执行后")

    def setup(self):
        print("用例执行前")

    def teardown(self):
        print("用例执行后")"""

    # @pytest.mark.parametrize("caseinfo", ["1", "2", "3"])
    # def test_login(self, caseinfo):
    #     print(caseinfo)
    #     write_yaml({"username": "admin"})
    #
    # # @pytest.mark.smoke
    # @pytest.mark.parametrize("name,age", [["1", "X"], ["2", "Y"], ["3", "Z"]])
    # def test_register(self, name, age):
    #     print("注册接口: %s" % name, age)
    #
    # def test_test(self):
    #     url = "https://api.weixin.qq.com/cgi-bin/tags/update?access_token" + read_yaml("access_token")
    #     datas = {"tag": {"id": 134, "name": "广东人"}}
    #     # res = requests.post(url=url, json=datas)
    #     res = SendRequest().all_send_request(method="post", url=url, json=datas)