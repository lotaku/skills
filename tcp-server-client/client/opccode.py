#!/usr/bin/env python
# encoding: utf-8
from packet import CSendPacket
from termcolor import colored

#客户端收包
def GS2C_1_Handler(client,packet):
    print '客户端收到新回的网络包'
    print '包的协议号：     ', packet.m_HandlerId

    content = packet.UnPackString()
    print '包的内容:        ', content
    print '包的内容长度:    ', len(content)
    print '='*60

def GS2C_2_Handler(client,packet):
    #因为时简单的示例，这里和GS2C_1_Handler 仅 协议号不同
    GS2C_1_Handler(client,packet)

def GS2C_Error_Handler(client,packet):
    print '客户端收到新回的网络包',colored('(发生错误)')
    print '包的协议号：     ', packet.m_HandlerId

    errorClass=packet.UnPackString()
    print '错误类型:        ', colored(errorClass,'red')

    errorInfo=packet.UnPackString()
    print '错误信息:        ', colored(errorInfo,'red')

    print '='*60

GS2CHandler={
    0:GS2C_Error_Handler,
    1:GS2C_1_Handler,
    2:GS2C_2_Handler,
}

def GS2CTcpHandler(client,packet):
    GS2CHandler[packet.m_HandlerId](client,packet)


#客户端发包
def C2GS_1_Handler(socket, oldPacket):
    #新包的协议号
    newPacket=CSendPacket(1)
    #将刚刚收到的包的内容重新打包
    text = oldPacket.UnPackString()
    newPacket.PackString(text)
    newPacket.SendToSocket(socket)



def C2GS_2_Handler(socket, oldPacket):
    #新包的协议号
    newPacket=CSendPacket(1)
    #将刚刚收到的包的内容重新打包
    text = oldPacket.UnPackString()
    newPacket.PackString(text)
    newPacket.SendToSocket(socket)

C2GSHandler={
    1:C2GS_1_Handler,
    2:C2GS_2_Handler,
}

def C2GSTcpHandler(remoteSocket,packet):
    C2GSHandler[packet.m_HandlerId](remoteSocket,packet)



