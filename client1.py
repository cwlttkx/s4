import socket  # 导入socket模块以进行网络通信 运行环境：cmd 
import sys     # 导入sys模块以便处理命令行参数  
import os      # 导入os模块以进行文件操作  

def send_file(server_ip, server_port, file_path):  
    # 创建一个UDP套接字  
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    
    # 检查要发送的文件是否存在  
    if not os.path.isfile(file_path):  
        print(f"File {file_path} not found!")  # 如果文件不存在，输出错误信息  
        return  

    # 获取文件名  
    filename = os.path.basename(file_path)  
    # 向服务器发送一个指示开始传输文件的消息  
    client_socket.sendto(b'SEND_FILE', (server_ip, server_port))  
    # 发送文件名到服务器  
    client_socket.sendto(filename.encode(), (server_ip, server_port))  

    # 以二进制模式打开文件  
    with open(file_path, 'rb') as f:  
        bytes_read = f.read(1024)  # 读取文件的前1024字节  
        # 循环发送文件数据，直到文件全部发送完毕  
        while bytes_read:  
            client_socket.sendto(bytes_read, (server_ip, server_port))  # 发送读取的字节  
            bytes_read = f.read(1024)  # 继续读取下一段数据  

    print(f'File {filename} sent successfully.')  # 发送完成后输出成功信息  
    client_socket.close()  # 关闭套接字连接  

if __name__ == "__main__":  
    # 检查命令行参数的数量是否正确  
    if len(sys.argv) != 4:  
        print("Usage: python client.py <server_ip> <server_port> <file_path>")  # 输出用法提示  
        sys.exit(1)  # 退出程序  

    # 从命令行参数中获取服务器的IP地址、端口和文件路径  
    server_ip = sys.argv[1]  
    server_port = int(sys.argv[2])  
    file_path = sys.argv[3]  

    # 调用send_file函数发送文件  
    send_file(server_ip, server_port, file_path) 