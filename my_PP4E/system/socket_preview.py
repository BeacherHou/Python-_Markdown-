#!/usr/bin/env python
"""
套接字用于跨任务通信，它传输字节字符串，后者可以是pickle后的对象或编码后的Unicode文本
"""

from socket import socket, AF_INET, SOCK_STREAM  # 可移植的套接字API
import time

PORT_INT = 50008
HOST = 'localhost'


def server():
	"服务器线程"
	sock = socket(AF_INET, SOCK_STREAM)  # tcp连接的ip地址
	sock.bind((HOST, PORT_INT))  # 绑定到这台机器的端口上
	sock.listen(5)  # 最多允许5个等待中的客户端

	while True:
		connection, address = sock.accept()  # 等待客户端连接
		data_bytes = connection.recv(1024)  # 从这个客户端读取字节数据
		reply_str = 'Server got: [{}]'.format(data_bytes)  # connection是一个新连接上的套接字
		connection.send(reply_str.encode())  # 将字节化的回复发给客户端


def client(name_str):
	"客户端进程"
	time.sleep(float(name_str[-1]))
	sock = socket(AF_INET, SOCK_STREAM)
	sock.connect((HOST, PORT_INT))  # 连接到一个套接字端口
	sock.send(name_str.encode())  # 向监听者发送字节数据
	reply_bytes = sock.recv(1024)  # 从监听者那里接受字节数据，信息最多包含1024字节
	sock.close()
	print('Client got: [{}]'.format(reply_bytes))


def main():
	from threading import Thread
	Thread(target=server, daemon=True).start()  # 不等待服务器进程（守护进程）
	
	for i_id_int in range(5):
		Thread(
			target=client, 
			args=('client {}'.format(i_id_int),)
		).start()  # 等待子进程结束


if __name__ == '__main__':
	main()
