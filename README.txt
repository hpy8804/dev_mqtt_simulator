1、文件说明
clientSubMain.py 模拟设备端收发消息
clientSub.py     模拟app端接收设备respond
clientPub.py     模拟app端发送请求
config.py        通用配置项
rsp.json         应答消息配置


2、使用说明
使用python3启动 clientSubMain clientSub
使用python3启动 clientPub

3、可以在config.py中直接定义某个action对应的应答消息

4、修改rsp.json可以看到发送消息后应答发生改变
