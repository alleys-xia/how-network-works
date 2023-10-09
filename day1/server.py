import socket

#创建套接字
server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#绑定ip,port
server_address= ('localhost', 10024)
server_socket.bind(server_address)

# 设置超时时间为10分钟
server_socket.settimeout(600)  # 单位是秒，这里设置为10分钟

#设置最大同时连接数并进行监听
server_socket.listen(5)
print('start listening...')

"""
client_socket 是服务器端套接字 accept() 方法返回的客户端套接字，它表示与客户端建立的连接。
在服务器端代码中，client_socket 已经包含了客户端的地址信息和端口信息，因为它代表了与特定客户端之间的通信通道。
"""
try:
	while True:
		#接收client传送的信息
		client_socket, client_address= server_socket.accept()
		request_data= client_socket.recv(1024).decode('utf-8')
		print(f'接收到的信息为{request_data}')
		# 构造HTTP响应
		response_data = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nHello, World!"
		client_socket.send(response_data.encode('utf-8'))
		client_socket.close()
except KeyboardInterrupt:
	print('server closed...')
	server_socket.close()

