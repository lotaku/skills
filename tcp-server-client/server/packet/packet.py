#!/usr/bin/env python
# encoding: utf-8
from client_socket import clientSocketManage
class CRecvPacket:

    def __init__(self,buffer):
        #self.m_HandlerClassId=ord(buffer[0])
        self.m_HandlerId=ord(buffer[0])
        self.m_Buffer=buffer
        self.m_CurrentIndex=1

    def UnPackInt(self):
        index = self.m_CurrentIndex

        value = ord(self.m_Buffer[index])*0x100 + ord(self.m_Buffer[index+1])

        self.m_CurrentIndex += 2

        return value

    def UnPackString(self):
        length = self.UnPackInt()

        string = self.m_Buffer[self.m_CurrentIndex:self.m_CurrentIndex+length]

        self.m_CurrentIndex+=length

        return string



class CSendPacket:

    def __init__(self, m_HandlerId):
        self.m_HandlerId= m_HandlerId
        self.m_Buffer = chr(self.m_HandlerId)

    def PackInt(self, value):
        self.m_Buffer += chr(value/0x100) + chr(value%0x100)

    def PackString(self, text):
        length = len(text)
        self.PackInt(length)
        self.m_Buffer += text

    def SendToSocket(self,socket):
        client=clientSocketManage.GetBySocket(socket)
        length = len(self.m_Buffer)
        buffer=chr(length/0x100)+chr(length%0x100)+self.m_Buffer
        client.m_SendData += buffer





