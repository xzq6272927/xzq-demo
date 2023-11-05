#coding=utf-8
'''
双向通信socket之服务器端
读取客户端发送的数据，将内容输出到控制台
将控制台输入的信息发送到客户器端
'''
#导入socket模块
from socket import *
from threading import Thread
def recv_data():
    while True:
        #读取客户端的消息
        re_data=tcp_client_socket.recv(1024).decode('gbk')
        #将消息输出到控制台
        print(f'客户端说:{re_data}')
        if re_data == 'end':
            break
def send_data():
    while True:
        #获取控制台信息
        msg=input('>')
        tcp_client_socket.send(msg.encode('gbk'))
if __name__ == '__main__':
    #创建socket对象
    tcp_server_socket=socket(AF_INET,SOCK_STREAM)
    #绑定端口
    tcp_server_socket.bind(('127.0.0.1',8888))
    #监听客户端的连接
    tcp_server_socket.listen()
    print("服务端已经启动，等待客户端连接!")
    #接收客户端的连接
    tcp_client_socket,host=tcp_server_socket.accept()
    print("一个客户端建立连接成功!")
    t1=Thread(target=recv_data)
    t2=Thread(target=send_data)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    tcp_client_socket.close()
    tcp_server_socket.close()