#!/usr/bin/env python
# encoding: utf-8

class CClientSocketManage():
    def __init__(self):
        self.m_FreeId=10
        self.m_clients={}#socket:client


    def Add(self,newClient):
        newClient.m_Id=self.m_FreeId
        self.m_FreeId+=1

        self.m_clients[newClient.m_socket]=newClient

    def GetBySocket(self,socket):
        return self.m_clients[socket]

clientSocketManage=CClientSocketManage()

