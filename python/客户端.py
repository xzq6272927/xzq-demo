#coding=utf-8
'''
双向通信socket之客户器端
读取客户端发送的数据，将内容输出到控制台
将控制台输入的信息发送到客户器端
'''
#导入socket模块
from socket import *
from threading import Thread
def recv_data():
    while True:
        #接收服务器数据
        recv_data=tcp_client_socket.recv(1024)
        print(f'服务器说:{recv_data.decode("gbk")}')
def send_data():
    while True:
        msg=input('>')
        #向服务器发送数据
        tcp_client_socket.send(msg.encode('gbk'))
        if msg=='end':
            break
if __name__ == "__main__":
    #创建客户端socket对象
    tcp_client_socket=socket(AF_INET,SOCK_STREAM)
    #连接服务器端
    tcp_client_socket.connect(('127.0.0.1',8888))
    t1=Thread(target=recv_data)
    t2=Thread(target=send_data)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    tcp_client_socket.close()