# encoding: utf-8
from termcolor import colored
class CTest_SendPacket():
    def __init__(self):
        pass

    def SendPacket(self,CSendPacket,tcpClient):
        print colored('请输入要发送的包协议号(1,或2)和内容：','green')
        print colored('参考格式：','green'),'2,你好'

        while True:
            print colored('开始输入：','green'),
            self.text=raw_input()
            print '='*60
            if self.text=='exit':
                print '退出程序'
                exit()
            try:
                self.m_HandlerId,self.m_Content=self.text.split(',')
                break
            except Exception as e:
                print colored(e,'red')
                print colored('Error:格式错误，请重新输入','red')

        self.m_HandlerId=int(self.m_HandlerId)
        packet = CSendPacket(self.m_HandlerId)
        packet.PackString(self.m_Content)
        packet.Send(tcpClient)

