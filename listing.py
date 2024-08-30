import socket
import asyncio
import re
from dglab import *

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 10086))
    server.listen(1)
    print("Waiting for connection...")

    while True:
        conn, addr = server.accept()
        print("Connected by", addr)
        
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break
                message = data.decode().strip()

                if message == "ping":
                    # 收到 ping 消息时不执行任何操作
                    continue
                else:
                    # 使用正则表达式解析 "hit:xxxhp:yyy" 格式的消息
                    match = re.match(r"hit:(-?\d+(\.\d+)?)hp:(-?\d+(\.\d+)?)", message)
                    if match:
                        delta = float(match.group(1))
                        hp = float(match.group(3))

                        asyncio.run(send_message())
                        
                        print(f"Received delta value: {delta}, HP value: {hp}")
                    else:
                        print(f"Received unknown message: {message}")
                        
            except (ConnectionResetError, ConnectionAbortedError):
                print("Connection lost. Waiting for reconnection...")
                break  # 退出内部循环以重新启动服务器

        conn.close()

if __name__ == "__main__":
    while True:
        try:
            start_server()
        except Exception as e:
            print(f"Server encountered an error: {e}. Restarting server...")
