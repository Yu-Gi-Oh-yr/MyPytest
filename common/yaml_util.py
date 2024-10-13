import os
import yaml


# 读取Yaml文件
def read_yaml(key):
    # os.getcwd()获取根目录
    with open(os.getcwd()+"/venu/extract.yaml", encoding="utf-8") as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value[key]


# 写入Yaml文件
def write_yaml(data):
    # 采用追加“a”的方式写入json值,allow_unicode=True表示允许写入unicode编码
    with open(os.getcwd() + "/venu/extract.yaml", encoding="utf-8", mode="a") as f:
        yaml.dump(data, stream=f, encoding="utf-8", allow_unicode=True)


# 清空Yaml文件
def clear_yaml():
    with open(os.getcwd() + "/venu/extract.yaml", encoding="utf-8", mode="w") as f:
        f.truncate()


def read_test_yaml(yaml_path):
    with open(os.getcwd() + yaml_path, encoding="utf-8") as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value