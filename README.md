# USTC_network_login
login and connect USTC campus network automaticly, 自动登录并连接中国科学技术大学(USTC)校园网.

## requirements
需要安装`requests`包
```shell
pip install requests
```
## NOTE
`ustc_login.py`文件的第一行指定了python的路径, 这是在linux系统下才有的写法, 若安装位置不同需要修改
以下所有设置的路径需要用户手动修改.

## 开机自动启动
### linux系统
然后通过命令行赋予这个文件的可执行权限
```shell
# cd 该文件所在文件夹
sudo chmod +x ./ustc_login.py
```
``` shell
sudo vim etc/rc.local
```
把执行py脚本的命令插入进去,保存
### windows系统
TODO
