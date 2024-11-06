import socket  # 导入socket模块以进行网络通信  运行环境：cmd
import os     # 导入os模块以进行文件操作  

def start_server(host='127.0.0.1', port=12345):  
    # 创建一个UDP套接字  
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    # 绑定套接字到指定的主机和端口  
    server_socket.bind((host, port))  
    print(f'Server is listening on {host}:{port}')  # 输出服务器正在监听的地址和端口  

    while True:  
        # 接收数据和客户端地址，缓冲区大小为1024字节  
        data, client_address = server_socket.recvfrom(1024)  
        # 检查接收到的数据是否为'SEND_FILE'指令  
        if data.decode() == 'SEND_FILE':  
            # 接收文件名  
            filename, _ = server_socket.recvfrom(1024)  
            filename = filename.decode()  # 解码文件名  
            print(f'Receiving file: {filename}')  # 输出正在接收的文件名  
            
            # 以二进制写模式打开文件  
            with open(filename, 'wb') as f:  
                while True:  
                    # 循环接收文件数据包  
                    bytes_packet, client_address = server_socket.recvfrom(1024)  
                    if not bytes_packet:  # 检查数据包是否为空  
                        break  # 如果数据包为空，退出循环  
                    f.write(bytes_packet)  # 将接收到的数据写入文件  
            
            print(f'File {filename} received successfully.')  # 输出文件接收成功的信息  

if __name__ == "__main__":  
    start_server()  # 启动服务器  