import pytest

from common.yaml_util import read_yaml, clear_yaml


@pytest.fixture(scope="function", autouse=True)
def exe_f1():
    print("用例执行前")
    # yield可以用来传递参数
    # yield "杨锐来了"
    print("用例执行后")


@pytest.fixture(scope="session", autouse=True)
def exe_f2():
    # 在每个会话开始前清空yaml文件，确保不会一直写入重复的变量
    clear_yaml()