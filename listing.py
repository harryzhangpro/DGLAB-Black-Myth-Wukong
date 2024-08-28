import socket
import asyncio
from dglab import send_message

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 10086))
server.listen(1)
print("Waiting for connection...")

conn, addr = server.accept()
print("Connected by", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    asyncio.run(send_message())
    print("Received:", data.decode())

# conn.close()
