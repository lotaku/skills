#!/usr/bin/env python
# encoding: utf-8
from packet import CSendPacket
from termcolor import colored
#服务器收包
def C2GS_1_Handler(socket,packet):
    print colored('服务器收到新的网络包','green')
    print colored('包的协议号：     ','green'), packet.m_HandlerId
    content = packet.UnPackString()
    print colored('包的内容长度:    ','green'), len(content)
    print colored('包的内容:        ','green'), content

    #实例化新的包,返回给客户端
    newPacket = CSendPacket(packet.m_HandlerId)
    newPacket.PackString(content)
    GS2CTcpHandler(socket,newPacket)
    print '*'*60
    #复习自问：在这里有执行发包到客户端的操作么？

def C2GS_2_Handler(socket,packet):
    #因为是简单测试，同C2GS_1_Handler()一样。
    C2GS_1_Handler(socket,packet)



C2GSHandler={
    1:C2GS_1_Handler,
    2:C2GS_2_Handler,
}

def C2GSTcpHandler(remoteSocket,packet):
    try:
        C2GSHandler[packet.m_HandlerId](remoteSocket,packet)

    except Exception as e:
        print '发生错误!'
        print '错误类型：',colored(str(e.__class__))
        errorString=str(e.message)+'号包的协议号没有定义'
        print colored(errorString,'red')
        print '*'*60
        newPacket=CSendPacket(0)
        #错误类型
        newPacket.PackString(str(e.__class__))
        #错误信息
        newPacket.PackString(errorString)
        GS2C_Error_Handler(remoteSocket,newPacket)




#服务器回包
def GS2C_1_Handler(socket, packet):
    try:
        packet.SendToSocket(socket)
        print '服务器发送包到客户端,包的协议号：',packet.m_HandlerId
    except Exception as e:
        errorSting='服务器发送包到客户端：失败！'+str(e.message)
        print colored(errorSting,'red')

def GS2C_2_Handler(socket, packet):
    GS2C_1_Handler(socket,packet)

def GS2C_Error_Handler(socket, packet):
    GS2C_1_Handler(socket,packet)

GS2CHandler={
    1:GS2C_1_Handler,
    2:GS2C_2_Handler,
}

def GS2CTcpHandler(remoteSocket,packet):
    GS2CHandler[packet.m_HandlerId](remoteSocket,packet)



