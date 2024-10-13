import os
import time

import pytest
from common.yaml_util import read_test_yaml, read_yaml

if __name__ == '__main__':
    pytest.main()
    # print(read_yaml("name"))
    # print(read_test_yaml("/testcases/get_token.yaml"))
    # 使程序暂停执行3秒
    time.sleep(3)
    # 根据临时json报告生成allure报告，-o ./reports 指定了生成的报告的输出目录，--clean 参数表示在生成报告之前清除输出目录中的旧文件。
    os.system("allure generate ./temps -o ./reports --clean")
