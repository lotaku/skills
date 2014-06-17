##个人职业技能
更新时间：2014-06-17

##程序1：C/S网络
在 网络 和朋友 prim 的支持下，学会编写本程序

###程序的简单介绍
* 支持TCP协议的Client/Server网络
* 用select 实现 I/O 的简单复用
* 编写packet类，实现压包、解包
* C/S 支持发包，收包操作
* 在server上创建client_socket包类,编写client类和client管理管理类

###其他说明
* '包',是指信息包，由包的协议号、内容长度、内容组成。

###程序的简单容错处理
* client：判断用户输入的内容是否符合要求的格式，不符合则要求重新输入。
* server：使用`try...except...`处理未定义包协议号发送的错误，在server显示错误信息，并把信息打包发给client

###运行程序
* 依次运行`client`和`server`文件夹下的`main.py`文件   
     
     
    #在终端里执行命令：
    python main.py

* 按照程序的提示，在client输入测试内容，如：   

    1,首都beijing

* 输入exit ，可以退出程序

###测试截图
client(客户端)   
![客户端测试截图](https://raw.githubusercontent.com/lotaku/skills/master/tcp-server-client/images/client.png)


server(服务器)   
![服务器测试截图](https://raw.githubusercontent.com/lotaku/skills/master/tcp-server-client/images/server.png)





