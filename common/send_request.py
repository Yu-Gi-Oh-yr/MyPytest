import requests


class SendRequest:

    # 获取会话(作为类属性，用类名调用)，所有请求共享，自动管理cookie关联
    sess = requests.session()

    def all_send_request(self, method, url, **kwargs):
        print("-----接口测试开始-----")
        print("请求方法：%s" % method)
        print("接口地址：%s" % url)
        res = SendRequest.sess.request(method, url, **kwargs)
        print("接口返回：%s" % res.json())
        print("-----接口测试结束-----")
        print("\n")
        return res