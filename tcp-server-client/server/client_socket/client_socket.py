#!/usr/bin/env python
# encoding: utf-8
class CClientSocket():
    def __init__(self,socket):
        self.m_Id=None
        self.m_socket=socket
        self.m_SendData=''
