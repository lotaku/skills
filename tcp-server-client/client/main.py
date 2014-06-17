#!/usr/bin/env python
# encoding: utf-8
from tcp_client import tcpClient
from packet import CSendPacket
from test import CTest_SendPacket

if '__main__' == __name__:

    tcpClient.Connect()
    tcpClient.Help()

    while True:
        test_sendPacket = CTest_SendPacket()
        test_sendPacket.SendPacket(CSendPacket,tcpClient)

        tcpClient.SendPackets()
        tcpClient.RecvPackets()
        tcpClient.HandlePackets()







