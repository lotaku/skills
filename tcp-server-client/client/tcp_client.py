#!/usr/bin/env python
# encoding: utf-8

from select import select
from socket import socket
from socket import AF_INET, SOCK_STREAM
from packet import CRecvPacket
#from packet import CSendPacket
from opccode import GS2CTcpHandler

from termcolor import colored
class CTcpClient:

    def __init__(self):
        self.m_ConnectSocket=socket(AF_INET, SOCK_STREAM)
        self.m_SendData = ''
        self.m_RecvData = ''
        self.m_Buffers = []

        self.m_Host = 'localhost'
        self.m_Port = 8888

    def Connect(self):
        try:
            self.m_ConnectSocket.connect((self.m_Host,self.m_Port))
            self.m_ConnectSocket.setblocking(0)
            print "连接服务器成功，socket设置为非阻塞"
        except Exception as e:
            print '连接服务器失败：', e
            exit()

    def RecvPackets(self):
        reads, _, errors =select([self.m_ConnectSocket], [], [],0.0001)
        if self.m_ConnectSocket in reads:
            self.Read()

    def SendPackets(self):
        _, writes, errors = select([], [self.m_ConnectSocket], [], 0.0001)
        if self.m_ConnectSocket in writes:
            self.Write()

    def HandlePackets(self):
        for buffer in self.m_Buffers:
            packet=CRecvPacket(buffer)
            GS2CTcpHandler(self,packet)
        self.m_Buffers=[]

    def Read(self):
        data = self.m_RecvData +self.m_ConnectSocket.recv(1024)
        if data:
            dataLength = len(data)
            lengthBeginIndex = 0
            contentBeginIndex = 2

            if dataLength >= contentBeginIndex:
                contentLength = ord(data[lengthBeginIndex])*0x100 + ord(data[lengthBeginIndex+1])
                packetLength = contentBeginIndex + contentLength
                while dataLength >= packetLength:
                    content = data[contentBeginIndex:contentBeginIndex+contentLength]
                    self.m_Buffers.append(content)
                    data=data[contentBeginIndex+contentLength:]
                    dataLength = len(data)
                    if dataLength >= contentBeginIndex:
                        contentLength = ord(data[lengthBeginIndex])*0x100 + ord(data[lengthBeginIndex+1])
                        packetLength = contentBeginIndex + contentLength
                    else:
                        break
                self.m_RecvData = data
        else:
            pass

    def Write(self):
        data = self.m_SendData
        if len(data):
            amount = self.m_ConnectSocket.send(data)
            self.m_SendData = data[amount:]

    def Help(self):
        print colored("用户帮助信息：",'green')
        print '1:   输入exit，可退出程序'
        print '2:   目前仅定义了1、2包协议号'

tcpClient = CTcpClient()




