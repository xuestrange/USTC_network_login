#!/home/xue/miniconda3/bin/python

"""
第一行为Python路径
"""
import requests
url = "http://wlt.ustc.edu.cn/cgi-bin/ip"

def login(name, passwd, type = 5):
    """
    自动登录中国科学技术大学网络通, 并选择网络进行自动连接
    Args:
        name (str): 帐号
        passwd (str/int): 帐号密码
        type (int, optional): 0代表教育网出口, 5代表(电信网出口3). Defaults to 5.
    """
    session = requests.Session()
    data = {
            "cmd":"login",
            "name": name,
            "password": passwd
            }
    network = {
        0: "1教育网出口",
        5: "6电信网出口"
    }
    try:
        login = session.post(url, data)
        if login.status_code == 200:
                query = {
                        "cmd":"set",
                        "url": "URL",
                        "type": type,
                        "exp": 0
                }
                try:
                    status = session.get(url, params=query)
                    if status.status_code == 200:
                        print("congratulations, 成功连接至中国科学技术大学校园网, 出口为\"%s\""%(network[type]))
                except:
                    print("connect error")
    except:
        print("login error")
login(name = "", passwd = )
