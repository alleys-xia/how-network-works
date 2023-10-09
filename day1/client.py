import socket

"""
1.地址族(Address Family):socket.AF_INET（IPv4）或 socket.AF_INET6(IPv6)

2.套接字类型(Socket Type):socket.SOCK_STREAM：用于创建 TCP 套接字
                          socket.SOCK_DGRAM：用于创建 UDP 套接字
"""
client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#需要tuple类型 指定host 和 port
server_address= ('localhost', 10024)

#socket连接
client_socket.connect(server_address)
#get请求 以字符串类型保存
request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"

#编码成utf-8类型然后发送该get请求
client_socket.send(request.encode('utf-8'))

#接收服务器消息并解码
response_data= client_socket.recv(1024).decode('utf-8')
print(f"接收到服务器响应:\n{response_data}")

# 关闭客户端套接字
client_socket.close()




